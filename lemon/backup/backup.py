import datetime
import os
from distutils.dir_util import copy_tree
from . import config


def _mkdir_recursive(path):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        _mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)


def create_folder(path):
    if not os.path.isdir(path):
        print('Creating folder: {0}'.format(path))
        os.mkdir(path)


def backup():
    config.load()
    type_ = config.CONFIG['type']
    dest = '{0}/{1}'.format(config.CONFIG['dest'], config.BACKUP_FOLDER)

    if type_ == 'default':
        dest = '{0}/{1}'.format(dest, type_)

    elif type_ == 'time':
        date_f = datetime.datetime.now().strftime("%Y-%m-%d")
        dest = '{0}/{1}'.format(dest, date_f)

    _mkdir_recursive(dest)

    srcs = config.CONFIG['srcs']

    if len(srcs):
        for src in srcs:
            print('Backupping {0}'.format(src))
            sub_dest = '{0}/{1}'.format(dest, src)
            _mkdir_recursive(sub_dest)
            copy_tree(src, sub_dest)
    print('Success')
