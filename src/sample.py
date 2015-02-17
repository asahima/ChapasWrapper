# coding: utf-8

from Chapas import Chapas

def main():
    chapas = Chapas("~/Downloads/chapas-0.742/chapas.jar")
    result = chapas.parse("./sample.txt")
    
    for items in result:
        for item in items:
            print(item)

if __name__ == "__main__":
    main()
