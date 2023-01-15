from pipeline.steps.element import Element


class CompanyElement(Element):
    @property
    def ID(self):
        return self.row["ID"]

    @property
    def name(self):
        return self.row["社名"]

    @property
    def address(self):
        return self.row["住所"]

    @property
    def phone(self):
        return self.row["電話番号"]

    @property
    def worker_num(self):
        return self.row["従業員数"]
