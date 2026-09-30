import os


if __name__ == '__main__':
    print("Me estoy ejecutando desde:")
    path = os.getcwd()
    print(path)
    content = open("hello world.txt").read()
    print(content)
