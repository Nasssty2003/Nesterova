from Tests import Salary, Vacancy, DataSet
from unittest import TestCase

class SalaryTests(TestCase):
    def test_salary_type(self):
        self.assertEqual(type(Salary(15.0, 25.5, 20.25, 'RUR')).__name__, 'Salary')

    def test_salary_from(self):
        self.assertEqual(Salary(20.0, 30.0, 30.0, 'EUR',).salary_from, 20)

    def test_salary_to(self):
        self.assertEqual(Salary(20.0, 30.0, 30.0, 'EUR',).salary_to, 30)

    def test_salary_gross(self):
        self.assertEqual(Salary(20.0, 30.0, 30.0, 'EUR',).salary_gross, 30)

    def test_salary_currency(self):
        self.assertEqual(Salary(20.0, 30.0, 25.0, 'EUR',).salary_currency, 'EUR')


class VacancyTests(TestCase):
    def test_vacancy_type(self):
        self.assertEqual(type(Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001')).__name__, 'Vacancy')

    def test_vacancy_name(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').name, 'Аналитик')

    def test_vacancy_description(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').description, 'Анализирует')

    def test_vacancy_key_skills(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').key_skills, 'Python')

    def test_vacancy_experience_id(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').experience_id, 'От 1 года до 3 лет')

    def test_vacancy_premium(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').premium, 'Да')

    def test_vacancy_employer_name(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').employer_name, '1Ц')

    def test_vacancy_salary(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').salary, '300')

    def test_vacancy_area_name(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').area_name, 'Екатеринбург')

    def test_vacancy_published_at(self):
        self.assertEqual(Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').published_at, '2.2.2002')


class DataSetTests(TestCase):
    def test_dataset_type(self):
        self.assertEqual(type(DataSet('filename.abc', Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001'))).__name__, 'DataSet')

    def test_dataset_file_name(self):
        self.assertEqual(DataSet('filename.abc', Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001')).file_name, 'filename.abc')