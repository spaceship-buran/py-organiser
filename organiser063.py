#-------------------------------------------------------------------------------
# Name:        Органайзер 0.6.3
# Purpose:     Консольная программа для создания, чтения и сохранения файлов,
#              а также для простейших вычислений
#
# Author:      Ермаков С.В.
#
# Created:     12.04.2021
# Licence:     GNU General Public License, v3
#-------------------------------------------------------------------------------
print('Органайзер, версия 0.6.3')
from datetime import*
import math
import os
print(datetime.date(datetime.now()))         #Выводим текущую дату
print(datetime.time(datetime.now()))         #и время
print('Author: Ермаков С.В.')

def end():                                   #Создаём инструкцию для закрытия
    end = input('Press "ENTER" to continue... ')
    print()
menu_exit = 0

while menu_exit == 0:
    print('Главное меню:')                       #Выводим список доступных программ
    print('1-Телефонная книга')
    print('2-Текстовый редактор')
    print('3-Калькулятор')
    print('4-Архиватор')
    print('5-Файлы')
    print('6-Справка')
    print('0-Выход')
    change = int(input('Выберите номер команды: '))

    if change == 1:
        print('Телефонная книга,ver.0.5')        #Если выбор = 1, то запускаем
        vib = int(input('1-Запись 2-Чтение: '))  #программу для создания тел. книг
        if vib == 1:
            colvo = int(input('Введите количество номеров: '))
            path = input('Введите путь к файлу [D:\example.txt or D:\example.pnb]: ')
            name = '%18s'%"Имя"                  #Вызываем переменную с отформа-
            num = '%18s'%"Номер"                 #тированным текстом и
            f = open(path,'w')                   #записываем их в файл, указанный
            f.write(name)                        #пользователем. Перем. явл. загл.
            f.write(num + '\n')
            for n in range(1,colvo+1):
                nm = input('Имя: ')              #Спрашиваем у пользователя имя и
                number = input('Номер: ')        #номер абонента, а затем записываем
                nm = '%18s'% nm                  #их в файл, но перед этим форматиру-
                number = '%18s'% number          #ем. Операция повт. заданное ч. раз
                f.write(nm)
                f.write(number + '\n')
            f.close()
            end()
        elif vib == 2:
            path = input('Введите путь к файлу [D:\example.txt or D:\example.pnb]: ')
            f = open(path,'r')                   #Спрашиваем у пользователя,
            text = f.read()                      #по какому пути расп. файл, запоми-
            print(text)                          #наем содерж. в пер. и выв. на экр.
            f.close()
            end()

    elif change == 2:
        print('Текстовый редактор 0.3.3')
        vib = int(input('1-Запись 2-Чтение: '))  #Если выбор пользователя = 2 выз.
        if vib == 1:                             #прог. Текст. ред. Польз. выб. З. или Ч.
            path = input('Введите путь к файлу [D:\example.txt]: ')
            f = open(path,'w')                   #Создаем файл по задан. пути
            text = '0'
            print('Введите "[end]", чтобы закончить')
            while text != '[end]':               #Выполн. цикл, пока польз. не введ. [end]
                text = input()
                if text == '[end]':
                    print('Файл завершён и сохранён успешно!')
                else:
                    f.write(text + '\n')         #Записываем строку и переходим на новую
            f.close()
            end()
        elif vib == 2:                           #Если выбор неверный, то заверш. прог.
            n = 1
            while n > 0:
                x = os.listdir()                 #Выполн., пока польз. не откр. файл,
                print('-----------------------') #а затем считываем содерж. каталога
                print('Файлы в текущей папке: ')
                print('-----------------------')
                for z in x:                      #Печатаем содерж. каталога
                    print(z)
                command = int(input('Открыть: 1-файл, 2-папку? '))
                if command == 1:                 #Пользователь выбир. откр. файл
                    path = input('Введите имя файла [example.txt]: ')
                    try:                         #Если файл поддерживается, открываем
                        f = open(path,'r')
                        txt = f.read()
                        print(txt)
                        f.close()
                        end()
                        n = 0
                    except:                      #Если нет...
                        print('Ошибка! Неподдерживаемый формат файла или кодировка!')
                elif command == 2:               #Пользователь выбирает каталог для открытия
                    chd = input('chdir=')
                    os.chdir(chd)
                else:
                    print('Uncorrect data! Try again!')

    elif change == 3:
        print('Калькулятор, версия 0.1')         #Заглавие. Это простой калькулятор
        numcalc = 1                              #Создаем переменную для цикла
        while numcalc > 0:
            print('For exit input "exit"')
            a = input('Выражение(e.g. 2*2 или введите sqrt чтобы найти кв.корень): ')
            if a == 'sqrt':                      #Подпрограмма нахождения корня
                sq = float(input('sq='))
                print(math.sqrt(sq))
                end()
            elif a == '':                        #Защита от случайного пустого ввода
                print('Введите выражение!')
            elif a == 'exit':                    #Стандартный выход
                numcalc = 0
                end()
            else:
                try:
                    print(a + ' =',eval(a))      #Вычисление начинается
                    end()
                except ZeroDivisionError:        #Если есть деление на 0 выводим ошибку
                    print('Ошибка! На нуль делить нельзя!')
                    end()

    elif change == 4:
        print('Easy_Zip,ver. 0.1.1')             #Простой архиватор
        import zipfile
        vibor = int(input('1-Запись, 2-Чтение: '))
        i = 1                                    #Переменная-регулировщик цикла
        if vibor == 1:
            while i > 0:                         #Начинаем работу с архивами
                ch = input('Введите "end",чтобы закончить работу с архивами...')
                if ch == 'end':
                    i = 0
                else:
                    file = input('Введите путь к создаваемому архиву: ')
                    ezip = zipfile.ZipFile(file,'w')
                    zwr = input('Введите файл, который надо запаковать: ')
                    ezip.write(zwr)              #Начинаем цикл, записываем и
                    ezip.close()                 #закрываем архив
            end()
        elif vibor == 2:                         #Чтение архива
            n = 1                                #Переменная-регулировщик цикла
            while n > 0:                         #Начинаем цикл
                x = os.listdir()                 #Читаем содерж.каталога
                print('-----------------------')
                print('Файлы в текущей папке: ')
                print('-----------------------')
                for z in x:                      #и выводим на экран построчно
                    print(z)
                command = int(input('Открыть: 1-файл, 2-папку? '))
                if command == 1:                 #Открываем архив
                    try:
                        path = input('Введите имя архива [example.zip]: ')
                        rd = zipfile.ZipFile(path,'r')
                        rd.printdir()                #и выводим содержимое на экран
                        i = int(input('Распаковать: 1-1 файл, 2-весь архив: '))
                        if i == 1:                   #Распаковываем по одному
                            ex = '0'
                            while ex != 'end':
                                f = int(input('Закончить работу? 1-да др.число-нет: '))
                                if f == 1:           #Выходим из цикла
                                    ex = 'end'
                                else:
                                    p = input('Введите название файла содержимого архива: ')
                                    rd.extract(p)    #Распаковываем
                                    rd.close()
                                end()
                            n = 0
                        elif i == 2:
                            rd.extractall()          #Распаковываем весь
                            rd.close()
                            end()
                            n = 0
                        else:
                           end()
                           n = 0
                    except zipfile.BadZipFile:
                        print('Ошибка!',path,'не является архивом!')
                elif command == 2:               #Выбираем папку
                    chd = input('chdir=')
                    os.chdir(chd)
                else:
                    print('Uncorrect data! Try again!')
        else:
            end()
    elif change == 5:
        print('Files v0.1')
        files_exit = 0
        while files_exit == 0:
            x = os.listdir()                 #Читаем содерж.каталога
            print('-----------------------')
            print('Файлы в текущей папке: ')
            print('-----------------------')
            for z in x:                      #и выводим на экран построчно
                print(z)
            files_vib = int(input('Введите номер команды (Справка-0): '))
            try:
                if files_vib == 0:                # Предлагаем пользователю
                    print('0-Справка')          #Выбрать файловую
                    print('1-Удалить каталог')  #операцию
                    print('2-Удалить')
                    print('3-Выбрать каталог')
                    print('4-Вывести содерж. файла')
                    print('5-Выполнить программу')
                    print('6-Выход')
                    end()
                elif files_vib == 1:
                    try:
                        kerase = input('Имя удаляемого каталога: ') #Уд. каталог
                        os.rmdir(kerase)
                        end()
                    except:
                        print('Непредвиденная ошибка!')
                        end()
                elif files_vib == 2:
                    try:
                        remove_f = input('Файл для удаления: ') #Уд. файл
                        os.remove(remove_f)
                        end()
                    except:
                        print('Непредвиденная ошибка!')
                        end()
                elif files_vib == 3:
                    try:
                        chd = input('chdir=') #Польз. выб. каталог
                        os.chdir(chd)
                        end()
                    except:
                        print('Невозможно отрыть каталог!')
                        end()
                elif files_vib == 4:
                    try:
                        filetype = input('Имя файла: ') #Аналог type (DOS)
                        ftpr = open(filetype, 'r')
                        rdft = ftpr.read()
                        print(rdft)
                        ftpr.close()
                        end()
                    except:
                        print('Ошибка, не могу открыть файл!')
                        end()
                elif files_vib == 5: #Выполнение программы WIN С аргументами или без
                    exe = input('Введите путь к программе и аргументы, если нужно: ')
                    try:
                        print(os.system(exe))
                        print('Программа выполнена')
                        end()
                    except:
                        print('Ошибка, программа не выполнена')
                        end()
                elif files_vib == 6:
                    end()
                    files_exit = 1
            except: #Выполн., если польз. ввёл неверный номер команды
                print('Неверные введённые данные! Для справки введите "0"')
                end()

    elif change == 6: #Справка по командам
        print('Справка')
        try:
            f = open('help.txt', 'r')
            hr = f.read()
            print(hr)
            f.close()
            end()
        except:
            print('Файл справки повреждён или не найден!')
            end()
    elif change == 0:
        menu_exit = 1
        end()

