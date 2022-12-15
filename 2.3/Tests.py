import csv
import re
from var_dump import var_dump as vd_print
import doctest


class Salary:
    """Класс для представления зарплаты.
    Attributes:
        salary_from (int): Нижняя граница вилки оклада
        salary_to (int): Верхняя граница вилки оклада
        salary_gross (int): Оклад до вычета налогов
        salary_currency (int): Валюта оклада
    """
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        """Инициализирует объект Salary
        Args:
            salary_from (str or int or float): Нижняя граница вилки оклада
            salary_to (str or int or float): Верхняя граница вилки оклада
            salary_gross (str or int or float): Оклад до вычета налогов
            salary_currency (str or int or float): Валюта оклада
        >>> type(Salary(15.0, 25.5, 20.25, 'RUR')).__name__
        'Salary'
        >>> Salary(20.0, 30.0, 30.0, 'EUR',).salary_from
        20.0
        >>> Salary(20.0, 30.0, 30.0, 'EUR',).salary_to
        30.0
        >>> Salary(20.0, 30.0, 30.0, 'EUR',).salary_gross
        30.0
        >>> Salary(20.0, 30.0, 25.0, 'EUR',).salary_currency
        'EUR'
        """
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency


class Vacancy:
    """Класс для представления вакансий
    Attributes:
        name (str): Название
        description (str): Описание
        key_skills (str): Навыки
        experience_id (str): Опыт работы
        premium (str): Премиум-вакансия
        employer_name (str): Компания
        salary (str): Оклад
        area_name (str): Название региона
        published_at (str): Дата и время публикации вакансии
    """
    def __init__(self, name, description, key_skills, experience_id, premium, employer_name, salary, area_name, published_at):
        """Инициализирует объект Vacancy
        Args:
            name (str): Название
            description (str): Описание
            key_skills (str): Навыки
            experience_id (str): Опыт работы
            premium (str): Премиум-вакансия
            employer_name (str): Компания
            salary (str): Оклад
            area_name (str): Название региона
            published_at (str): Дата и время публикации вакансии
        >>> type(Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001')).__name__
        'Vacancy'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').name
        'Аналитик'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').description
        'Анализирует'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').key_skills
        'Python'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').experience_id
        'От 1 года до 3 лет'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').premium
        'Да'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').employer_name
        '1Ц'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').salary
        '300'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').area_name
        'Екатеринбург'
        >>> Vacancy('Аналитик', 'Анализирует', 'Python', 'От 1 года до 3 лет', 'Да', '1Ц', '300', 'Екатеринбург', '2.2.2002').published_at
        '2.2.2002'
        """
        self.name = name
        self.description = description
        self.key_skills = key_skills
        self.experience_id = experience_id
        self.premium = premium
        self.employer_name = employer_name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at


class DataSet:
    """Класс oбрабатывает и считывает данные файла
    Attributes:
        file_name (str): Название файла
        vacancies_objects (Vacancy): Данные вакансий
    """
    def __init__(self, file_name, vacancies_objects):
        """Инициализирует объект DataSet
        Args:
            file_name (str): Название файла
            vacancies_objects (Vacancy): Данные вакансий
        >>> type(DataSet('filename.abc', Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001'))).__name__
        'DataSet'
        >>> DataSet('filename.abc', Vacancy('Программист', 'Программирует', 'Python, C#', 'Нет опыта', 'Нет', 'BoxSkill', '100', 'Екатеринбург', '1.1.2001')).file_name
        'filename.abc'
        """
        self.file_name = file_name
        self.vacancies_objects = vacancies_objects


trash = {'<.*?>': '', '\s+': ' '}

def clear_trash(string):
    """Функция для отчищения строк от html-тегов, пробелов и переноса строк.
    Args:
         string (str): Строка
    Функция возвращает данные типа str
    """
    clean_string = string
    for key, value in trash.items():
        clean_string = re.sub(key, value, clean_string.strip())
    return ', '.join(clean_string.split("\n"))

def clear_fields(array):
    """Функция для удаления html-тегов и \n из строк, находящихся в списке.
    Args:
        array (list): Массив
    Функция возвращает данные типа list
    """
    cleared_array = []
    for sub_array in array:
        transport = []
        for string in sub_array:
            string = clear_trash(string)
            transport.append(string)
        cleared_array.append(transport)
    return cleared_array

def get_list(string):
    """Функция для разделения строки на элементы списка.
    Args:
        string (str): Строка
    Функция возвращает данные типа list
    """
    return string.split(', ')

def convert(keys, values):
    """Функция для распределения keys и values по классам Vacancy и Salary.
    Args:
        keys (list): в данный аргумент передаются заголовки столбиков
        values (list):  в этот аргумент передаётся информация по вакансиям
    Функция возвращает данные типа list
    """
    full_list = []
    for element in values:
        dictionary = dict(zip(keys, element))
        salaries = Salary(dictionary["salary_from"], dictionary["salary_to"], dictionary["salary_gross"], dictionary["salary_currency"])
        vacancy_obj = Vacancy(dictionary["name"], dictionary["description"], get_list(dictionary["key_skills"]), dictionary["experience_id"],
                              dictionary["premium"], dictionary["employer_name"], salaries, dictionary["area_name"], dictionary["published_at"])
        full_list.append(vacancy_obj)
    return full_list

def get_inputs():
    """Функция, которая принимает входные данные.
    При ее вызове к ней на вход не поступают никакие аргументы.
    Функция возвращает данные типа str
    """
    set_file = input('Введите название файла: ')
    set_filter = input('Введите параметр фильтрации: ')
    set_sort = input('Введите параметр сортировки: ')
    set_order = input('Обратный порядок сортировки (Да / Нет): ')
    set_range = input('Введите диапазон вывода: ')
    set_columns = input('Введите требуемые столбцы: ')

    return set_file, set_filter, set_sort, set_order, set_range, set_columns

def make_titles(file):
    """Функция для создания листа заголовок по следующей строчке csv-файла.
    Args:
        file (str): Название файла
    При вызове данной функции она попытается создать и вернуть заголовки стоблцов из csv-файла в виде
    данных типа list. Если на вход поступает пустой файл, то может выйти ошибка StopIteration, при ловле
    которой программа выдаёт, что на вход поступил пустой файл, после чего работа программы заканчивается.
    """
    try:
        get_titles = next(file)
        return get_titles
    except StopIteration:
        print("Пустой файл")
        exit()


def main():
    """Основная функция, которая будет вызвана при запуске программы.
    Данная функция ничего не принимает в качестве аргументов и ничего возвращает.
    """
    file_name, filter_set, sort_by, order, output_range, columns = get_inputs()
    csv_file = csv.reader(open(file_name, encoding='utf-8-sig'), delimiter=",")
    titles = make_titles(csv_file)
    fields = clear_fields([l for l in csv_file if len(l) == len(titles) and l.count("") == 0])
    vacancies = convert(titles, fields)

    vd_print(DataSet(file_name, vacancies))


if __name__ == "__main__":
    # main()
    print(doctest.testmod())