from pipeline.steps.element import Element


class UserElement(Element):
    @property
    def ID(self):
        return self.row["ID"]

    @property
    def username(self):
        return self.row["ユーザー名"]

    @property
    def name(self):
        return self.row["氏名"]

    @property
    def sex(self):
        return self.row["性別"]

    @property
    def address(self):
        return self.row["住所"]

    @property
    def mail(self):
        return self.row["メールアドレス"]

    @property
    def birthday(self):
        return self.row["誕生日"]
