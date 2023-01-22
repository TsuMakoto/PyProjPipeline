from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import company_input, job_input, user_input
from samples.steps.appendix.company_appendix import CompanyAppendix
from samples.steps.appendix.job_appendix import JonAppendix
from samples.steps.appendix.user_appendix import UserAppendix


def main():
    params = Params(
        inputs={
            "user": user_input,
            "company": company_input,
            "job": job_input
        },
        outputs={
            "user": Output(UserAppendix()),
            "company": Output(CompanyAppendix()),
            "job": Output(JonAppendix(), ["user", "company"])
        }
    )

    appendixes = Pipeline(params).do()

    user_appendix: UserAppendix = appendixes["user"]
    job_appendix: JonAppendix = appendixes["job"]

    user = user_appendix[465]

    print(user)
    print(job_appendix[user])
