from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import company_input, job_input, user_input
from samples.steps.indexer.company_indexer import CompanyIndexer
from samples.steps.indexer.job_indexer import JonIndexer
from samples.steps.indexer.user_indexer import UserIndexer


def main():
    params = Params(
        inputs={
            "user": user_input,
            "company": company_input,
            "job": job_input
        },
        outputs={
            "user": Output(UserIndexer),
            "company": Output(CompanyIndexer),
            "job": Output(JonIndexer, ["user", "company"])
        }
    )

    indexes = Pipeline(params).do()

    user_index: UserIndexer = indexes["user"]
    job_index: JonIndexer = indexes["job"]

    user = user_index[465]

    print(user)
    print(job_index[user])
