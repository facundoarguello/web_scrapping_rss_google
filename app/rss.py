import feedparser
from datetime import datetime
format_date = '%Y-%m-%d %H:%M:%S'
from request_page import get_text_from_page
from scrapping_html.scrapping import scrapping_html_and_return_obj
def verify_logo(logo_url:str, url_page:str) -> str:
    
    if 'http' not in logo_url:
        if  '/favicon.ico' in logo_url or  'favicon.png' in logo_url or  'favicon.jpg' in logo_url:
            logo_url = url_page + logo_url

    return logo_url
def get_info_rss_google(words:str) ->  list:
    "input- > words : string output -> list with items news"
    retur_list_news_from_rss = []
    try:
        google_rss_url = f'https://news.google.com/rss/search?q={words}+-site:ole.com.ar+-site:lavoz.com.ar&hl=es-419&gl=AR&ceidAR:es&ceid=AR:es-419'
        parser = feedparser.parse(google_rss_url)
    except feedparser.exceptions.NonXMLContentType as parser_error:
        print("Error parser:",parser_error)
        return retur_list_news_from_rss
    try:
        entries = parser['entries']
        #sacar del arreglo todas las que tengan el mismo id_rss_google
        retur_list_news_from_rss = sorted(entries, key=lambda item: item['published_parsed'], reverse=True)
        return retur_list_news_from_rss
    except Exception as error:
        print("Error then parser rss: " , error)
        return retur_list_news_from_rss
    
def get_list_info_from_scrappin_page_from_rss(items_from_rss:list, cantidad:int) -> list:
    arr_notes = []
    index = 0
    for item in items_from_rss:
        obj_note = {}
        response_text = None

        url_to_logo_tag = item['source']['url']
        link_to_page = item['link']
        author_for_the_note = item['source']['title']
        title_note = item['title']
        id_rss = item['id']
        fecha_original = item['published']
        # Convierte la fecha original a un objeto datetime
        fecha_datetime = datetime.strptime(fecha_original, '%a, %d %b %Y %H:%M:%S %Z')
        # Convierte la fecha datetime a un string con el formato deseado
        fecha_formateada = fecha_datetime.strftime(format_date)
        print("LOG: link:", link_to_page)
        print("LOG: index: ",index)
        response_text, type_page = get_text_from_page(link_to_page)

        if response_text is None:
            continue
        else:
            try:
                get_obj_scrap = None
                if 'text/html' in type_page:
                    get_obj_scrap = scrapping_html_and_return_obj(response_text)
                print("LOG: index: ",index)
                print("LOG: objetscrap: ",get_obj_scrap)

                if get_obj_scrap is None:
                    continue
                obj_note['id_rss_google'] = id_rss
                obj_note['title'] = title_note
                obj_note['date'] = fecha_formateada
                obj_note['author'] = author_for_the_note
                url_logo = verify_logo(get_obj_scrap['icon'], url_to_logo_tag)
                obj_note['icon'] = url_logo
                obj_note['description'] = get_obj_scrap['description']
                obj_note['image'] = get_obj_scrap['img']
                obj_note['href'] = get_obj_scrap['href']
                
                arr_notes.append(obj_note)
                index += 1
                if index == cantidad:
                    break
            except Exception as error:
                print("Error in for from fcuntion get_list_info_from_scrappin_page_from_rss, details: ", error)
                continue
    return arr_notes