from utils.utils import generate_age, generate_gender, generate_nationality


class TestPerson:
    def test_gender(self, person, logger):
        gender = generate_gender(person.name)
        logger.info(f"Comparing {person.gender} : {gender}")
        assert person.gender == gender

    def test_age(self, person, logger):
        age = generate_age(person.name)
        logger.info(f"Comparing {person.age} : {age}")
        assert person.age == age

    def test_nationality(self, person, logger):
        nationality = generate_nationality(person.name)
        logger.info(f"Comparing {person.nationality} : {nationality}")
        assert person.nationality == nationality
