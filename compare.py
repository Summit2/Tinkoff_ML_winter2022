import os
import numpy as np

class File():


    '''
    Класс File

    Содержит метод Levenstien для сравения похожести 2 строк

    '''
    
        
        
    def __init__(self,path) -> None:
        '''
        path - пути до 2 файлов
        передается кортежем или списком
        '''
        with open (path[0] ,"rt") as text:
            self.__file1=text
        with open (path[1] ,"rt") as text:
            self.__file2=text
    @classmethod #чтобы была возможность вызывать метод, не создавая объект класса
    def Levenstein(self,file1, file2):
        print("lev")
    


def delete_element_from_list(lst,elem):
    '''
    удаляет все элементы со значением elem из списка lst
    '''
    while(True):
        try:
            lst.remove(elem)
        except:
            break

    
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

def main():
    
    i = "input.txt"#input() #файл с указанием путей для файлов
    o = "scores.txt"#input() #файл с итоговыми значениями
    
    result=[]
    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары названий сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    
    for file in paths:
        answer = File(file)
        result.append(answer)

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
        print(length1,length2,sep='\n')
        
        
        
        
    
    
    with open (o,"w") as out:
        pass



    

if __name__ == "__main__":
    #main()
    File.Levenstein(1,1)
    