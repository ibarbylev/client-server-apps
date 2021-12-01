import sys


def my_func():
    print(sys.argv[2])


def get_port_number():
    try:
        args = sys.argv
        if '-p' in args:
            port_number = args.index('-p') + 1
            return args[port_number]
    except IndexError:
        print('ERROR! After parameter -p must be the port number!')


if __name__ == "__main__":
    print(get_port_number())
