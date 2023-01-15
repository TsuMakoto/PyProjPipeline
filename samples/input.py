from pipeline.input import Input
from samples.steps.element.company_element import CompanyElement
from samples.steps.element.job_element import JobElement
from samples.steps.element.user_element import UserElement


class UserInput(Input):
    def _element(self, index, row) -> UserElement:
        return UserElement(index, row)


class CompanyInput(Input):
    def _element(self, index, row) -> CompanyElement:
        return CompanyElement(index, row)


class JobInput(Input):
    def _element(self, index, row) -> JobElement:
        return JobElement(index, row)
