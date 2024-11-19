import csv
import os
bp=str(os.path.abspath(os.getcwd()))+"/car_base.csv"
# №,марка,модель,год,цвет,дтп,пробег,инфо
def new():
    os.system("clear")
    out_list=[]
    temp=[]
    while True:
        ans=str(input("Ввести новую строку? (y/n):"))
        if ans=="y":
            while True:
                num=str(input("Номер:"))
                if len(num)<7 or len(num)>9:
                    print("Неверный номер!")
                    continue
                else:
                    out_list.append(num)
                mark=str(input("Марка:"))
                if len(mark)<2 or len(mark)>20:
                    print("Неверная марка!")
                    continue
                else:
                    out_list.append(mark)
                model=str(input("Модель:"))
                if len(model)<2 or len(model)>20:
                    print("Неверная модель!")
                    continue
                else:
                    out_list.append(model)
                year=str(input("Год:"))
                if len(year)<2!=4:
                    print("Неверный год!")
                    continue
                else:
                    out_list.append(year)
                color=str(input("Цвет:"))
                if len(color)<2 or len(color)>20:
                    print("Неверный цвет!")
                    continue
                else:
                    out_list.append(color)
                ra=str(input("ДТП(y/n):"))
                if ra=="y":
                    out_list.append(ra)
                elif ra=="n":
                    out_list.append(ra)
                else:
                    print("Неверный параметр!")
                    continue
                dis=str(input("Пробег:"))
                if len(dis)<0:
                    print("Неверный пробег!")
                    continue
                else:
                    out_list.append(dis)
                info=str(input("Инфо:"))
                out_list.append(info)
                break
            try:
                with open(bp, 'r') as file:
                    reader=csv.reader(file)
                    for x in reader:
                        temp.append(x)
                temp.append(out_list)
                with open(bp, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(temp)
                print("База перезаписана и сохранена успешно!")
                print("")
                return new()
            except:
                print("Ошибка в ходе перезаписи базы!")
                print("")
                return 0
        elif ans=="n":
            break
        else:
            print("Неверная команда!")
            print("")

def shw():
    os.system("clear")
    cnt=1
    print("№| Номер | Марка | Модель | Год | Цвет | ДТП | Пробег | Инфо |")
    with open(bp,'r') as file:
        reader=csv.reader(file)
        for x in reader:
            print(str(cnt)+" ",end='');print(*x)
    return

def count():
    os.system("clear")
    cnt=0
    with open(bp, "r") as file:
        reader=csv.reader(file)
        for x in reader:
            cnt+=1
        print("Количество авто на парковке: "+str(cnt))
    return

def srh():
    while True:
        temp=[]
        os.system("clear")
        cnt = 1
        print("№| Номер | Марка | Модель | Год | Цвет | ДТП | Пробег | Инфо |")
        with open(bp, 'r') as file:
            reader = csv.reader(file)
            for x in reader:
                temp.append(x)
                print(str(cnt) + " ", end='')
                print(*x)
                cnt += 1
        pos=[]
        ans = str(input("Введите ключевое слово ('back'): "))
        if ans == "back":
            return 0
        else:
            os.system("clear")
            cnt4=1
            cnt3=0
            print("№| Номер | Марка | Модель | Год | Цвет | ДТП | Пробег | Инфо |")
            for x in temp:
                for y in range(len(x)):
                    if ans==str(x[y]):
                        print(str(cnt4) + " ", end='')
                        print(*x)
                        cnt4+=1
                        pos.append(cnt3)
                cnt3+=1
        cmnd = str(input("Функция (mod,del,back): "))
        if cmnd == "mod":
            ans4 = str(input("Введите номер пункта ('back'): "))
            if ans4 == "back":
                return srh()
            elif ans4.isnumeric():
                ans4 = int(ans4)
                if 0 < ans4 < len(temp)+1:
                    cnt2 = 1
                    mod = temp[ans4-1]
                    print("Детали пункта:")
                    for x in mod:
                        print(str(cnt2) + " " + str(x))
                        cnt2 += 1
                    ans2 = str(input("Введите номер пункта ('back'): "))
                    if ans2 == "back":
                        continue
                    elif ans2.isnumeric():
                        ans2 = int(ans2)
                        if 0 < ans2 < cnt2:
                            ans3 = str(input("Введите параметр: "))
                            mod[ans2 - 1] = ans3
                            temp[pos[0]]=mod
                            try:
                                with open(bp, 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(temp)
                                print("База перезаписана и сохранена успешно!")
                                print("")
                                continue
                            except:
                                print("Ошибка в ходе перезаписи базы!")
                                print("")
                                return 0
                        else:
                            print("Неверный номер пункта!")
                            print("")
                    else:
                        print("Неверный номер пункта!")
                        print("")
                else:
                    print("Неверный номер пункта!")
                    print("")
            else:
                print("Неверный номер пункта!")
                print("")
        elif cmnd == "del":
            ans5 = str(input("Введите номер пункта ('back'): "))
            if ans5 == "back":
                return srh()
            elif ans5.isnumeric():
                ans5=int(ans5)
                print(ans5)
                print(len(temp))
                if 0 < ans5 < len(pos)+1:
                    temp.pop(pos[ans5-1])
                    pos.pop(ans5-1)
                    try:
                        with open(bp, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(temp)
                        print("База перезаписана и сохранена успешно!")
                        print("")
                        continue
                    except:
                        print("Ошибка в ходе перезаписи базы!")
                        print("")
                        return 0
            else:
                print("Неверный номер пункта!")
                print("")
        elif cmnd == "back":
            return srh()
        else:
            os.system("clear")
            return 0

def mod():
    os.system("clear")
    while True:
        temp = []
        cnt = 1
        print("№| Номер | Марка | Модель | Год | Цвет | ДТП | Пробег | Инфо |")
        with open(bp, 'r') as file:
            reader = csv.reader(file)
            for x in reader:
                temp.append(x)
                print(str(cnt) + " ", end='');print(*x)
                cnt += 1
        ans = str(input("Введите номер пункта ('back'): "))
        if ans=="back":
            return 0
        elif ans.isnumeric():
            ans=int(ans)
            if 0 < ans < cnt:
                cnt2=1
                mod=temp[ans-1]
                print("Детали пункта:")
                for x in mod:
                    print(str(cnt2)+" "+str(x))
                    cnt2+=1
                ans2 = str(input("Введите номер пункта ('back'): "))
                if ans2 == "back":
                    continue
                elif ans2.isnumeric():
                    ans2 = int(ans2)
                    if 0 < ans2 < cnt2:
                        ans3=str(input("Введите параметр: "))
                        mod[ans2-1]=ans3
                        temp[cnt-2]=mod
                        try:
                            with open(bp, 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(temp)
                            print("База перезаписана и сохранена успешно!")
                            print("")
                            continue
                        except:
                            print("Ошибка в ходе перезаписи базы!")
                            print("")
                            return 0
                    else:
                        print("Неверный номер пункта!")
                        print("")
                else:
                    print("Неверный номер пункта!")
                    print("")
            else:
                print("Неверный номер пункта!")
                print("")
        else:
            print("Неверный номер пункта!")
            print("")

def dell():
    os.system("clear")
    while True:
        temp=[]
        cnt=1
        print("№| Номер | Марка | Модель | Год | Цвет | ДТП | Пробег | Инфо |")
        with open(bp, 'r') as file:
            reader = csv.reader(file)
            for x in reader:
                temp.append(x)
                print(str(cnt)+" ", end='');print(*x)
                cnt+=1
        ans=str(input("Введите номер пункта ('back'): "))
        if ans=="back":
            return 0
        elif ans.isnumeric():
            ans=int(ans)
            if 0<ans<cnt:
                temp.pop(ans-1)
                try:
                    with open(bp, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(temp)
                    print("База перезаписана и сохранена успешно!")
                    return dell()
                except:
                    print("Ошибка в ходе перезаписи базы!")
                    print("")
                    return dell()
            else:
                print("Неверный номер пункта!")
                print("")
        else:
            print("Неверный номер пункта!")
            print("")

def main():
    if os.path.exists(bp)==False:
        with open(bp, 'x') as fp:
            pass
    os.system("clear")
    cnt = 0
    with open(bp, 'r') as file:
        reader=csv.reader(file)
        for x in reader:
            cnt+=1
    if cnt==0:
        print("В базе нет элементов!")
    else:
        print("В базе "+str(cnt)+" элементов.")
    while True:
        print("")
        cmnd=str(input("Функция (new,srh,cnt,shw,mod,del,ext): "))
        if cmnd=="new":
            new()
            os.system("clear")
        elif cmnd=="srh":
            srh()
        elif cmnd=="cnt":
            count()
        elif cmnd=="shw":
            shw()
        elif cmnd=="mod":
            mod()
            os.system("clear")
        elif cmnd=="del":
            dell()
            os.system("clear")
        elif cmnd=="ext":
            os.system("clear")
            return 0
        else:
            print("Неверная команда!")
main()
