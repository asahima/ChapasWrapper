# coding: utf-8

from Chapas import Chapas
from config import CHAPAS_PATH

def main():
    chapas = Chapas(CHAPAS_PATH)
    result = chapas.parse("./sample.txt", "cat")
    
    for items in result:
        for item in items:
            print(item)

if __name__ == "__main__":
    main()
