import urllib2
import re

class PageCache(dict):
    """
    This is just a basic dictionary object.  I am 
    overriding it to add a new page if the dictionary 
    doesn't already have a page for the URL.
    """
    def __init__(self, *args):
        dict.__init__(self, args)

    def __getitem__(self, key):
        """"
        Retrieves a page. If the page has already
        been retrieved, this method pulls it from cache.
        """
        if not key in dict.keys(self):
            dict.__setitem__(self, key, Page(key))

        return dict.__getitem__(self, key)


 
class Page(object):
    """
    This class is used to read a page from a URL and store its contents.
    It also contains methods for examining the contents of a page.
    """
    html = ''
    status_code = 0
    headers = {}
    get_url = ''
    url = ''

    # This is a backing property for the parsed_html property
    _parsed_html = None
    _title = ''


    def __init__(self, url=None):

        if url:
            self.url = url

            try:
                page = urllib2.urlopen(url, timeout=3)
            except urllib2.HTTPError, error:
                page = error
            
            if page:
                self.status_code = page.getcode()
                self.headers = page.headers
                self.get_url = page.geturl()

                for line in page.readlines():
                    self.html += line    
                page.close()

    @property
    def title(self):
        if not self._title:
            self._title = self.parsed_html.title.string
        
        return self._title

    def exists(self):
        """
        Return True if a request for this page 
        returned a status code in the 200s
        """

        if str(self.status_code)[0] == '2':
            return True
        else:
            return False  

    def contains_pattern(self, pattern, ignorecase=False):
        """
        Returns True if the given page contains a particular string.
        """
        result = False
        if ignorecase:
            rgx = re.compile(pattern, re.IGNORECASE)
        else:
            rgx = re.compile(pattern)

        if self.html and rgx.search(self.html):
                result = True

        return result 

    def contains_any_pattern(self, patterns):
        """
        Returns a True if any of the patterns are found in the page
        """

        for pattern in patterns:
            if self.contains_pattern(pattern):
                return True

        return False


    def contains_all_patterns(self,patterns):
        """
        Returns a false unless all of the patterns are found in the page
        """

        for pattern in patterns:
            if not self.contains_pattern(pattern):
                return False

        return True


    def is_dot_net_webforms(self):
        """
        Returns True is the URL has .Net WebForm markers.
        """
        result = False

        if 'x-powered-by' in self.headers and self.headers['x-powered-by'] == 'ASP.NET':
            result = True

        if self.contains_any_pattern(('id="aspnetform"','ct100_','name="__VIEWSTATE"')):
            result = True

        return result

    def has_php_credits(self):
        """
        Checks for the easter egg where the PHP credits page 
        appears when you add the query string:
        ?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000
        """
        credits_page = Page(self.url + "?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000")
        return credits_page.contains_pattern('PHP Credits')

    def has_matching_tag(self, tag_name, attributes, ignorecase = True):
        """
        Iterates all specified tags and compares the specified attribute
        against a supplied pattern.

        Usage:

        To look for a tag like:
        <meta name="generator" content="Joomla">

        do:

        page.has_matching_tag('meta' {'name':'generator'; 'content':'joomla'})

        Note, the default search is case insensitive.

        """

        # I feel like I can really boil this down by doing something like

        for k in attributes.keys():
            if ignorecase:
                attributes[k] = re.compile(attributes[k], re.IGNORECASE)
            else:
                attributes[k] = re.compile(attributes[k])

        if self.parsed_html.findAll(name=tag_name, attrs=attributes):
            return True
        else:
            return False



    def has_tag_containing_pattern(self, tag_name, pattern, ignorecase=True):
        """
        Looks for a regex expression within a given tag.

        Usage:

        To look for a tag like:
        <script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-28302554-1']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

        </script>

        you might do something like:

        page.has_tag_containing_pattern('script', '\.google-analytics.com/ga\.js')

        Note, the default search is case insensitive.
        """

        if ignorecase:
            rgx = re.compile(pattern, re.IGNORECASE)
        else:
            rgx = re.compile(pattern)

        if self.parsed_html.findAll(tag_name, text=rgx):
            return True
        else:
            return False




    @property
    def parsed_html(self):
        """
        Returns HTML parsed by Beautiful Soup.  Caches the parse for future requests.
        """
        if self._parsed_html:
            return self._parsed_html

        from BeautifulSoup import BeautifulSoup
        self._parsed_html = BeautifulSoup(self.html)
        return self._parsed_html
