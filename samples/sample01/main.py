from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import CompanyInput, UserInput
from samples.steps.appendix.company_appendix import CompanyAppendix
from samples.steps.appendix.user_appendix import UserAppendix


def main():
    params = Params(
        inputs={
            "user": UserInput("samples/files", "users"),
            "company": CompanyInput("samples/files", "companies")
        },
        outputs={
            "user": Output(UserAppendix()),
            "company": Output(CompanyAppendix()),
        }
    )

    appendixes = Pipeline(params).do()

    user_appendix: UserAppendix = appendixes["user"]
    company_appendix: CompanyAppendix = appendixes["company"]

    print(user_appendix[465])
    print(company_appendix[876])
