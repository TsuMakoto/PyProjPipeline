import os
import sys
from random import sample

import click

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def __make_data():
    from samples.make_data import Companies, Jobs, Users

    nums = 100
    users = Users()
    companies = Companies()
    jobs = Jobs()

    for _ in range(nums):
        users.add()
        companies.add()

    li = list(range(nums))
    user_indexes = sample(li, len(li))
    company_indexes = sample(li, len(li))

    for i in range(nums):
        user_index = user_indexes[i]
        company_index = company_indexes[i]

        user = users[user_index]
        company = companies[company_index]

        jobs.add(user, company)

    users.make()
    companies.make()
    jobs.make()


@click.command()
@click.option('--execute', '-e', type=int, default=1)
@click.option('--make_data', '-m', is_flag=True)
def main(execute: int, make_data: bool):
    if make_data:
        __make_data()
    else:
        pass


if __name__ == "__main__":
    main()
