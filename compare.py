import os
import numpy as np

class File():


    '''
    Класс File
    '''
            
    def __init__(self,path) -> None:
        '''
        path - пути до 2 файлов
        передается кортежем или списком
        '''
        
        self.__path=path
        if self.__path[len(self.__path)-1:len(self.__path)]=='\n': 
            self.__path=self.__path[:-1]
        self.__file=[]
        with open (self.__path ,"rt") as text:
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
def Levenstein(func):
    '''
    декоратор для функции, вычисляющей расстояние Левенштейна.
    Дает возможность посчитать расстояние между многострочными текстами
    '''
    def wrapper(lst1,lst2):
        result=0
        if len(lst1)!=len(lst2):
            min_str=lst2 if len(lst1)>len(lst2) else lst1
            max_str=lst2 if len(lst1)<len(lst2) else lst1
            for i in range(0,max(len(lst1), len(lst2))-min(len(lst1),len(lst2))): 
                min_str.insert(i,max_str[i])  #добавили строчки, чтобы длина массивов была равна
                    
        for i in range(len(lst1)):
            distance=func(lst1[i],lst2[i]) #построчно сравниваем массивы
            result+=1-distance/max(len(lst1[i]),len(lst2[i]))
        
        return round(result/len(lst1),3) # получаем число <=1
            
    return wrapper

@Levenstein
def dist(s1, s2):      
    '''
    Функция принимает массива строк и считает
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
    
    i = input() #файл с указанием путей для файлов
    o = input() #файл с итоговыми значениями
    
    paths = [] # массив с указанием путей к файлам
    texts = [] # сравниваемые файлы

    with open (i,'rt') as p: #считываем входной файл, в paths записываем кортежные пары названий сравниваемых файлов
        paths=[tuple(text_file.split(" ")) for text_file in p]
    
    for file in paths:
        arr = (File(file[0]),File(file[1])) 
        texts.append(arr)

    
    result=list(dist(arr[0].file,arr[1].file) for arr in texts)
       
    
    
    with open (o,"w") as out:
        for res in result:
            out.write(str(res)+'\n')



    

if __name__ == "__main__":
    main()
    