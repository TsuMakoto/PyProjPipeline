from math import log10
from random import randint

import pandas as pd
from faker import Faker
from utils.operators.pipe import PipeOperator

faker = Faker('jp-JP')


def useId(ids, maximum=1000):
    for _ in range(maximum):
        Id = PipeOperator(1, maximum) * randint >> str
        Id = PipeOperator(maximum*10) * log10 * int >> Id.zfill

        if Id not in ids:
            return Id

    return maximum


class Users:
    def __init__(self):
        self.__id = []
        self.__username = []
        self.__name = []
        self.__sex = []
        self.__address = []
        self.__mail = []
        self.__birthdate = []

        self.__items = []

    class User:
        def __init__(self, ID: str):
            user = faker.simple_profile()

            self.ID = ID
            self.username = user["username"]
            self.name = user["name"]
            self.sex = user["sex"]
            self.address = user["address"]
            self.mail = user["mail"]
            self.birthdate = user["birthdate"]

    def add(self):
        user = Users.User(useId(self.__id))
        self.__items.append(user)

        self.__id.append(user.ID)
        self.__username.append(user.username)
        self.__name.append(user.name)
        self.__sex.append(user.sex)
        self.__address.append(user.address)
        self.__mail.append(user.mail)
        self.__birthdate.append(user.birthdate)

    def __getitem__(self, index: int) -> User:
        return self.__items[index]

    def make(self):
        pd.DataFrame({
            "ID": self.__id,
            "ユーザー名": self.__username,
            "氏名": self.__name,
            "性別": self.__sex,
            "住所": self.__address,
            "メールアドレス": self.__mail,
            "誕生日": self.__birthdate
        }).to_csv(
            "samples/files/users.csv",
            encoding='utf-8-sig',
            index=False
        )


class Companies:
    def __init__(self):
        self.__id = []
        self.__name = []
        self.__address = []
        self.__phone = []
        self.__worker_num = []

        self.__items = []

    class Company:
        def __init__(self, ID: str):
            self.ID = ID
            self.name = faker.company()
            self.address = faker.address()
            self.phone = faker.phone_number()
            self.worker_num = randint(1, 100)

    def add(self):
        company = Companies.Company(useId(self.__id))
        self.__items.append(company)

        self.__id.append(company.ID)
        self.__name.append(company.name)
        self.__address.append(company.address)
        self.__phone.append(company.phone)
        self.__worker_num.append(company.worker_num)

    def __getitem__(self, index: int) -> Company:
        return self.__items[index]

    def make(self):
        pd.DataFrame({
            "ID": self.__id,
            "社名": self.__name,
            "住所": self.__address,
            "電話番号": self.__phone,
            "従業員数": self.__worker_num
        }).to_csv(
            "samples/files/companies.csv",
            encoding='utf-8-sig',
            index=False
        )


class Jobs:
    def __init__(self):
        self.__user_id = []
        self.__company_id = []

    def add(self, user: Users.User, company: Companies.Company):
        self.__user_id.append(user.ID)
        self.__company_id.append(company.ID)

    def make(self):
        pd.DataFrame({
            "ユーザーID": self.__user_id,
            "会社ID": self.__company_id,
        }).to_csv(
            "samples/files/jobs.csv",
            encoding='utf-8-sig',
            index=False
        )
