from pipeline.steps.indexer import Indexer
from samples.steps.element.user_element import UserElement


class UserIndexer(Indexer[UserElement]):
    def _make(self):
        return {user.ID: user for user in self.sets}
