#-------------------------------------------------------------------------------
# Name:        Organiser, version 0.6.3
# Purpose:     Console program for working with files and typical maths
# Author:      Yermakov S.V. aka spaceship-buran
# Created:     12.04.2021
# Licence:     GNU General Public License
# Site:        https://github.com/spaceship-buran/py-organiser
#-------------------------------------------------------------------------------
print('Organiser, version 0.6.3')
from datetime import*
import math
import os
print(datetime.date(datetime.now()))         #Date
print(datetime.time(datetime.now()))         #and time now
print('Author: Yermakov S.V.')

def end():                                   #Closing procedure
    end = input('Press "ENTER" to continue... ')
    print()
menu_exit = 0

while menu_exit == 0:
    print('Main menu:')                       #Choose of subprograms
    print('1-Phonebook')
    print('2-Simply text editor')
    print('3-Calculator')
    print('4-Zip utility')
    print('5-File manager')
    print('6-Info')
    print('0-Exit')
    change = int(input('Your choose: '))

    if change == 1:
        print('Phonenumber,ver.0.5')        #If choosing - 1
        vib = int(input('1-Edit 2-Read: '))  #run phonenumber subprogram
        if vib == 1:
            colvo = int(input('How many numbers: '))
            path = input('Path to file [D:\example.txt or D:\example.pnb]: ')
            name = '%18s'%"Name"                  #Call variable with formatted
            num = '%18s'%"Number"                 #text and write into the file,
            f = open(path,'w')                   #choosen by user.
            f.write(name)                        #Var is the title.
            f.write(num + '\n')
            for n in range(1,colvo+1):
                nm = input('Name: ')              #Waiting for user's data and
                number = input('Number: ')        #writing it into the file,
                nm = '%18s'% nm                  #but format it before.
                number = '%18s'% number          #Do the operation set value of
                f.write(nm)                     #repeats
                f.write(number + '\n')
            f.close()
            end()
        elif vib == 2:
            path = input('Path to file [D:\example.txt or D:\example.pnb]: ')
            f = open(path,'r')                   #Read user's path and print
            text = f.read()                      #content to the monitor
            f.close()
            end()

    elif change == 2:
        print('Text editor 0.3.3')
        vib = int(input('1-Edit 2-Read: '))  #If user chooses 2, then editor
        if vib == 1:                             #runs for editing or reading
            path = input('Path to file [D:\example.txt]: ')
            f = open(path,'w')                   #Edit file at path
            text = '0'
            print('Type "[end]" for end editing')
            while text != '[end]':               #Editing while typing [end]
                text = input()
                if text == '[end]':
                    print('File edited and sucessfully saved!')
                else:
                    f.write(text + '\n')         #Write a string and go to a new
            f.close()                            #one
            end()
        elif vib == 2:                           #End programme, when uncorrect
            n = 1                                #data inputted
            while n > 0:
                x = os.listdir()                 #Reading dir while user open
                print('-----------------------') #another dir or file
                print('This directory listing:')
                print('-----------------------')
                for z in x:                      #Typing the dir list
                    print(z)
                command = int(input('Open: 1-file, 2-dir? '))
                if command == 1:                 #Choosing of file
                    path = input('Input file name [example.txt]: ')
                    try:                         #If format readable
                        f = open(path,'r')
                        txt = f.read()
                        print(txt)
                        f.close()
                        end()
                        n = 0
                    except:                      #If not...
                        print('Error! Unsupported format or encoding!')
                elif command == 2:               #User chooses new dir
                    chd = input('chdir=')
                    os.chdir(chd)
                else:
                    print('Uncorrect data! Try again!')

    elif change == 3:
        print('Calculator, v0.1')         #Subprogram "Calculator, v0.1
        numcalc = 1                              #Cycle's variable
        while numcalc > 0:
            print('For exit input "exit"')
            a = input('Sum(e.g. 2*2 or input sqrt for sqrt eval): ')
            if a == 'sqrt':                      #sqrt subprogram
                sq = float(input('sq='))
                print(math.sqrt(sq))
                end()
            elif a == '':                        #Empty input shield
                print('Введите выражение!')
            elif a == 'exit':                    #Normal exit
                numcalc = 0
                end()
            else:
                try:
                    print(a + ' =',eval(a))      #Calculating...
                    end()
                except ZeroDivisionError:        #If a/0 type error mes
                    print('Error while division on zero!')
                    end()

    elif change == 4:
        print('Easy_Zip,ver. 0.1.1')             #Simple archiver
        import zipfile
        vibor = int(input('1-Edit, 2-Read: '))
        i = 1                                    #Entering to the cycle
        if vibor == 1:
            while i > 0:                         #Begin work with .zip
                ch = input('Input "end" for exit...')
                if ch == 'end':
                    i = 0
                else:
                    file = input('Path to editing archive: ')
                    ezip = zipfile.ZipFile(file,'w')
                    zwr = input('Packing file: ')
                    ezip.write(zwr)              #Begin cycle and write ZIP
                    ezip.close()                 #and close file
            end()
        elif vibor == 2:                         #Reading ZIP
            n = 1                                #Begin cycle
            while n > 0:                         #and reading
                x = os.listdir()                 #dir listing
                print('-----------------------')
                print('This directory listing:')
                print('-----------------------')
                for z in x:                      #string typing
                    print(z)
                command = int(input('Open: 1-file, 2-dir? '))
                if command == 1:                 #Opening ZIP
                    try:
                        path = input('Name of ZIP [example.zip]: ')
                        rd = zipfile.ZipFile(path,'r')
                        rd.printdir()                #typing Zip content
                        i = int(input('Unpack: 1-1 archived file, 2-all ZIP: '))
                        if i == 1:                   #Распаковываем по одному
                            ex = '0'
                            while ex != 'end':
                                f = int(input('Stop working? 1-yes another-no: '))
                                if f == 1:           #Exiting...
                                    ex = 'end'
                                else:
                                    p = input('Existing file name to unzip: ')
                                    rd.extract(p)    #Unpacking chosen
                                    rd.close()
                                end()
                            n = 0
                        elif i == 2:
                            rd.extractall()          #Extract all zipfile
                            rd.close()
                            end()
                            n = 0
                        else:
                           end()
                           n = 0
                    except zipfile.BadZipFile:
                        print('ERROR!',path,'is not archive!')
                elif command == 2:               #Change working dir
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
            x = os.listdir()                 #Reading dir listing
            print('-----------------------')
            print('This directory listing:')
            print('-----------------------')
            for z in x:                      #and typing strings
                print(z)
            files_vib = int(input('Command number (Info-0): '))
            try:
                if files_vib == 0:                # User's choose
                    print('0-Info')          #Choose of file
                    print('1-Remove dir')  #operation
                    print('2-Erase')
                    print('3-Change dir')
                    print('4-Type file')
                    print('5-Run .EXE')
                    print('6-Exit')
                    end()
                elif files_vib == 1:
                    try:
                        kerase = input('Removing dir: ') #RemDir
                        os.rmdir(kerase)
                        end()
                    except:
                        print('Error!')
                        end()
                elif files_vib == 2:
                    try:
                        remove_f = input('Erasing file: ') #ErFile
                        os.remove(remove_f)
                        end()
                    except:
                        print('Error!')
                        end()
                elif files_vib == 3:
                    try:
                        chd = input('chdir=') #User Change dir
                        os.chdir(chd)
                        end()
                    except:
                        print('Cannot open dir!')
                        end()
                elif files_vib == 4:
                    try:
                        filetype = input('Filename: ') #type (DOS)
                        ftpr = open(filetype, 'r')
                        rdft = ftpr.read()
                        print(rdft)
                        ftpr.close()
                        end()
                    except:
                        print('Cannot open file!')
                        end()
                elif files_vib == 5: #Exec WIN program with argues or without
                    exe = input('Path to program + args: ')
                    try:
                        print(os.system(exe))
                        print('Program executed')
                        end()
                    except:
                        print('Error, program did not executed!')
                        end()
                elif files_vib == 6:
                    end()
                    files_exit = 1
            except: #Unsupported command input
                print('Uncorrect data! Input "0" for help')
                end()

    elif change == 6: #Program info
        print('Info')
        try:
            f = open('help_en.txt', 'r')
            hr = f.read()
            print(hr)
            f.close()
            end()
        except:
            print('Error while info file reading!')
            end()
    elif change == 0:
        menu_exit = 1
        end()

