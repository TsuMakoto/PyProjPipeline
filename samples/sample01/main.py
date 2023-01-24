from pipeline import Pipeline
from pipeline.output import Output
from pipeline.params import Params
from samples.input import company_input, user_input
from samples.steps.indexer.company_indexer import CompanyIndexer
from samples.steps.indexer.user_indexer import UserIndexer


def main():
    params = Params(
        inputs={
            "user": user_input,
            "company": company_input
        },
        outputs={
            "user": Output(UserIndexer),
            "company": Output(CompanyIndexer),
        }
    )

    indexes = Pipeline(params).do()

    user_index: UserIndexer = indexes["user"]
    company_index: CompanyIndexer = indexes["company"]

    print(user_index[465])
    print(company_index[876])
