import os
import numpy as np

# class File():

    
        
        
#     def __init__(self,paths) -> None:
#         self.paths=paths 
        
#         with open (self.paths ,"rt") as text:
#             self.text=text
    
#     def distance(self):
#         pass
def delete_element_from_list(lst,elem):
    '''
    удаляет все элементы со значением elem из списка lst
    '''
    while(True):
        try:
            lst.remove(elem)
        except:
            break
            

def main():
    
    i = "input.txt"#input() #файл с указанием путей для файлов
    o = "scores.txt"#input() #файл с итоговыми значениями
    paths=[]
    

    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары названий сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    

    for s in paths:
        s1,s2="",""
        length1,length2=[],[]
        with open (s[0],"rt") as string:
            for text in string:
             s1+=' '.join(text.split(" "))
             length1.append(text)
        with open (s[1],"rt") as string:
           for text in string:
             s2+=' '.join(text.split(" "))
             length2.append(text)

        delete_element_from_list(length1,'\n')
        delete_element_from_list(length2,'\n')
        print(length1,length2)
        print(1-distance(str(s1),str(s2))/len(s1))
        
        
        
    
    
    with open (o,"w") as out:
        pass


def distance(s1, s2):
    '''
    Функция принимает 2 строки и считает
    расстояние Левенштейна между ними
    '''
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
    
    