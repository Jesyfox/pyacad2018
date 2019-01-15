import json
import os
from .logger_battlefield import logger

FILE_NAME = 'battlefield/sides_template.json'


def get_side_pattern(template, file=FILE_NAME):
    logger.debug('# json_bridge getting side pattern')
    with open(file) as f:
        return json.load(f)[template]


def get_available_patterns(file=FILE_NAME):
    logger.debug('# json_bridge getting available patterns')
    with open(file) as f:
        return json.load(f)


def safe_pattern(template_name, file=FILE_NAME):
    logger.debug('# json_bridge saving pattern')
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({}, f, indent=4)
    with open(file) as f:
        json_db = json.load(f)
        json_db.update(template_name)
    with open(file, 'w') as f:
        json.dump(json_db, f, indent=4)


def delete_pattern(template_key, file=FILE_NAME):
    logger.debug('# json_bridge deleting pattern')
    with open(file) as f:
        json_db = json.load(f)
        json_db.pop(template_key)
    with open(file, 'w') as f:
        json.dump(json_db, f, indent=4)
