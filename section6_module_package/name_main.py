import config


def main():
    print('name_main:', __name__)


# 外からimportされた時に実行されることを防ぐ
if __name__ == '__main__':
    main()
