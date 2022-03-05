import typer

from parser.app.config import CONFIG, SOURCES
# from parser.app.telegram import tg
from parser.app.web import web

app = typer.Typer(help="Parse sources")


@app.command()
def parse(source_name):
    source = SOURCES["sources"][source_name]
    if source['type'] == 'web':
        web(source_name)


if __name__ == "__main__":
    app()
