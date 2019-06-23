import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-v', '--version', action='store_true',
                        help='an integer for the accumulator')

    parser.add_argument('task', type=str, nargs='?',
                        help='an integer for the accumulator')

    # Arguments for backup task
    parser.add_argument('-config', action='store_true',
                        help='an integer for the accumulator')
    parser.add_argument('-view', action="store_true",
                        help='an integer for the accumulator')
    parser.add_argument('-set', action="store", dest="set",
                        help='an integer for the accumulator')
    parser.add_argument('-add', action="store", dest="add",
                        help='You must specify the type of resource to set')

    parser.add_argument("-g", "--generate", action='store_true',
                        help="increase output verbosity")
    parser.add_argument("-r", "--reset", action='store_true',
                        help="increase output verbosity")

    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('-a', action="store", dest="a")
    # group.add_argument('-b', action="store", dest="b")

    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                    help='an integer for the accumulator')

    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                    const=sum, default=max,
    #                    help='sum the integers (default: find the max)')

    # parser.add_argument("-v", "--verbose", help="increase output verbosity")

    # parent_parser = argparse.ArgumentParser(add_help=False)
    # parent_parser.add_argument('--user', '-u',
    #                            default='nguyencuong',
    #                            help='username')
    # parent_parser.add_argument('--debug', default=False, required=False,
    #                            action='store_true', dest="debug", help='debug flag')

    # main_p = argparse.ArgumentParser()

    # main_sub_p = main_p.add_subparsers(title='main parser')

    # backup_p = main_sub_p.add_parser('backup', help='backup data')
    # other_p = main_sub_p.add_parser('other', help='other fucntion')

    # backup_sub_p = backup_p.add_subparsers(title='backup', dest="backup")

    # config_p = backup_sub_p.add_parser('config', help='backup config')

    # config_sub_p = config_p.add_subparsers(title='config', dest="backup_config")

    # config_sub_p.add_parser('view', help='view config')
    # set_ = config_sub_p.add_parser('set', help='view config')

    # set_.add_argument('func', nargs='?')

    # config_sub_p.add_parser('add', help='view config')

    # service_subparsers = main_p.add_subparsers(title="service",
    #                     dest="service_command")

    # service_parser = service_subparsers.add_parser("first", help="first",
    #                     parents=[parent_parser])

    # action_subparser = service_parser.add_subparsers(title="action",
    #                     dest="action_command")

    # action_parser = action_subparser.add_parser("second", help="second",
    #                     parents=[parent_parser])

    # args = main_p.parse_args()

    args = parser.parse_args()

    def run_backup(args):
        from backup import backup
        if args.config:
            from backup import config

            if args.set:
                func = getattr(config, 'set_{0}'.format(args.set))
                func()
            elif args.add:
                func = getattr(config, 'add_{0}'.format(args.add))
                func()
            elif args.view:
                config.view_config()

            if args.generate:
                config.generate()
            elif args.reset:
                config.reset()
        else:
            backup.backup()

    if args.version:
        print('lemon-1.0')

    if args.task == 'backup':
        run_backup(args)
