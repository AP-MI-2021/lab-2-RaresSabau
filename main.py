#Problemele 2,3,13

from datetime import datetime, date


'''
Problema 2
'''
def get_age_in_days(datan: str):
    '''
    Functia returneaza varsta persoanei in zile
    :param datan:parametru prin care se calculeaza data nasterii din str in .date()
    :return:
    '''

    data_nastere = datetime.strptime(datan, '%d/%m/%y')

    data_nastere = data_nastere.date()

    return (date.today() - data_nastere).days

def test_get_age_in_days():
    assert (get_age_in_days("06/08/02")) == 7019
    assert (get_age_in_days('27/2/96')) == 9371

'''
Problema 13
'''
def get_temp(temp, scara1, scara2):
    """
    :param temp: primeste temperatura
    :param scara1: scara initiala
    :param scara2: scara in care se doreste sa fie transformata temperatura
    :return: returneaza valoarea temperaturii din scara1 in scara2
    """
    temp = int (temp)
    if scara1 == 'c':
        if scara2 == 'k':
            return temp + 273.15
        elif scara2 == 'f':
            return temp * 1.8 + 32
    elif scara1 == 'k':
        if scara2 == 'c':
            return temp - 273.15
        elif scara2 == 'f':
            return (temp - 32) / 1.8 + 273.15
    elif scara1 == 'f':
        if scara2 == 'c':
            return (temp - 32) / 1.8
        elif scara2 == 'k':
            return (temp - 32) * 5 / 9 + 273.15

    return temp
def test_get_temp():
    assert (round(get_temp(300, 'k', 'c'), 2)) == 26.85
    assert (round(get_temp(16, 'c', 'f'), 2)) == 60.8
    assert (round(get_temp(45, 'f', 'k'), 2)) == 280.37

'''
Problema 3
'''

def prim(n):
    '''
    Returneaza True daca numarul este prim, iar Flase in caz contrar
    :return:
    '''
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def test_prim():
    assert prim(7) == True
    assert prim(82) == False


def get_goldbach(n):
    """
    :param n: n numar natural
    :return: scrierea numarului n ca suma de 2 numere prime
    """

    for i in range(2, n):
        if prim(i):
            if prim(n - i):
                return i, n - i
    return False


def test_get_goldbach():
    assert get_goldbach(16) == (3, 13)
    assert get_goldbach(15) == (2, 13)

def show_menu():
    '''
    Printare meniu
    :return:
    '''
    print ('''
    1. Problema 2
    2. Problema 13.
    3. Problema 3
    x. Iesire
    ''')

def main():
    while True:
        show_menu()
        cmd = input ("Introduceti comanda dvs: ")
        if cmd == '1':
            datan = input ("Introduceti data nasterii: ")
            print (get_age_in_days(datan))

        elif cmd == '2':
            temp = int (input ("Introduceti temperatura: "))
            scara1 = input ("Introduceti scara temperaturii introduse: ")
            scara2 = input ("Introduceti scara in care doriti sa fie transformata temperatura: ")
            print (round(get_temp(temp, scara1, scara2)))
        elif cmd == '3':
            n = int(input("introduceti un numar intreg n: "))
            print(get_goldbach(n))
        elif cmd == 'x':
            break
        else:
            print ("Comanda invalida")

def run_tests():
    test_get_temp()
    test_get_age_in_days()
    test_prim()
    test_get_goldbach()

if __name__ == '__main__':
    run_tests()
    main()