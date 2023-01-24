from pipeline.steps.indexer import Indexer
from samples.steps.element.company_element import CompanyElement
from samples.steps.element.job_element import JobElement
from samples.steps.element.user_element import UserElement
from samples.steps.indexer.company_indexer import CompanyIndexer
from samples.steps.indexer.user_indexer import UserIndexer


class JonIndexer(Indexer[JobElement]):
    def compile(self,
                user_index: UserIndexer,
                company_index: CompanyIndexer):

        for job in self.sets:
            user = user_index[job.user_id]
            company = company_index[job.company_id]

            self.table[user.ID] = company

    def __getitem__(self, user: UserElement) -> CompanyElement:
        return self.table[user.ID]
