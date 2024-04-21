from datetime import date

import os

from classes import Printer, Catalog

fileNameStorage = "dataCatalog.txt"

storage=Catalog() # все що в каталозі


def options():
    print("\n--------------ГОЛОВНЕ МЕНЮ--------------\n")
    print("1: Cпиcoк принтерів в каталозі")
    print("2: Додати новий принтер до каталогу")
    print("3: Редагувати інформацію про принтер")
    print("4: Видалення принтера за назвою")
    print("5: Пошук принтера в каталозі")
    print("6: Сортувати принтери, що є каталозі")
    print("7: Очистити вікно")
    print("8: Зберегти дані y файл")
    print("9: Завершити роботу з додатком")

def options_storage_find():
    print("\n-------ПОШУК ТОВАРІВ-------")
    print("1: Пошук за назвою принтера")
    print("2: Пошук за брендом")
    
    print("3: Очистити вікно")
    print("4: Повернутися у основне меню")


storage.read_from_file(fileNameStorage) #переносить дані з файлу в клас Catalog


os.system('cls') # очищає екран
options() # запускає функцію options, друк меню на екрані


while True:
    option = int(input("--Виберіть пункт меню: "))

    if option == 1:
        storage.print()
    

    elif option == 2:
        name=input("Введіть назву принтера: ")
        price=input("Введіть ціну принтера: ")
        while True:
            numberType=input("Введіть тип друку (1 - чорно-білий чи 2 - кольоровий): ")
            match numberType:
                case '1':
                    printing = "чорно-білий"
                    break
                case '2':
                    printing = "кольоровий"
                    break
                case _:
                    print ("Введіть 1 або 2")
        while True:
            numberTechnology=input("Введіть технологію друку (1 - лазерна, 2 - струменева): ")
            match numberTechnology:
                case '1':
                    technology = "лазерна"
                    break
                case '2':
                    technology = "струменева"
                    break
                case _:
                    print ("Введіть 1 або 2")
        weight=input("Введіть вагу принтера: ")
        brend=input("Введіть бренд: ")
        country=input("Введіть країну - виробник: ")
        storage.add( Printer(name,float(price), printing, technology, weight,brend,country) )
        print("Adding new product is success")

    elif option == 3: 
        name = input("--Введіть назву повністю: ")
        product = storage.get_printer(name)   
        if(product):
            while input("---Введіть '+' щоб продовжити редагування: ") == '+':
                key = input("Введіть назву поля: ")
                value  = input("Введіть нове значення: ")
                if(key in "pricecount"):
                    value = int(value)
                product.edit(key, value)
                print("!!! Редагування завершене успішно")
                     
                storage.save_to_file(fileNameStorage)
               
        else:
            print("!!! Товар " + name + " не знайдено")
    
    elif option==4:
        name=input("Введіть назву товару: ")
        storage.delete(name)  

   
    elif option == 5:
        os.system('cls')
        while True:
            options_storage_find()
            option = input("--Виберіть пункт меню: ")
            if option == '1': # name                
                name = input ("Введіть назву повністю або частину: ")
                storage.find('name', name)
            elif option == '2':# бренд
                text = input("Введіть бренд принтера: ")
                storage.find('brend', text)
            
            elif option == '3':
                os.system('cls')
            elif option == '4':
                os.system('cls')
                options()
                break
            else:
                print("Виберіть коректне значення")

    elif option == 6:
        n=input("Введіть поле за яким бажаєте посортувати:")
        storage.sort(n)
        storage.print()

    elif option == 7:
        os.system('cls')

    elif option==8:
        storage.save_to_file(fileNameStorage)
       
        print("Saving file is success")
    
    elif option == 9:
        break
    else:
        print("Input menu number, pls\n") 
  
         
print("ДО ЗУСТРІЧІ!")
