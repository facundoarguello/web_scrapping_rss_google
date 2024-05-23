from bs4 import BeautifulSoup
from .description_tag import get_html_description_from_page
from .icon_tag import get_html_logo_from_page
from .image_tag import get_html_image_from_page
from .link_tag import get_html_url_from_page
def scrapping_html_and_return_obj(response_text:str) -> dict:
    #Parser text to html
    html = BeautifulSoup(response_text, 'html.parser')
    head_component = html.find('head')
    body_component =  html.find('body')
    scrap_obj = None
    if head_component is not None:
        scrap_obj = {
            
        }
        url_clean = get_html_url_from_page(head_component)
        if url_clean is None:
            return None
        scrap_obj['href'] = url_clean
        logo_clean = get_html_logo_from_page(head_component)
        if logo_clean is None:
            return None
        scrap_obj['icon'] = logo_clean
        img_clean = get_html_image_from_page(head_component, body_component)
        if img_clean is None:
            return None
        scrap_obj['img'] = img_clean
        description_clean = get_html_description_from_page(head_component, body_component)
        if description_clean is None:
            return None
        scrap_obj['description'] = description_clean

        return scrap_obj
    return scrap_obj