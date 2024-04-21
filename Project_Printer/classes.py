from tokenize import String
from datetime import datetime

# опис характеристик принтерів
class Printer():
    def __init__ (self, name, price, printing, technology,weight,brend,country):
        self.__name:str = name # робиться внутрішня змінна, її область видимості тільки цей клас. змінна захищається від несанкціонованих змін
        self.__price = price
        self.__printing = printing
        self.__technology=technology
        self.__weight = weight
        self.__brend = brend
        self.__country = country


    # get метод щоб отримати значення полів класу Printers
    def get(self,key):
        if (key=="name"):
            value=self.__name
        elif (key=="price"):
            value=self.__price
        elif (key=="printing"):
            value=self.__printing
        elif (key=="technology"):
            value=self.__technology
        elif (key == "weight"):
            value=self.__weight
        elif (key == "brend"):
            value=self.__brend
        elif (key == "country"):
            value=self.__country    
        else:
            print("задано не існуюче поле")
        return value
    

    # функція що редагує окреме поле рядка з іменем key
    def edit(self, key, value):
        if (key == "name"):
            self.__name = value
        if (key == "price"):
            self.__price = value
        if (key == "printing"):
            self.__printing = value
        if (key == "technology"):
            self.__technology = value
        if (key == "weight"):
            self.__weight = value
        if (key == "brend"):
            self.__brend = value
        if (key == "country"):
            self.__country = value


    # друк одного рядка
    def print(self):
        print ("{0:20} | {1:8} | {2:15} | {3:15} | {4:6} | {5:10} | {6}".format(
                self.__name, 
                self.__price, 
                self.__printing,
                self.__technology,
                self.__weight,
                self.__brend,
                self.__country
            )
        )
    def join(self):
        return(','.join([
                self.__name, 
                str(self.__price), 
                self.__printing, 
                self.__technology,
                str(self.__weight),
                self.__brend,
                self.__country
            ])
        )


    def set(self, text_row:String):
        try:
            list = text_row.split(',')
            self.__name = list[0]
            self.__price = float(list[1])
            self.__printing = list[2]
            self.__technology = list[3]
            #self.__rent = int(list[3])
            self.__weight = float(list[4])
            self.__brend = list[5]
            self.__country = list[6]
            print("Convert is successfull")
            return self
        except:
            print("String isn't converted")


class Catalog():
    # в цьому класі зберігається масив обєктів класу Printers  і методи для роботи з цим масивом
    def __init__(self): 
        self.__printers = []


    # додавання нового товару
    def add (self, printer):
        self.__printers.append(printer)


    # шукає товар по назві на складі
    def get(self, name):
        for printer in self.__printers:
            if (printer.get("name") == name):
                return printer
            

    # шукає по імені і видаляє з списку цілий рядок
    def delete(self, name):
        success = False # змінна успішне завершення
        for i in range(len(self.__printers)):
            if (self.__printers[i].get("name") == name): # шукає поле з іменем name
                self.__printers.remove(self.__printers[i])
                success = True
                break
        return False
    

    # друкує всі принтери з каталогу
    def print(self): 
        self.__print_head() # print head
        for printer in self.__printers:
            printer.print()
        print("-"*100)


    def read_from_file(self, fileName):
        print("Storage start read")
        if (len(self.__printers) > 0):
            print("Storage set is full")
            return
        file_reader = open (fileName, mode = 'r', encoding='utf-8')
        data_list = file_reader.read().strip().split('\n')
        for row in data_list:
            printer = Printer('',0,'','',0,'','')
            self.__printers.append(printer.set(row))
        file_reader.close()


    def save_to_file(self, fileName):
        file_writer = open (fileName, mode = 'w', encoding='utf-8')
        for printer in self.__printers:
            
            file_writer.write(printer.join() + '\n')
        file_writer.close()
    

    def find (self, key, value): 
        self.__print_head()
        for printer in self.__printers:
            if(value in printer.get(key)):
                printer.print()        
        print("-"*100) 


    def get_printer(self, value): 
        for printer in self.__printers:
            if(value == printer.get("name")):
                return printer
            

              

    def __print_head(self): #  print head
        print("-"*100)
        print("{0:20} | {1:8} | {2:15} | {3:15} | {4:6} | {5:10} | {6}".format(
                "printer's name",
                "price",
                "printing",
                "technology",
                "weight",
                "brend",
                "country"
            )
        )        
        print("-"*100) 

    def sort(self,key,value):
        self.__printers.sort()

    def sort(self, m):
        self.__printers.sort(key = lambda x: x.get(m))
                

