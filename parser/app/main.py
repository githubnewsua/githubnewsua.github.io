import typer

from parser.app.config import CONFIG
from parser.app.telegram import tg

app = typer.Typer(help="Parse sources")


@app.command()
def parse(source_name):
    source = CONFIG["sources"][source_name]
    if source['type'] == 'telegram':
        tg(source['channel'])


if __name__ == "__main__":
    app()
