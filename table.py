import csv
import re
from prettytable import PrettyTable

#Класс зарплаты
class Salary:
    #метод для перевода названий валют на русский язык
    translate = {'AZN': 'Манаты', 'BYR': 'Белорусские рубли', 'EUR': 'Евро', 'GEL': 'Грузинский лари',
                 'KGS': 'Киргизский сом', 'KZT': 'Тенге', 'RUR': 'Рубли', 'UAH': 'Гривны', 'USD': 'Доллары',
                 'UZS': 'Узбекский сум'}
    #словарь для перевода валют в рубли
    currency_to_rub = {"AZN": 35.68, "BYR": 23.91, "EUR": 59.90, "GEL": 21.74, "KGS": 0.76, "KZT": 0.13, "RUR": 1,
                    "UAH": 1.64, "USD": 60.66, "UZS": 0.0055}

    # Конструктор для объектов класса Salary(зарплата)
    def __init__(self, vacancy):
        self.salary_from = int(float(vacancy['salary_from']))
        self.salary_to = int(float(vacancy['salary_to']))
        self.salary_gross = 'Без вычета налогов' if vacancy['salary_gross'].lower() == 'true' else 'С вычетом налогов'
        self.salary_currency = vacancy['salary_currency']
        self.salary_average = Salary.currency_to_rub[self.salary_currency] * (self.salary_from + self.salary_to) / 2

    #метод форматирует данные о ЗП
    def __str__(self):
        return '{0:,} - {1:,} ({2}) ({3})'.format(self.salary_from, self.salary_to,
                                                  Salary.translate[self.salary_currency],
                                                  self.salary_gross).replace(',', ' ')

#Класс вакансии
class Vacancy:
    order = ['index', 'name', 'description', 'key_skills', 'experience_id', 'premium', 'employer_name', 'salary', 'area_name', 'published_at']
    #создаём словари для значений опыта работы
    experience_values = {'Нет опыта': 1, 'От 1 года до 3 лет': 2, 'От 3 до 6 лет': 3, 'Более 6 лет': 4}
    experience = {'noExperience': 'Нет опыта', 'between1And3': 'От 1 года до 3 лет', 'between3And6': 'От 3 до 6 лет',
                     'moreThan6': 'Более 6 лет'}

    # Конструктор для объектов класса Vacancy(вакансия)
    def __init__(self, vacancy):
        self.index = 0
        self.name = self.clean(vacancy['name'])
        self.description = self.control(self.clean(vacancy['description']))
        self.skills = vacancy['key_skills'].split('\n')
        self.key_skills = self.control(vacancy['key_skills'])
        self.skills_length = len(self.skills)
        self.experience_id = self.experience[vacancy['experience_id']]
        self.premium = 'Да' if vacancy['premium'].lower() == 'true' else 'Нет'
        self.employer_name = vacancy['employer_name']
        self.salary_class = Salary(vacancy)
        self.salary = str(self.salary_class)
        self.area_name = vacancy['area_name']
        self.published = vacancy['published_at']
        self.published_at = '{0[2]}.{0[1]}.{0[0]}'.format(vacancy['published_at'][:10].split('-'))

    #метод очищает код от лишних пробелов и html-кода
    @staticmethod
    def clean(string):
        result = re.sub(r'<.*?>', '', string)
        result = re.sub(r'\s+', ' ', result)
        return result.strip()

    #метод проверяет, чтобы строка не превышала 100 символов
    @staticmethod
    def control(string):
        return string if len(string) <= 100 else string[:100] + '...'

    #метод определяет среднюю ЗП
    @property
    def salary_average(self):
        return self.salary_class.salary_average

    #метод определяет валюту ЗП
    @property
    def salary_currency(self):
        return self.salary_class.salary_currency

    # метод определяет нижнюю границу ЗП
    @property
    def salary_from(self):
        return self.salary_class.salary_from

    # метод определяет верхнюю границу ЗП
    @property
    def salary_to(self):
        return self.salary_class.salary_to

    #метод задаёт вес опыта работы
    @property
    def experience_weight(self):
        return self.experience_values[self.experience_id]

    # метод создаёт из данных список
    def get_list(self):
        return [getattr(self, key) for key in self.order]

#Класс данных
class DataSet:
    #создаём словарь для перевода атрибутов на русский язык
    translate_dictionary = {'Описание': 'description', 'Навыки': 'skills_length', 'Оклад': 'salary_average',
                     'Дата публикации вакансии': 'published', 'Опыт работы': 'experience_weight',
                     'Премиум-вакансия': 'premium',
                     'Идентификатор валюты оклада': 'salary_currency', 'Название': 'name',
                     'Название региона': 'area_name',
                     'Компания': 'employer_name'}
    # создаём словарь для перевода атрибутов с условием на русский язык
    conditions_sort = {'Навыки': lambda vacancy, value: all([skill in vacancy.skills for skill in value.split(', ')]),
                       'Оклад': lambda vacancy, value: vacancy.salary_from <= float(value) <= vacancy.salary_to,
                       'Дата публикации вакансии': lambda vacancy, value: vacancy.published_at == value,
                       'Опыт работы': lambda vacancy, value: vacancy.experience_id == value,
                       'Премиум-вакансия': lambda vacancy, value: vacancy.premium == value,
                       'Идентификатор валюты оклада': lambda vacancy, value: Salary.translate[
                                                                                 vacancy.salary_currency] == value,
                       'Название': lambda vacancy, value: vacancy.name == value,
                       'Название региона': lambda vacancy, value: vacancy.area_name == value,
                       'Компания': lambda vacancy, value: vacancy.employer_name == value}

    # Конструктор для объектов класса Data(данные)
    def __init__(self, file_name, filter_param, sort_param, sort_reverse, sort_range):
        self.file_name = file_name
        self.filter_param = filter_param
        self.sort_param = sort_param
        self.sort_reverse = sort_reverse
        self.sort_range = sort_range
        self.vacancies_objects = []

    # метод читает заданный файл
    def csv_reader(self):
        h = []
        with open(self.file_name, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    h = row
                    csv_h_length = len(row)
                elif '' not in row and len(row) == csv_h_length:
                    self.vacancies_objects.append(Vacancy(dict(zip(h, row))))
        if len(self.vacancies_objects) == 0:
            if len(h) == 0:
                print('Пустой файл')
            else:
                print('Нет данных')
            exit()

    # метод все данные записывает в список
    def get_list_(self):
        return [vacancy.get_list() for vacancy in self.vacancies_objects]

    #метод фильтрует вакансии
    def filter(self):
        if len(self.filter_param) == 0:
            return
        self.vacancies_objects = list(
            filter(lambda vacancy: self.conditions_sort[self.filter_param[0]](vacancy, self.filter_param[1]),
                   self.vacancies_objects))

    #метод сортирует вакансии в нужном порядке
    def sort(self):
        if self.sort_param != '':
            self.vacancies_objects.sort(key=lambda a: getattr(a, DataSet.translate_dictionary[self.sort_param]),
                                        reverse=self.sort_reverse)
        elif self.sort_param == '' and self.sort_reverse:
            self.vacancies_objects.reverse()

    # метод форматирует данные по заданному диапазону
    def get_range(self):
        vacancies_temp = []
        length = len(self.sort_range)
        for index, vacancy in enumerate(self.vacancies_objects):
            if (length > 1 and self.sort_range[0] <= index < self.sort_range[1]) or (
                    length == 1 and self.sort_range[0] <= index) or length == 0:
                vacancy.index = index + 1
                vacancies_temp.append(vacancy)
        self.vacancies_objects = vacancies_temp

#Класс отвечает за обработку параметров вводимых пользователем: фильтры, сортировка, диапазон вывода, требуемые столбцы
class InputConnect:
    #список атрибутов таблицы
    attributs = ['№', 'Название', 'Описание', 'Навыки', 'Опыт работы', 'Премиум-вакансия', 'Компания', 'Оклад',
               'Название региона', 'Дата публикации вакансии']

    # Конструктор для объектов класса InputConnect (входное соединение)
    def __init__(self):
        self.errors = []
        self.file_name = input('Введите название файла: ')
        self.filter_param = self.parse_filter_params(input('Введите параметр фильтрации: '))
        self.sort_param = self.parse_params(input('Введите параметр сортировки: '))
        self.sort_reverse = self.parse_reverse(input('Обратный порядок сортировки (Да / Нет): '))
        self.sort_range = self.parse_range(input('Введите диапазон вывода: '))
        self.table_fields = self.parse_fields(input('Введите требуемые столбцы: '))
        if len(self.errors) != 0:
            print(self.errors[0])
            exit()
        data_set = DataSet(self.file_name, self.filter_param, self.sort_param, self.sort_reverse, self.sort_range)
        data_set.csv_reader()
        data_set.filter()
        data_set.sort()
        data_set.get_range()
        rows = data_set.get_list_()
        if len(rows) == 0:
            print('Ничего не найдено')
        else:
            table = PrettyTable(align='l', field_names=InputConnect.attributs, max_width=20, hrules=1)
            table.add_rows(rows)
            print(table.get_string(fields=self.table_fields))

    # метод обрабатывает параметры фильтрации, введённые пользователем, и выводит ошибку, если данные введены некорректно
    def parse_filter_params(self, filter_param):
        if filter_param == '':
            return []
        if ': ' not in filter_param:
            self.errors.append('Формат ввода некорректен')
            return []
        filter_param = filter_param.split(': ')
        if filter_param[0] not in list(DataSet.conditions_sort.keys()):
            self.errors.append('Параметр поиска некорректен')
            return []
        return filter_param

    #метод обрабатывает порядок сортировки, введённый пользователем, и выводит ошибку при вводе некорректных данных
    def parse_reverse(self, sort_reverse):
        if sort_reverse not in ('', 'Да', 'Нет'):
            self.errors.append('Порядок сортировки задан некорректно')
        return True if sort_reverse == 'Да' else False

    # метод обрабатывает параметры сортировки, введённые пользователем, и выводит ошибку, если данные введены некорректно
    def parse_params(self, sort_param):
        if sort_param not in InputConnect.attributs + ['']:
            self.errors.append('Параметр сортировки некорректен')
        return sort_param

    # метод обрабатывает диапозон сортировки, введённый пользователем, и выводит ошибку, если данные введены некорректно
    def parse_range(self, sort_range):
        return [] if sort_range == '' else [int(limit) - 1 for limit in sort_range.split()]

    #метод обрабатывает поля, введённые пользователем, и выводит ошибку, если данные введены некорректно
    def parse_fields(self, table_fields):
        return InputConnect.attributs if table_fields == '' else ['№'] + [a for a in table_fields.split(', ') if
                                                                        a in InputConnect.attributs]

#метод запускает программу
def get_answer():
    InputConnect()