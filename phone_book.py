# ТЕЛЕФОННЫЙ СПРАВОЧНИК
# Создать контакт
# Изменить контакт
# Показать контакт
# Найти контакт
# Удалить контакт
# Копировать контакт
# Выход

import sys
def print_menu():
    print(f'\t ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print(f'\t\t * * *')
    print(f'\t 1. Создать контакт')
    print(f'\t 2. Изменить контакт')
    print(f'\t 3. Показать контакт')
    print(f'\t 4. Найти контакт')
    print(f'\t 5. Удалить контакт')
    print(f'\t 6. Копировать в папку')
    print(f'\t 7. Выход')
    
file_name = "./phonebook.txt"
data = open(file_name, 'a+')
data.close()
lines = {}

def create_contact(file):
    
    name = input('Введите имя: ')
    phone_num = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    with open(file_name, 'a', encoding='utf-8') as file:
	    file.write(f'{name}  {phone_num}  {comment} \n')
  
        
def change_contact(file, d):
    name_contact = input('Введите имя контакта, который вы хотите изменить: ')
    print(name_contact, end=' ')
    print(d[name_contact])
    phone = input('Введите новый номер телефона: ')
    comment = input('Введите новый комментарий: ')
    d[name_contact] = [phone, comment]
    with open(file_name, 'w', encoding='utf-8') as file:
        for k, v in d.items():
            file.write(f'{k}\t')  
            file.write(f'{"   ".join(v)}\n')  
        
def import_contact(file):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            key, *value = line.split()
            lines[key] = value
        return lines
        
def show_contact(d):
    print(f'\t ПОЛНЫЙ СПИСОК КОНТАКТОВ:')
    print(f'\t\t * * *')
    for k, v in d.items():
        print(f'{k}\t')  
        print(f'{"   ".join(v)}\n')  
    
def delete_contact(d):
    del_contact = input('Введите имя контакта, который вы хотите удалить: ')
    print(del_contact, end=' ')
    print(d[del_contact])
    del_marker = input(f'Удалить контакт {del_contact} да/нет?:')
    if del_marker == 'да':
        del d[del_contact]
        with open(file_name, 'w', encoding='utf-8') as file:
            for k, v in d.items():
                file.write(f'{k}\t')  
                file.write(f'{"   ".join(v)}\n') 
    else:
        delete_contact(d)  
        
def copy_contact(d):
    copy_contact = input('Введите имя контакта, который вы хотите скопировать: ')
    print(copy_contact, end=' ')
    print(d[copy_contact])
    file_copy = input('Введите название папки куда копировать контакт: ')
    with open(file_copy, 'a', encoding='utf-8') as file:
        file.write(f'{copy_contact}  {d[copy_contact]} \n')  
                       
        
def find_contakt(d):
    find_name = input('Введите нужное имя: ')
    print(find_name, end='   ')
    print('   '.join(d[find_name]))     
           
            
def menu_trans():
    print_menu()
    while True:
        lines = import_contact(data)
        #print(lines)
        variant = int(input('Для выбора пункта меню введите его номер: '))
        if variant == 1:
            create_contact(data)
            menu_trans()
        elif variant == 2: 
            change_contact(data,lines)
            menu_trans()
        elif variant == 3:
            show_contact(lines)
            menu_trans()    
        elif variant == 4:
            find_contakt(lines)
            menu_trans()  
        elif variant == 5:
            delete_contact(lines)
            menu_trans()  
        elif variant == 6:
            copy_contact(lines)
            menu_trans()              
        elif variant == 7:   # Не понимаю почему break иногда с певого раза работает , а то с третьего?
            break 
        else:
            menu_trans()
menu_trans()
           
           
        