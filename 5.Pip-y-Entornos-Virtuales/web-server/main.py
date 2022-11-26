from store import get_categorys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =  FastAPI()


@app.get('/')
def get_list():
    return [
        1, 2, 3, 4, 5
    ]


@app.get('/contacto', response_class=HTMLResponse)
def get_contact():
    return """
        <h1> Hola soy una pagina </h1>
        <p> Soy un parrafo, desde vs code </p>
    """


def run():
    get_categorys()

if __name__ == '__main__':
    run()