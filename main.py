#PROBLEMELE 2 SI 13

from datetime import datetime, date

'''
Problema 2
'''


def get_age_in_days(zile):
    '''

    :param zile: parametrul in care se salveaza varsta in zile
    :return: vasrta persoanei in zile
    '''
    data_curenta = date.today()
    zile = data_curenta - data_nastere

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

    if scara1 == 'k':
        if scara2 == 'c':
            temp = temp - 273.15
        elif scara2 == 'f':
            temp = (temp - 273.15) * 9 / 5 + 32
    elif scara1 == 'c':
        if scara2 == 'k':
            temp = temp + 273.15
        elif scara2 == 'f':
            temp = temp * 9 / 5 + 32
    elif scara1 == 'f':
        if scara2 == 'k':
            temp = (temp - 32) * 5 / 9 + 273.15
        elif scara2 == 'c':
            temp = (temp - 32) * 5 / 9

    return temp


def test_get_temp():
    assert get_temp(60, 'f', 'c') == 15.6
    assert get_temp(-55, 'f', 'c') == -48.3

test_get_temp()
