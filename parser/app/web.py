from pywebcopy import save_webpage

from parser.app.config import CONFIG, SOURCES


def web(source):
    source = SOURCES[source]
    download_folder = '/path/to/downloads/'

    kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

    save_webpage(url, download_folder, **kwargs)
