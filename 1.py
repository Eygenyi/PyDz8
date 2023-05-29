path = 'phonebook.txt'
try:
    collect = {}
    d=1
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for l in file:
            l=l.replace('\n','')
            collect[d]=list(l.split(';'))
            d=d+1
    dictPhone = collect
except:
    collect = {}
    d=1
    with open('phonebook.txt', 'w+', encoding='utf-8') as file:
        for l in file:
            l=l.replace('\n','')
            collect[d]=list(l.split(';'))
            d=d+1
    dictPhone = collect
    

def findNumber(dict):
    find = str(input('Введите ваш запрос для поиска: '))
    for i in (dict):
        if find in dict[i]:
            print(i,': ',*dict[i])
def  DelPhone(dict):
    print('Сделайте выбор для удаления: ')
    f=int(input())
    del dict[f]
    for i in (dict):
        print(i,' ',*dict[i])
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for k in dictPhone:
            file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')
def addPhone():
    s=1
    save = list(input('Ввведите Ф.И и телефон через пробел: ').split())
    while True:
        if s in dictPhone:
            s=s+1
        else:
            dictPhone[s] = save
            break
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for k in dictPhone:
            file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')
def RenamePhone(dict):
    print('Сделайте выбор для изменения именм: ')
    f=int(input())
    dict[f]=list(input('Ввведите Ф.И и телефон через пробел: ').split())
    for i in (dict):
        print(i,': ',*dict[i])
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for k in dictPhone:
            file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')
def getPhone(dictP):
    for i in dictP:
        print(i,' ',*dictP[i])
def choice(n,dict):
    if n==1:
        getPhone(dict)
    if n==2:
        findNumber(dict)
    if n==3:
        addPhone()
        getPhone(dict)
    if n==4:
        getPhone(dict)
        RenamePhone(dict)
    if n==5:
        getPhone(dict)
        DelPhone(dict)


print('Здравствуйте')
print('Выберите действие с телефонным справочником от 1 до 6 и нажмите Enter:')
print('1 - Показать справочник, 2 - Произвести поиск по запросу, 3 - Добавить запись ,4-изменение записи,5- удаление записи,6-выход')
while True:
    n=int(input())
    if 1<=n & n<=5:
        choice(n, dictPhone)
        print('1 - Показать справочник, 2 - Поиск по запросу, 3 - Добавить запись, 4-изменение записи,5- удаление записи, 6-выход')
    else:
        break    
