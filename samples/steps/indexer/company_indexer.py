from pipeline.steps.indexer import Indexer
from samples.steps.element.company_element import CompanyElement


class CompanyIndexer(Indexer[CompanyElement]):
    def _make(self):
        return {company.ID: company for company in self.sets}
