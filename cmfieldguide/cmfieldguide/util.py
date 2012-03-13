import httplib
from urlparse import urlparse



def get_url(url):
    #Parse the URL to get the host and the path
    parsed_url = urlparse(self.url)
    domain = parsed_url.netloc
    path = parsed_url.path + '?' + parsed_url.query if parsed_url.query else parsed_url.path

    # Grab the page via HTTP
    conn = httplib.HTTPConnection(domain)
    conn.request('GET', path)
    response = conn.getresponse()

    return response