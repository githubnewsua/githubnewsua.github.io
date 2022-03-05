import typer
from pywebcopy import save_webpage

from parser.app.config import CONFIG, SOURCES, output_path


def web(source_name):
    source = SOURCES["sources"][source_name]
    url = source["url"]

    typer.echo(f"Saving {url} to {output_path}")

    kwargs = {'bypass_robots': True, 'project_name': "pages"}

    save_webpage(url, str(output_path), **kwargs)
