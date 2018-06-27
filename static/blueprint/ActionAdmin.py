from datetime import date, datetime

from Data.database.controllers.UserController import UserController
from static.blueprint.TestData import testData
from flask import Blueprint, render_template, request, session, redirect

action_admin = Blueprint('action_admin', __name__, template_folder='templates')


@action_admin.route("/panel")
def AdminPanel():
    init = {
        'title': 'Panel zarządzania',
        'css':'menu',
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
        'nm': datetime.now().month - 1, # 0 - 11
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
    # list2 = []
    # Dater = UserController()
    # for x in Dater:
    #     list2.append(x.id)
    #     list2.append(x.name)
    #     list2.append(x.lastname)
    #     list2.append(x.email)
    #     list2.append(x.id_permission)
    #     list2.append(" -||- ")
    # print("Dane: {}".format(list2))

    return render_template('include/include_listOFsaved.html', list=list)

@action_admin.route("/include_detail-of-user-dinners", methods=['POST'])
def detail_dinner():
    id = request.form.get('id')
    nm = request.form.get('nm')
    year = request.form.get('year')
    print("ID: {} {} {}".format(id, nm, year))
    Dater = UserController()
    list = {'name':'Adam Małysz', 'list':[
        {'date':'06/06/2018', 's':'checked', 'o':'checked', 'k':'', 'pay':'Opłacone', 'price':10,'pay_action':'disabled'},
        {'date':'07/06/2018', 's':'', 'o':'checked', 'k':'checked', 'pay':'Zaległości', 'price':8, 'pay_action':''}]}
    return render_template('include/include_detail-of-user-dinners.html', init=list)
