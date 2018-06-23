from datetime import date, datetime

from flask import Blueprint, render_template, request

admin_panel = Blueprint('admin_panel', __name__, template_folder='templates')


@admin_panel.route("/include_menu")
def menu():
    data = {
        'status': 'Administrator',
        'user': 'Aleksander Sinkowski'
    }
    return render_template('include/include_menu.html', init=data)


@admin_panel.route("/include_zapisani")
def listOfsavedBase():
    '''
    * Renderuje stronę z podstawowym widokiem,
    * resztę dociąga ajax w funkcji listOFsaved
    :return: basic view for users list
    '''
    # Parametry początkowe, powinien to być aktualny miesiąc i rok
    init = {
        'nm': datetime.now().month - 1, # 0 - 11
        'year': datetime.now().year
    }
    return render_template('include/include_zapisani.html', init=init)


def testData(nm):
    '''
    * Funkcja z danymi testowymi,
    * przyjmuje numer miesiąca
    :param nm:
    :return: test - list of users
    '''
    if nm == '0':
        list = [{
            'name': 'Aleksander Sinkowski',
            'date': 'Styczeń 2018',
            'stat': 'Opłacono',
            'color': 'green',
            'id':'1'
        }, {
            'name': 'Serhii Riznychuk',
            'date': 'Styczeń 2018',
            'stat': 'Opłacono',
            'color': 'green',
            'id':'2'
        }, {
            'name': 'Mikołaj Rychel',
            'date': 'Styczeń 2018',
            'stat': 'Nie opłacono',
            'color': 'red',
            'id':'3'
        }]
    else:
        list = []
        for x in range(400):
            list.append({
                'name': 'Aleksander Sinkowski',
                'date': 'Luty 2018',
                'stat': 'Opłacono',
                'color': 'green',
                'id':'1'
            })
    return list


@admin_panel.route("/include_listOFsaved", methods=['POST'])
def listOfsaved():
    '''
    * Funkcja przyjmuje cztery parametry z posta
    * i przekazuje je do funkcji zwracającej
    * listę użytkowników zapisanych do stołóki

    :name return_user_list_in_month: def
    :param nm: int numer miesiąca do wyświetlenia ( od 0 do 11 )
    :param year : int wybrany rok ( 2018 )
    :param az : bool sortowanie od a-z ( True ) lub od z-a ( False )
    :param stat : bool sortowanie po statusie opłacony ( True ) lub nieopłacony ( False )
    :param search : str przesłanie stringa, po którym szukana będzie osoba zapisana na miesiąc podany wyżej, jeśli parametr pusty to nie szukaj

    :return tuple( [ id, user, date, status, color, id ],  ):

    przyklad = ([Jan Kowalski, Styczeń 2018, Opłacono, green, 42], [Adam Nowak, Styczeń 2018, Nieopłacono, red, 69])
    '''

    # nr of month, 0 - styczen, 11 - grudzien
    nm = request.form.get('nm')
    # year
    year = request.form.get('year')
    # a - z or z - a
    az = request.form.get('az')
    # status of pay, yup or nope
    stat = request.form.get('stat')
    # for search
    search = request.form.get('user')
    print("Odebrano: {} - {} - {} - {} - {}".format(nm, year, az, stat, search))

    # TODO Funkcja zwaracająca jsona z danymi
    # Tworzenie testowej listy
    # Tu musi sie znaleźć funkcja przyjmująca parametry wypisywane powyżej
    list = testData(nm)

    return render_template('include/include_listOFsaved.html', list=list)
