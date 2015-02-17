# coding: utf-8

from Chapas import Chapas

def main():
    chapas = Chapas("./chapas.jar")
    chapas.parse("./sample.txt")
    chapas.result()

if __name__ == "__main__":
    main()
