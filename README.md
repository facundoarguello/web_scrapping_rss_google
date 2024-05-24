# web_scrapping_rss_google
Repository where I practice web scraping from an RSS feed and then its different links with python beautiful soup


### Pre-request📋

_You need venv to virtual enviroment and python 3.8_
_Install fastappi, python, beatifulsoap. No worried beacause all instalations are inside the requiremnt_

### Installation 🔧

_create venv_
```
python -m venv env
```
_activate venv_
```
source env/bin/activate
```
_Install requiremnts_

```
pip install -r requirements.txt
```

## Testing ⚙️

_Then the installation. We let's raise our api_
```
cd app
uvicorn main:app --reload 
```
_ the console will show this_
```
INFO:     Will watch for changes in these directories: ['your_directory/web_scrapping_rss_google/app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2115075] using WatchFiles
INFO:     Started server process [2115134]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
_And test the api_
_You send the endpoint http://127.0.0.1:8000/scrappe_
```
with body:{
    words: deporte+futbol+voley (Words where search in rss)
    amount: 5 (number of notes to be made)
}
```

_result example_
```
[
    {
        "id_rss_google": "CBMiuwFodHRwczovL3d3dy5pbmZvYmFlLmNvbS9kZXBvcnRlcy8yMDI0LzA1LzI0L2xvcy1kZXRhbGxlcy1kZS1sYS1sdWpvc2EtbWFuc2lvbi1xdWUta3lsaWFuLW1iYXBwZS1jb21wcm8tZW4tbWFkcmlkLWRvcy1waXNjaW5hcy1jaW5lLWNhbmNoYS1kZS10ZW5pcy15LXVuYS1lc3RyZWxsYS1kZS1ob2xseXdvb2QtY29tby12ZWNpbm8v0gHPAWh0dHBzOi8vd3d3LmluZm9iYWUuY29tL2RlcG9ydGVzLzIwMjQvMDUvMjQvbG9zLWRldGFsbGVzLWRlLWxhLWx1am9zYS1tYW5zaW9uLXF1ZS1reWxpYW4tbWJhcHBlLWNvbXByby1lbi1tYWRyaWQtZG9zLXBpc2NpbmFzLWNpbmUtY2FuY2hhLWRlLXRlbmlzLXktdW5hLWVzdHJlbGxhLWRlLWhvbGx5d29vZC1jb21vLXZlY2luby8_b3V0cHV0VHlwZT1hbXAtdHlwZQ",
        "title": "Los detalles de la lujosa mansión que Kylian Mbappé compró en Madrid: dos piscinas, cine, cancha de tenis y una estrella de Hollywood como vecino - infobae",
        "date": "2024-05-24 01:45:00",
        "author": "infobae",
        "icon": "https://www.infobae.com/pf/resources/favicon/favicon.ico?d=2262",
        "description": "Los medios españoles aseguran que Sergio Ramos lo asesoró en la operación y que invirtió entre 10 y 15 millones de dólares",
        "image": "https://www.infobae.com/new-resizer/Jy46bZKp5WAFejOyrCRzZ-uQv3k=/1200x630/filters:format(webp):quality(85)/cloudfront-us-east-1.images.arcpublishing.com/infobae/FPO7IQN3IJGQJOHGJWGCJM77DQ.jpg",
        "href": "https://www.infobae.com/deportes/2024/05/24/los-detalles-de-la-lujosa-mansion-que-kylian-mbappe-compro-en-madrid-dos-piscinas-cine-cancha-de-tenis-y-una-estrella-de-hollywood-como-vecino/?outputType=amp-type"
    },
    {
        "id_rss_google": "CBMiXmh0dHBzOi8vd3d3LmxhcHJlbnNhLmNvbS5hci9CZW5lZGV0dG8tdm9sdmlvLWEtcXVlZGFyLWZ1ZXJhLWRlLWxvcy1jb252b2NhZG9zLTU0NTAyNy5ub3RlLmFzcHjSAQA",
        "title": "Benedetto volvió a quedar fuera de los convocados - Diario La Prensa",
        "date": "2024-05-23 23:11:26",
        "author": "Diario La Prensa",
        "icon": "https://www.laprensa.com.ar/assets/imgs/favicon.ico",
        "description": "",
        "image": "https://www.laprensa.com.ar/Multimedios/Imgs/176259_620.webp?v=4",
        "href": "https://www.laprensa.com.ar/amp/Benedetto-volvio-a-quedar-fuera-de-los-convocados-545027.note.aspx"
    },
    {
        "id_rss_google": "CBMiK2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9OEFpa3JrbXNyY2fSAQA",
        "title": "#ENVIVO🔴 | JORGE FOSSATI ANUNCIA A SUS CONVOCADOS PARA AMISTOSOS Y COPA AMÉRICA ESTADOS ... - YouTube",
        "date": "2024-05-23 21:29:44",
        "author": "YouTube",
        "icon": "https://www.youtube.com/s/desktop/fcc2ca55/img/favicon.ico",
        "description": "El director técnico de la Selección Peruana, Jorge Fossati, anuncia a sus convocados para los partidos amistosos frente a Paraguay y El Salvador previos a la...",
        "image": "https://i.ytimg.com/vi/8Aikrkmsrcg/maxresdefault.jpg",
        "href": "https://www.youtube.com/watch?v=8Aikrkmsrcg"
    },
    {
        "id_rss_google": "CBMijwFodHRwczovL3d3dy5lbGRlc3RhcGV3ZWIuY29tL2RlcG9ydGVzL2luZGVwZW5kaWVudGUvaW5kZXBlbmRpZW50ZS1xdWllbi1lcy1uaWNvbGFzLWxhcmNhbW9uLWVsLWR0LXF1ZS1wdWVkZS1zZXItcmVlbXBsYXpvLWRlLXRldmV6LTIwMjQ1MjMxNzM0MNIBjwFodHRwczovL3d3dy5lbGRlc3RhcGV3ZWIuY29tL2RlcG9ydGVzL2luZGVwZW5kaWVudGUvaW5kZXBlbmRpZW50ZS1xdWllbi1lcy1uaWNvbGFzLWxhcmNhbW9uLWVsLWR0LXF1ZS1wdWVkZS1zZXItcmVlbXBsYXpvLWRlLXRldmV6LTIwMjQ1MjMxNzM0MA",
        "title": "Independiente: Quién es Nicolás Larcamón, el DT que puede ser reemplazo de Tevez - El Destape",
        "date": "2024-05-23 21:01:21",
        "author": "El Destape",
        "icon": "https://www.eldestapeweb.com/img/favicons/favicon.ico",
        "description": "El técnico suena para independiente como reemplazo de Carlos Tevez. Se trata de un entrenador importante para el Rojo. ",
        "image": "https://cdn.eldestapeweb.com/eldestape/052024/1716497878291.jpg?&cw=600&ch=365",
        "href": "https://www.eldestapeweb.com/deportes/independiente/independiente-quien-es-nicolas-larcamon-el-dt-que-puede-ser-reemplazo-de-tevez-202452317340"
    },
    {
        "id_rss_google": "CBMicWh0dHBzOi8vd3d3LmNhZGVuYTMuY29tL25vdGljaWEvdGFsbGVyZXMvY2FkZW5hLTMtY2luZXMtZGluby15LXRhbGxlcmVzLXByZXNlbnRhbi1saWJlcnRhZG9yZXMtZGUtcGVsaWN1bGFfMzg4MzQw0gF1aHR0cHM6Ly93d3cuY2FkZW5hMy5jb20vYW1wL25vdGljaWEvdGFsbGVyZXMvY2FkZW5hLTMtY2luZXMtZGluby15LXRhbGxlcmVzLXByZXNlbnRhbi1saWJlcnRhZG9yZXMtZGUtcGVsaWN1bGFfMzg4MzQw",
        "title": "Cadena 3, Cines Dino y Talleres presentan: Libertadores de Película - Cadena 3",
        "date": "2024-05-23 20:40:39",
        "author": "Cadena 3",
        "icon": "https://www.cadena3.com/img/cadena3com.ico",
        "description": "El duelo con Sao Paulo se podrÃ¡ ver en los cines Dino. DisfrutÃ¡ el partido junto a Cadena 3 y participÃ¡ por un viaje para dos personas para el prÃ³ximo encuentro de la T en octavos de final.",
        "image": "https://www.cadena3.com/admin/playerswf/fotos/ARCHI_1110965.jpg",
        "href": "https://www.cadena3.com/amp/noticia/talleres/cadena-3-cines-dino-y-talleres-presentan-libertadores-de-pelicula_388340"
    }
]
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python3.8](https://www.python.org/downloads/release/python-380/) - Language
* [fastapi](https://fastapi.tiangolo.com/#installation) - Api rest
* [Beatifulsoap](https://beautiful-soup-4.readthedocs.io/en/latest/) - Scrapper
* [feedparser](https://feedparser.readthedocs.io/en/latest/)- parser rss


## Authors ✒️
* **Facundo Argüello** - *Trabajo Inicial* - [facuarguello](https://github.com/facundoarguello)

