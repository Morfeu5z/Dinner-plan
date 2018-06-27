from ..models import User, Permission, Dinnerset, Dinnertype, Userlist, Dinner, Dinnercomposit
from datetime import date, timedelta
from sqlalchemy import or_
import calendar
import hashlib
from ...database import IConnector
from copy import deepcopy


class UserController(IConnector):

    def regestration(self, email: str, password: str, name: str, lastname:str, permission : int = 2) -> int:
        """

        :param email: string
        :param password: md5
        :param name: string
        :param lastname string
        :param permission - id permission to object;
        :return: new user id
        """
        """
        md5 = hashlib.md5()
        password = password.strip()
        md5.update(bytearray(password, encoding="UTF-8"))
        """
        #new_user = User(email, md5.hexdigest(), name, lastname, permission)
        new_user = User(email, password, name, lastname, permission)
        if(self.session.query(User).filter_by(email=email).count()):
            return deepcopy(self.session.query(User).filter_by(email=email).filter_by(password=password).first())
        #new_user = User(email, password, name, lastname, permission)
        try:
            self.session.add(new_user)
            self.session.commit()
            return deepcopy(new_user)
        except:
            self.session.rollback()



    def login(self, email: str, password : str) -> User:
        """

        :param email: string
        :param password: string
        :return: isset user data
        """
        user = self.session.query(User).filter_by(email=email).filter_by(password=password).first()
        return user

    def find_by_name_or_lastname(self, text:str):
        text = text.strip()
        users = list()
        if len(text.split(" ")) > 1:
            imie, nazwisko = text.split()
            users = self.session.query(User).filter(or_(User.name.ilike('%{im}%'.format(im=imie)), User.lastname.ilike('%{nzw}%'.format(nzw=nazwisko)))).all()
        elif len(text.split(" ")) == 1:
            users = self.session.query(User).filter(or_(User.name.ilike('%{text}%'.format(text=text)), User.lastname.ilike('%{text}%'.format(text=text)))).all()
        if len(users) == 0:
            users = self.session.query(User).all()
        return users

    def change_permissions(self, id: int, id_permission: int):
        user = self.session.query(User).filter_by(id=id)
        user.id_permission = id_permission
        try:
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(user)

    def delete_by_email(self, email):
        user_to_removing = self.session.query(User).filter_by(email=email).first()
        user_to_return = deepcopy(user_to_removing)
        try:
            self.session.delete(user_to_removing)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return user_to_return

    def delete_by_id(self, id):
        user_to_removing = self.session.query(User).filter_by(id=id).first()
        user_to_return = deepcopy(user_to_removing)
        try:
            self.session.delete(user_to_removing)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return user_to_return

    def __iter__(self):
        users = self.session.query(User)
        for user in users:
            yield user


class PermissionsController(IConnector):

    def create(self, permission):
        new_permission = Permission(permission)
        try:
            self.session.add(new_permission)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return new_permission

    def delete(self, id):
        delete = self.session.query(Permission).filter_by(id=id).first()
        return_del_object = deepcopy(delete)
        try:
            self.session.delete(delete)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return return_del_object

    def __iter__(self):
        permissions = self.session.query(Permission)
        for perm in permissions:
            yield perm


class DinnerController(IConnector):

    def create(self, dinner, about):
        dinner = Dinner(dinner, about)
        try:
            self.session.add(dinner)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return dinner

    def update(self, id : int, dinner : str, about : str):
        if not (self.session.query(Dinnerset).filter_by(id_dinner=id).count()):
            update = self.session.query(Dinner).filter_by(id=id).first()
            update.dinner = dinner
            update.more = about
            try:
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return deepcopy(update)

    def delete(self, id):
        if not (self.session.query(Dinnerset).filter_by(id_dinner=id).count()):
            delete = self.session.query(Dinner).filter_by(id=id).first()
            return_del_object = deepcopy(delete)
            try:
                self.session.delete(delete)
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return return_del_object

    def __iter__(self):
        dinners = self.session.query(Dinner)
        for dinner in dinners:
            yield dinner

    def find_by_id(self, id):
        find = self.session.query(Dinner).filter_by(id=id).first()
        return deepcopy(find)

    def find_by_dinner(self, dinner):
        find = self.session.query(Dinner).filter_by(dinner=dinner).first()
        return deepcopy(find)

    def return_all(self):
        return self.session.query(Dinner)

class DinnerTypeController(IConnector):

    def create(self, type, cena):
        type = Dinnertype(type, cena)
        try:
            self.session.add(type)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(type)

    def delete(self, id):
        if not (self.session.query(Dinnerset).filter_by(id_dinnertype=id).count()):
            delete = self.session.query(Dinnertype).filter_by(id=id).first()
            return_del_object = deepcopy(delete)
            try:
                self.session.delete(delete)
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return return_del_object

    def update(self, id: int, dinnertype: str, price: str):
            update = self.session.query(Dinnertype).filter_by(id=id).first()
            update.dinnertype = dinnertype
            update.price = price
            try:
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return deepcopy(update)

    def __iter__(self):
        dinners = self.session.query(Dinnertype)
        for dinner in dinners:
            yield dinner


class DinnerSetController(IConnector):

    def create(self, id_dinnertype):
        new = Dinnerset(id_dinnertype)
        try:
            self.session.add(new)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(new)

    def delete(self, id):
        if not (self.session.query(Userlist).filter_by(id_dinnerset=id).count()):
            delete = self.session.query(Dinnerset).filter_by(id=id).first()
            return_del_object = deepcopy(delete)
            try:
                self.session.delete(delete)
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return return_del_object

    def update(self, id, id_dinnertype: str):
        if not (self.session.query(Userlist).filter_by(id_dinnerset=id).count()):
            update = self.session.query(Dinnerset).filter_by(id=id).first()
            update.id_dinnertype = id_dinnertype
            try:
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return deepcopy(update)

    def __iter__(self):
        Objects = self.session.query(Dinnerset)
        for unit in Objects:
            yield unit#tuple((unit.dinner.dinner, unit.dinner.more, unit.dinnertype, unit.dinnertype.price))

    def find(self, id):
        Object = self.session.query(Dinnerset).filter_by(id=id).first()
        return deepcopy(Object)#tuple((Object.dinner.dinner, Object.dinner.more, Object.dinnertype, Object.dinnertype.price))


class DinnerCompositController(IConnector):

    def create(self, id_dinner, id_dinnerset):
        composti = Dinnercomposit(id_dinner, id_dinnerset)
        try:
            self.session.add(composti)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(composti)

    def delete(self, id):
            delete = self.session.query(Dinnercomposit).filter_by(id=id).first()
            return_del_object = deepcopy(delete)
            try:
                self.session.delete(delete)
                self.session.commit()
            except:
                self.session.rollback()
                return None
            return return_del_object

    def __iter__(self):
        find = self.session.query(Dinnercomposit)
        for x in find:
            yield x

class UserListController(IConnector):

    def create(self, id_user: str, id_dinnerset, bought:bool, dinnerdate):
        userlist = Userlist(id_user, id_dinnerset, bought, dinnerdate)
        try:
            self.session.add(userlist)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(userlist)

    def delete(self, id: int):
        delete = self.session.query(Userlist).filter_by(id=id).first()
        return_del_object = deepcopy(delete)
        try:
            self.session.delete(delete)
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return return_del_object

    def update(self, id: int, id_user, id_dinnerset, bought, dinnerdate):
        Userl = self.session.query(Userlist).filter_by(id=id).first()
        Userl.id_dinnerset = id_dinnerset
        Userl.id_user = id_user
        Userl.bought = bought
        Userl.dinnerdate = dinnerdate
        try:
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(Userl)

    def pay(self, id: int, bought: bool = True):
        Userl = self.session.query(Userlist).filter_by(id=id).first()
        Userl.bought = bought
        try:
            self.session.commit()
        except:
            self.session.rollback()
            return None
        return deepcopy(Userl)

    def find(self, id):
        temp = self.session.query(Userlist).filter_by(id=id).first()
        return temp

    def find_id_mies_rok(self, id_user, mies, rok):
        """

        :return:
        """
        start = date(rok, mies, 1)
        finish = self.___add_months(start, 1)
        for x in self.session.query(Userlist).filter_by(id_user=id_user).all():
            if start <= x.dinnerdate <= finish:
                yield x

    def find_mies_rok(self, mies, rok):
        """

        :return:
        """
        start = date(rok, mies, 1)
        finish = self.___add_months(start, 1)
        for x in self.session.query(Userlist).all():
            if start <= x.dinnerdate <= finish:
                yield x

    def __iter__(self):
        Objects = self.session.query(Userlist)
        for Object in Objects:
            yield Object

    #def get_user_lit(self, dinnertype=None, day_date=None, payed=None):
    #    if dinnertype != None
    def ___add_months(self, sourcedate:date , months):
         month = sourcedate.month - 1 + months
         year = sourcedate.year + month // 12
         month = month % 12 + 1
         day = min(sourcedate.day,calendar.monthrange(year,month)[1])
         return date(year,month,day)



