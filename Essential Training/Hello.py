import platform
import serial


def main():  # function
    message()

def message():  # function
    print('Hello this is a python piatform  {}'.format(platform.python_version()))

if __name__ == '__main__':
    main()

