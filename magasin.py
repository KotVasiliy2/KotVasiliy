количество_денег=500
стоимость=0
корзина=""
a=None
while a!=0:
    a=int(input("выберите категорию товара 1 чипсеки 2 лимонадек 3 сухареки 0 уйти"))
    if a==1:
        b=int(input("выберите товар 1 Читос 25руб 2 Лейс 30руб 3 Доритос 80руб"))
        if b==1:
            стоимость+=25
            корзина+="читос "
            print("вы взяли Читос")
        if b==2:
            стоимость+=30
            корзина+="лейс "
            print("вы взяли Лейс")
        if b==3:
            стоимость+=80
            корзина+="доритос "
            print("вы взяли Доритос")
    if a==2:
        c=int(input("выберите товар 1 кока-лока 32руб 2 Спрайт 40руб 3 Фанта 28руб"))
        if c==1:
            стоимость+=32
            корзина+="кока-лока "
            print("вы взяли коку-локу")
        if c==2:
            стоимость+=40
            корзина+="Спрайт "
            print("вы взяли Спрайт")
        if c==3:
            стоимость+=28
            корзина+="Фанта "
            print("вы взяли Фанту")
    if a==3:
        d=int(input("выберите товар 1 Кириешки 8руб 2 Хрус Team 14руб 3 3 корочки 18руб"))
        if d==1:
            стоимость+=8
            корзина+="кириешки "
            print("вы взяли Кириешки")
        if d==2:
            стоимость+=14
            корзина+="хрус team "
            print("вы взяли Хрус Team")
        if d==3:
            стоимость+=18
            корзина+="3 корочки "
            print("вы взяли 3 корочки")
if a==0:
    if стоимость<количество_денег:
        print("остаток", количество_денег-стоимость)
    else:
        print("недостаточно денег!")
    print(корзина)