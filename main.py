#PROBLEMELE 2, 3 SI 13

from datetime import datetime, date

'''
Problema 2
'''


def get_age_in_days():
    '''

    :param zile: parametrul in care se salveaza varsta in zile
    :return: vasrta persoanei in zile
    '''
    data_curenta = date.today()
    zile = int (data_curenta) - int (data_nastere)
    return zile

def data_nasterii(datan: str):
    '''
    Functie folosita pentru a transforma data citita de tip str in .date()
    '''

    data_nastere = datetime.strptime(datan, '%d/%m/%y')

    data_nastere = data_nastere.date()

    return data_nastere





'''
Problema 13
'''
def get_temp(temp: float, scara1: str, scara2: str):
    """
    :param temp: primeste temperatura
    :param scara1: scara initiala
    :param scara2: scara in care se doreste sa fie transformata temperatura
    :return: returneaza valoarea temperaturii din scara1 in scara2
    """

    if scara1 == 'C':
        if scara2 == 'K':
            return temp + 273.15
        elif scara2 == 'F':
            return temp * 1.8 + 32
    elif scara1 == 'K':
        if scara2 == 'C':
            return temp - 273.15
        elif scara2 == 'F':
            return (temp - 32) / 1.8 + 273.15
    elif scara1 == 'F':
        if scara2 == 'C':
            return (temp - 32) / 1.8
        elif scara2 == 'K':
            return (temp - 32) * 5 / 9 + 273.15

    return temp


def test_get_temp():
    assert (round(get_temp(300, 'k', 'c'), 2)) == 26.85
    assert (round(get_temp(16, 'c', 'f'), 2)) == 60.8
    assert (round(get_temp(45, 'f', 'k'), 2)) == 280.37


test_get_temp()


'''
Problema 3

'''

def is_prime(n):
    """
       :param n:  numar natural
       :return: True daca numarul n este prim si False daca numarul n nu este prim
    """
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def test():
    assert is_prime(3) == True
    assert is_prime(4) == False


def get_goldbach(n):
    """
    :param n: n numar natural
    :return: scrierea numarului n ca suma de 2 numere prime
    """

    for i in range(2, n):
        if is_prime(i):
            if is_prime(n - i):
                return i, n - i
    return False


def test_get_goldbach():
    assert get_goldbach(16) == (3, 13)
    assert get_goldbach(15) == (2, 13)

def meniu():
    print('''
1.Problema 2
2.Problema 13
3.Problema 3
4.Afara''')


def main():


    while True:
        meniu()
        cmd = input("Comanda:")
        if cmd == '1':
            data1 = input("introduceti data nasterii in format zz/ll/aa")
            data_nasterii (data1)
            print (get_age_in_days())
        elif cmd == '2':
            temp = input ("Introduceti temperatura:")
            scara_initiala = input ("Introduceti scara initiala:")
            scara_dorita = input ("Introduceti scara dorita:")
            print(get_temp(temp, scara_initiala, scara_dorita))
        elif cmd == '3':
            n = int(input("introduceti un numar intreg n"))
            print(get_goldbach(n))
        elif cmd == '4':
            break
        else:
            print('comanda invalida')

if __name__ == '__main__':
    main()
