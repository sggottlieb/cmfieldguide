
name = 'WordPress'

def run():

    results = {}
    results[test_has_wpadmin.__doc__] = test_has_wpadmin()
    results[test_has_wptheme.__doc__] = test_has_wptheme()

    return results


def test_has_wpadmin():
    """Has a valid URL at wp-admin."""
    return -1

def test_has_wptheme():
    """Has a WP-Theme directory."""
    return -1