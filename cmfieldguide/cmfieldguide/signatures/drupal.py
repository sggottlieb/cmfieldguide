
name = 'Drupal'

def run():

    results = {}
    results[test_has_sites_path.__doc__] = test_has_sites_path()
    results[test_has_node_class_on_body_tag.__doc__] = test_has_node_class_on_body_tag()

    return results


def test_has_sites_path():
    """Has a /sites/all path in HTML."""
    return -1

def test_has_node_class_on_body_tag():
    """Has a class containing 'node' on the BODY tag."""
    return -1
