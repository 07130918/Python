from optparse import OptionParser
from optparse import OptionGroup


def main():
    usage = 'usage: %prog [options] arg1 arg2'
    paser = OptionParser(usage=usage)

    paser.add_option('-f', '--file', action='store', type='string',
                     dest='filename', help='File name')
    paser.add_option('-n', '--num', action='store', type='int', dest='num')
    paser.add_option('-v', action='store_true', dest='verbose', default=True)
    paser.add_option('-q', action='store_false', dest='verbose')

    paser.set_defaults(num=100)

    paser.add_option('-r', action='store_const',
                     const='root', dest='user_name')
    paser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, paser):
        if paser.values.env == 'prd':
            raise paser.error('Can not release')
        setattr(paser.values, option.dest, 'SUCCESS')

    paser.add_option('--release', action='callback',
                     callback=is_relase, dest='release')

    group = OptionGroup(paser, 'Dangerous group')
    group.add_option('-g', action='store_true', help='Group option')
    paser.add_option_group(group)

    options, args = paser.parse_args()
    print(options)
    # destから
    print('options.filename:', options.filename)
    print('options.num:', options.num)
    print('options.release:', options.release)
    print('args:', args)


if __name__ == '__main__':
    main()
