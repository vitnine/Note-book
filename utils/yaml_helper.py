from typing import Dict, Any

import yaml


def load_yaml_files(*paths: str, loader: yaml.Loader) -> Dict[str, Any]:
    yaml_files = {}
    for path in paths:
        with open(path) as file:
            yaml_content = yaml.load(stream=file, Loader=loader)
        yaml_files[path] = yaml_content
    return yaml_files