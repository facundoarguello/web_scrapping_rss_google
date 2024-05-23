import json
def get_html_logo_from_head_component(head_component) -> str:
    logo_from_head = None
    try:
        logo_tag = head_component.find('link', {'rel': 'icon'})
        if logo_tag is not None:
            logo_from_head = logo_tag['href']
            return logo_from_head
        if logo_tag['rel'] ==['shortcut','icon']:
            logo_from_head = logo_tag['href']
            return logo_from_head
        logo_tag_arr_scripts = head_component.find_all('script', {'type': 'application/ld+json'})
        if logo_tag_arr_scripts is not None:
            for script in logo_tag_arr_scripts:
                try:
                    json_sript = json.loads(script.string)
                    if json_sript is not None:
                        if 'publisher' in json_sript:
                            publisher = json_sript['publisher']
                            logo = publisher['logo']
                            url = logo['url']
                            logo_from_head = url
                            return logo_from_head
                except Exception as err:
                    print("Error inside for script",err)
                    continue
                
        return logo_from_head
    except Exception as error:
        print("Error in get_html_logo_from_head_component, details: ", error)
        return logo_from_head

def get_html_logo_from_page(head_component) -> str:

    logo_return = None
    try:
        logo_return = get_html_logo_from_head_component(head_component)
        return logo_return
    except Exception as error:
        print("Error in get_html_logo_from_page, details: ", error)
        return logo_return