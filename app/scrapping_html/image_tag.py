import json
def get_html_image_from_head_component(head_component) -> str:
    image_from_head = None
    try:
        image_tag = head_component.find('meta',{'property':'og:image'})
        if image_tag is not None:
            image_from_head = image_tag['content']
            return image_from_head
        image_tag_arr_scripts = head_component.find_all('script', {'type': 'application/ld+json'})
        if image_tag_arr_scripts is not None:
            for script in image_tag_arr_scripts:
                try:
                    json_sript = json.loads(script.string)
                    if json_sript is not None:
                        if 'image' in json_sript:
                            image = json_sript['image']
                            img_url = image[0]['url']
                            image_from_head = img_url
                            return image_from_head
                except Exception as err:
                    print("Error inside for script",err)
                    continue
        return image_from_head
    except Exception as error:
        print("Error in get_html_image_from_head_component, details: ", error)
        return image_from_head

def get_html_image_from_page(head_component, body_component) -> str:

    image_return = None
    try:
        image_return = get_html_image_from_head_component(head_component)
        # if image_return is None:
        #     image_return = get_html_url_from_body_component(body_component)
        return image_return
    except Exception as error:
        print("Error in get_html_image_from_page, details: ", error)
        return image_return