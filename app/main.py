from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from models.ScrapperRequest import ScrapperRequest
from rss import get_info_rss_google
from rss import get_list_info_from_scrappin_page_from_rss
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World Pibeishon"}

@app.post("/scrappe/")
async def create_item(request: ScrapperRequest):
    try:
        words = request.words
        amount = request.amount
        list_items_rss = []
        list_items_rss = get_info_rss_google(words)
        if len(list_items_rss) > 0:
            list_objects_notes = get_list_info_from_scrappin_page_from_rss(list_items_rss, amount)
            return list_objects_notes
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))