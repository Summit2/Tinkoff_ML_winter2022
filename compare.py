import ast
import os
import numpy as np




def main():
    
    i = "input.txt"#input()
    o = "scores.txt"#input()
    paths=[]


    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    
    
    




if __name__ == "__main__":
    main()
