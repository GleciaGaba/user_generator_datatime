"""Module to generate random users"""

import faker
import logging
from pathlib import Path
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.INFO)


# fake data generator
fake = faker.Faker("fr_FR")


def get_user() -> str:
    """
    Generate a single user

    :return str: full name of a single user.
    """
    logger.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n) -> list[str]:
    """
    Generate a list of users

    :param int : the number of users
    :return [str]: a list of users
    """
    """users = []

    for i in range(n):
        users.append(get_user())
        return users"""
    logging.info(f"Generating a list of {n} user.")
    return [get_user() for _ in range(n)]


if __name__ == '__main__':
    user = get_user()
    print(user)
