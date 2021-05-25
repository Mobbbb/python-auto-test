def is_element_exist(element, css):
    s = element.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        return False
    else:
        return True
