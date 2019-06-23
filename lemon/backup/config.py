import json
import os
import re

HOME = os.environ['HOME']

CONFIG_PATH = '{0}/config.json'.format(os.path.dirname(__file__))

TYPES = [
    'default',
    'time'
]

BACKUP_FOLDER = 'lemon_backup'

FILES = {

}

DEFAULT = {
    'srcs': [
        '{0}/.ssh'.format(HOME),
    ],
    'dest': '{0}/Dropbox'.format(HOME),
    'type': 'default'
}

CONFIG = DEFAULT


def filter(srcs):
    i = j = 0
    while i < len(srcs) - 1:
        src = srcs[i]
        j = i+1
        while j < len(srcs):
            sub_src = srcs[j]
            if src in sub_src:
                del srcs[j]
            else:
                j += 1
        i += 1

    return srcs


def save():
    global CONFIG
    CONFIG['srcs'] = filter(sorted(CONFIG['srcs']))
    with open(CONFIG_PATH, 'w') as json_file:
        json.dump(CONFIG, json_file, indent=4)


def load():
    with open(CONFIG_PATH, 'r') as json_file:
        global CONFIG
        CONFIG = json.load(json_file)


def strim_path(src):
    path = src.strip()
    if len(path):
        if path[-1] == '/':
            return path[:-1]
        return path

    return None


def view_config():
    load()
    print(json.dumps(CONFIG, indent=4))


def generate():
    """Get configuration
    """

    # Get backup resources
    srcs = get_srcs()
    if not len(srcs):
        choice = raw_input(
            'Backup sources is empty. Do you want to save it? (y/n) [n]').lower()
        if choice == 'y':
            CONFIG['srcs'] = srcs
    else:
        CONFIG['srcs'] = srcs

    # Get backup destination
    dest = get_dest()
    if dest:
        CONFIG['dest'] = dest

    # Get backup type
    type_ = get_type()
    if type_:
        CONFIG['type'] = type_

    save()


def change_config(func):
    def inner(*args, **kwargs):
        load()
        func(*args, **kwargs)
        save()
    return inner


@change_config
def add_srcs():
    srcs = get_srcs()
    if len(srcs):
        for src in srcs:
            if src not in CONFIG['srcs']:
                CONFIG['srcs'].append(src)


@change_config
def set_srcs():
    srcs = get_srcs()
    if len(srcs):
        CONFIG['srcs'] = srcs


@change_config
def set_dest():
    dest = get_dest()
    if dest:
        CONFIG['dest'] = dest


@change_config
def set_type():
    type_ = get_type()
    if type_:
        CONFIG['type'] = type_


def get_srcs():
    """Set backup resources
    """

    src_raw = raw_input(
        'Backup files or folders (Separate by comma or space): ')
    srcs_ = re.split(' |, |,', src_raw)
    srcs = []
    for src in srcs_:
        trim = strim_path(src)
        if trim and trim not in srcs:
            if os.path.exists(trim):
                srcs.append(trim)
            else:
                print('{0} does not exist'.format(trim))

    return srcs


def get_dest():
    """Set backup destination
    """

    src_raw = raw_input('Backup destination [{0}/Dropbox]: '.format(HOME))
    trim = strim_path(src_raw)
    if trim and os.path.exists(trim):
        return trim
    else:
        print('{0} does not exist'.format(trim))

    return None


def get_type(save=False):
    """Set backup type
    """
    trim = raw_input('Type [default]: ').strip().lower()

    if trim in TYPES:
        return trim

    return None


def reset():
    global CONFIG
    CONFIG = DEFAULT
    save()
