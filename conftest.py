import pytest
from classes.person import Person
import logging

PEOPLE = []


def pytest_addoption(parser):
    parser.addoption("--n", type=int, default=5, help="Number of people to generate")


@pytest.fixture(scope="session")
def logger():
    return logging.getLogger(__name__)


def pytest_sessionstart(session):
    num_of_people = session.config.getoption("--n")
    for i in range(num_of_people):
        person = Person()
        person.generate_all()
        PEOPLE.append(person)


def pytest_generate_tests(metafunc):
    if "person" in metafunc.fixturenames:
        metafunc.parametrize("person", PEOPLE)
