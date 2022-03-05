import yaml
from pathlib import Path


config_path = Path(__file__).resolve().parent.parent / 'config.yml'
sources_path = Path(__file__).resolve().parent.parent / 'sources.yml'
output_path = Path(__file__).resolve().parent.parent.parent


def read_config(path):
    with path.open() as file:
        return yaml.load(file, Loader=yaml.FullLoader)


CONFIG = read_config(config_path)
SOURCES = read_config(sources_path)
