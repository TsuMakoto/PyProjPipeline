from pipeline.steps.appendix import Appendix
from samples.steps.element.user_element import UserElement


class UserAppendix(Appendix):
    def post_init(self, users: set[UserElement]):
        for user in users:
            self.appendix[user.ID] = user

    def __getitem__(self, ID: str) -> UserElement:
        return self.appendix[ID]
