from pipeline.input import Input

from samples.steps.element.company_element import CompanyElement
from samples.steps.element.job_element import JobElement
from samples.steps.element.user_element import UserElement

user_input = Input(
    path="samples/files",
    name="users",
    element=UserElement
)

company_input = Input(
    path="samples/files",
    name="companies",
    element=CompanyElement
)

job_input = Input(
    path="samples/files",
    name="jobs",
    element=JobElement
)
