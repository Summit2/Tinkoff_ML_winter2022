import os
import numpy as np

# class File():

    
        
        
#     def __init__(self,paths) -> None:
#         self.paths=paths 
        
#         with open (self.paths ,"rt") as text:
#             self.text=text
    
#     def distance(self):
#         pass

def main():
    
    i = "input.txt"#input() #файл с указанием путей для файлов
    o = "scores.txt"#input() #файл с итоговыми значениями
    paths=[]
    

    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    

    for s in paths:
        s1,s2="",""
        with open (s[0],"rt") as string:
            for text in string:
             s1+=' '.join(text.split(" "))
        with open (s[1],"rt") as string:
           for text in string:
             s2+=' '.join(text.split(" "))
        print(distance(str(s1),str(s2)))
        
        
        
    
    


def distance(s1, s2):
    "Считает расстояние Левенштейна от а до b"
    n, m = len(s1), len(s2)
    if n > m:
        
        s1, s2 = s2,s1
        n, m = m, n

    cur = range(n + 1) 
    for i in range(1, m + 1):
        prev, cur = cur, [i] + [0]*n
        for j in range(1,n + 1):
            add, delete, change = prev[j] + 1, cur[j - 1] + 1, prev[j - 1]
            if s1[j - 1] != s2[i - 1]:
                change += 1
            cur[j] = min(add, delete, change)

    return cur[n]

if __name__ == "__main__":
    main()
    
