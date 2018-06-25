
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