import argparse


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to dataset', type=str)  # 位置参数
    parser.add_argument('-c', '--cuda', help='use cuda', action='store_true')
    parser.add_argument('-e', '--epoch', type=int, help='epochs')
    options = parser.parse_args(args)
    print(options)


if __name__ == '__main__':
    main('-c', '/user/cui', '--epoch', '50') # 可选参数不影响位置参数的使用
