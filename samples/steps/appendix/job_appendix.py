from typing import Set

from pipeline.steps.appendix import Appendix
from samples.steps.element.company_element import CompanyElement
from samples.steps.element.job_element import JobElement
from samples.steps.element.user_element import UserElement


class JonAppendix(Appendix):
    def post_init(
            self,
            jobs: Set[JobElement],
            users: Set[UserElement],
            companies: Set[CompanyElement]):

        for job in jobs:
            user = self.__find_user(job, users)
            company = self.__find_company(job, companies)

            self.appendix[user.ID] = company

    def __getitem__(self, user: UserElement) -> CompanyElement:
        return self.appendix[user.ID]

    def __find_user(
            self,
            job: JobElement,
            users: Set[UserElement]) -> UserElement:
        for user in users:
            if job.user_id == user.ID:
                return user

    def __find_company(
            self,
            job: JobElement,
            companies: Set[CompanyElement]) -> CompanyElement:
        for company in companies:
            if company.ID == job.company_id:
                return company
