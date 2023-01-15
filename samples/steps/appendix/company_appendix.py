from typing import Set

from pipeline.steps.appendix import Appendix
from samples.steps.element.company_element import CompanyElement


class CompanyAppendix(Appendix):
    def post_init(self, companies: Set[CompanyElement]):
        for company in companies:
            self.appendix[company.ID] = company

    def __getitem__(self, ID: str) -> CompanyElement:
        return self.appendix[ID]
