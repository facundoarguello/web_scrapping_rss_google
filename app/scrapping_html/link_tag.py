def get_html_url_from_head_component(head_component) -> str:
    url_from_head = None
    try:
        url_tag = head_component.find('link', {'rel': "amphtml"})
        if url_tag:
            url_from_head = url_tag['href']
            return url_from_head
        url_tag = head_component.find('link', {'rel': 'canonical'})
        if url_tag:
            url_from_head = url_tag['href']
            return url_from_head
        url_tag = head_component.find('meta', {'property':'og:image'})
        if url_tag:
            url_from_head = url_tag['content']
            return url_from_head
        return url_from_head
    except Exception as error:
        print("Error in get_html_url_from_head_component, details: ", error)
        return url_from_head

def get_html_url_from_page(head_component) -> str:

    url_return = None
    try:
        url_return = get_html_url_from_head_component(head_component)
        # if url_return is None:
        #     url_return = get_html_url_from_body_component(body_component)
        return url_return
    except Exception as error:
        print("Error in get_html_url_from_page, details: ", error)
        return url_return