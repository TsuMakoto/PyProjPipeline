from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import company_input, user_input
from samples.steps.appendix.company_appendix import CompanyAppendix
from samples.steps.appendix.user_appendix import UserAppendix


def main():
    params = Params(
        inputs={
            "user": user_input,
            "company": company_input
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
