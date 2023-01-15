from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import CompanyInput, JobInput, UserInput
from samples.steps.appendix.company_appendix import CompanyAppendix
from samples.steps.appendix.job_appendix import JonAppendix
from samples.steps.appendix.user_appendix import UserAppendix


def main():
    params = Params(
        inputs={
            "user": UserInput("samples/files", "users"),
            "company": CompanyInput("samples/files", "companies"),
            "job": JobInput("samples/files", "jobs")
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
