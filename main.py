#!.venv/bin/python3

import os


def main():
    username = input()
    try:
        os.mkfifo('py-c')
    except FileExistsError:
        pass
    with open('py-c', 'wb') as f:
        f.write(username)


if __name__ == '__main__':
    main()
