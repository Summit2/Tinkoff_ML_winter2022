import os
import numpy as np

class File():


    '''
    Класс File

    Содержит метод Levenstein для сравения похожести 2 строк

    '''
    
        
        
    def __init__(self,path) -> None:
        '''
        path - пути до 2 файлов
        передается кортежем или списком
        '''
        self.__path=path
        self.__file=[]
        with open (path ,"rt") as text:
            string = ''
            for t in text:
                self.__file.append(t)  
        delete_element_from_list(self.__file,'\n') # удаляем лишние переносы строк
    @property 
    def file(self):
        return self.__file
    
    @property
    def path(self):
        return self.__path
    


def delete_element_from_list(lst,elem):
    '''
    удаляет все элементы со значением elem из списка lst
    '''
    while(True):
        try:
            lst.remove(elem)
        except:
            break

def Levenstein(s1, s2):      
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
    
    paths = [] # массив с указанием путей к файлам
    texts = [] # сравниваемые файлы

    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары названий сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    
    for file in paths:
        arr = (File(file[0]),File(file[1])) 
        #print(arr[0].get_file)
    texts.append(arr)

    
    result=list( (len(arr[0].file[0]),len(arr[0].file[1])) for arr in texts)
    print(result)
        
        
    
    
    with open (o,"w") as out:
        for res in result:
            out.write(res)



    

if __name__ == "__main__":
    main()
    
    