import json
def get_html_description_from_head_component(head_component) -> str:
    print(type(head_component))
    description_from_head = None
    try:
        
        description_tag = head_component.find('meta',{'property':'og:description'})
        if description_tag is not None:
            description_from_head = description_tag['content']
            return description_from_head
        description_tag = head_component.find('meta',{'name':'description'})
        if description_tag is not None:
            description_from_head = description_tag['content']
            return description_from_head
        description_tag_arr_scripts = head_component.find_all('script', {'type': 'application/ld+json'})
        if description_tag_arr_scripts is not None:
            for script in description_tag_arr_scripts:
                try:
                    json_sript = json.loads(script.string)
                    if json_sript is not None:
                        if 'description' in json_sript:
                            description = json_sript['description']
                            description_from_head = description
                            print("desescriptionsscript", description_from_head)
                            return description_from_head
                except Exception as err:
                    print("Error inside for script",err)
                    continue
        return description_from_head
    except Exception as error:
        print("Error in get_html_description_from_head_component, details: ", error)
        return description_from_head
    
def get_html_description_from_page(head_component, body_component) -> str:

    description_return = None
    try:
        description_return = get_html_description_from_head_component(head_component)
        # if description_return is None:
        #     description_return = get_html_url_from_body_component(body_component)
        return description_return
    except Exception as error:
        print("Error in get_html_description_from_page, details: ", error)
        return description_return