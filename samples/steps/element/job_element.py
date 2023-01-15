from pipeline.steps.element import Element


class JobElement(Element):
    @property
    def user_id(self):
        return self.row["ユーザーID"]

    @property
    def company_id(self):
        return self.row["会社ID"]
