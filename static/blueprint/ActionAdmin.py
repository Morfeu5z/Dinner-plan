from datetime import date, datetime
import random

from Data.database.controllers.UserController import UserController, UserListController
from static.blueprint.TestData import testData
from flask import Blueprint, render_template, request, session, redirect

action_admin = Blueprint('action_admin', __name__, template_folder='templates')


@action_admin.route("/panel")
def AdminPanel():
    init = {
        'title': 'Panel zarządzania',
        'css': 'menu',
        'onStart': 'menu',
        'js': 'menu'
    }
    return render_template('index.html', init=init)


@action_admin.route("/include_menu")
def menu():
    if 'user_premission' in session:
        '''
        Funkcja ładująca menu funkcji
        po zalogowaniu do
        :return:
        '''
        premission = 'Administrator' if session['user_premission'] == 1 else 'Użytkownik'
        data = {
            'status': premission,
            'user': session['user_first_name'] + ' ' + session['user_last_name']
        }
        if session['user_premission'] == 1:
            return render_template('include/include_menu-admin.html', init=data)
        else:
            return render_template('include/include_menu-user.html', init=data)

    return redirect('/include_login')


@action_admin.route("/include_zapisani")
def listOfsavedBase():
    '''
    * Renderuje stronę z podstawowym widokiem,
    * resztę dociąga ajax w funkcji listOFsaved
    :return: basic view for users list
    '''
    # Parametry początkowe, powinien to być aktualny miesiąc i rok
    init = {
        'nm': datetime.now().month - 1,  # 0 - 11
        'year': datetime.now().year
    }
    return render_template('include/include_zapisani.html', init=init)


@action_admin.route("/include_listOFsaved", methods=['POST'])
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
    nm = int(request.form.get('nm')) + 1
    # year
    year = int(request.form.get('year'))
    # a - z or z - a
    az = request.form.get('az')
    # status of pay, yup or nope
    stat = request.form.get('stat')
    # for search
    search = request.form.get('user')
    print("Odebrano: {} - {} - {} - {} - {}".format(nm, year, az, stat, search))

    # Tworzenie testowej listy
    # Tu musi sie znaleźć funkcja przyjmująca parametry wypisywane powyżej
    # list = testData(nm)
    id_list = []
    dict = []
    # users = Dater.find_mies_rok(int(nm), int(year))
    if search == 'none':
        Dater = UserListController()
        for x in Dater.find_mies_rok(nm, year):
            print(x.user.name)
            if not x.user.id in id_list:
                dictme = {
                    'name': x.user.name + ' ' + x.user.lastname,
                    'date': '{} - {}'.format(year, nm),
                    'stat': 'Zapisany' if True == 1 else 'Nie zapisany',
                    'color': 'green' if True else 'red',
                    'id': x.user.id
                }
                dict.append(dictme)
                id_list.append(x.user.id)
    else:
        Dater = UserController()
        for x in Dater.find_by_name_or_lastname(search):
            if not x.id in id_list:
                dictme = {
                    'name': x.name + ' ' + x.lastname,
                    'date': '{} - {}'.format(year, nm),
                    'stat': 'Zapisany',
                    'color': 'green',
                    'id': x.id
                }
                dict.append(dictme)
                id_list.append(x.id)

    return render_template('include/include_listOFsaved.html', list=dict)


@action_admin.route("/include_detail-of-user-dinners", methods=['POST'])
def detail_dinner():
    id = int(request.form.get('id'))
    # nr of month, 0 - styczen, 11 - grudzien
    nm = int(request.form.get('nm')) + 1
    # year
    year = int(request.form.get('year'))
    print("ID: {} {} {}".format(id, nm, year))
    dict = []
    Dater = UserListController()
    user_name=''
    user_lastname=''
    for x in Dater.find_id_mies_rok(id, nm, year):
        user_name=x.user.name
        user_lastname=x.user.lastname
        box = [0]
        for x in range(3):
            box.append('checked' if random.randint(1,3) == x else '')
            box[0] = box[0] + 5 if box[x+1] == 'checked' else box[0]
        box.append(random.randint(0,1))

        if box[0] != 0:
            dictme = {
                'date': '{} - {}'.format(year, nm),
                's': box[1],
                'o': box[2],
                'k': box[3],
                'pay': 'Opłacono' if box[4] == 1 else 'Nie opłacono',
                'price': box[0],
                'pay_action': 'disabled' if [4] == 1 else '',
                'color': 'green' if box[4] == 1 else 'red',
                'btn_action':'Zaksięguj'
            }
            dict.append(dictme)

    list = {
        'name': user_name + ' ' + user_lastname,
        'list': dict
    }

    # list = {'name': 'Adam Małysz', 'list': [
    #     {'date': '06/06/2018', 's': 'checked', 'o': 'checked', 'k': '', 'pay': 'Opłacone', 'price': 10,
    #      'pay_action': 'disabled'},
    #     {'date': '07/06/2018', 's': '', 'o': 'checked', 'k': 'checked', 'pay': 'Zaległości', 'price': 8,
    #      'pay_action': ''}]}
    return render_template('include/include_detail-of-user-dinners.html', init=list)
