from abc import ABC, abstractmethod
import requests


class VacancyJobAPI(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def get_vacancies(self, vacancies, count_page):
        pass


class HeadHunterAPI(VacancyJobAPI):
    """ Класс для работы с API HeadHunter"""


    def __init__(self):
        """
        Инициализация класса
        """
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, vacancies, count_page=1):
        """
        Подключение к API  и получени информации о вакансии
        vacancies: ключвое слово для поиска вакансии
        params: параметры поиска
        'text': Текст фильтра. В имени должно быть ключевое слово для поиска
        'page': Индекс страницы поиска на HH
        'area': Поиск ощуществляется по вакансиям города Москва
        'per_page': Кол-во вакансий на 1 странице

        """
        self.vacansies = vacancies
        self.count_page = count_page

        params = {
            'text': f'NAME:{self.vacansies}',
            'area': 1,
            'page': 0,
            'per_page': {count_page}
        }
        response = requests.get(self.url, params=params)

        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансии")

        return response.json()


    def formatted_vacancy(self):
        """
        Обработка данных полученных из API HeadHanter
        возвращает список словарей с вакансиями с ключами:
        "title": название вакансии
        "url": сслыка на вакансию
        "salary_from": зарплата от
        "salary_to": зарплата до
        "requirement": требования
        """
        v = HeadHunterAPI()
        vacansies_hh = v.get_vacancies(self.vacansies, self.count_page)

        vacancy_list = []

        for vac in vacansies_hh['items']:

            vacancy_salary = vac['salary']

            if vacancy_salary == None:
                vacancy_list.append({
                    "title": vac['name'],
                    "url": vac['alternate_url'],
                    "salary_from": 0,
                    "salary_to": 0,
                    "requirement": vac['snippet']['requirement']
                })

            elif vacancy_salary['from'] == None:
                vacancy_list.append({
                    "title": vac['name'],
                    "url": vac['alternate_url'],
                    "salary_from": 0,
                    "salary_to": vacancy_salary["to"],
                    "requirement": vac['snippet']['requirement']
                })

            elif vacancy_salary['to'] == None:
                vacancy_list.append({
                    "title": vac['name'],
                    "url": vac['alternate_url'],
                    "salary_from": vacancy_salary["from"],
                    "salary_to": 0,
                    "requirement": vac['snippet']['requirement']
                })

            else:
                vacancy_list.append({
                    "title": vac['name'],
                    "url": vac['alternate_url'],
                    "salary_from": vacancy_salary["from"],
                    "salary_to": vacancy_salary["to"],
                    "requirement": vac['snippet']['requirement']
                })


        return vacancy_list


class SuperJobAPI(VacancyJobAPI):
    """ Класс для работы с API SuperJob"""

    def __init__(self):
        """
        Инициализауия класса
        """
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {
            'X-Api-App-Id': 'v3.r.137574612.de937b6deb3e4f84715320b9257a669c7fee8118.c8d35ae04539d8545d3bd1744be1abe492473689'
        }


    def get_vacancies(self, vacancies, count_page=1):
        """
        Подключение к API  и получени информации о вакансии
        params: параметры поиска
        'keyword', vacancies: ключвое слово для поиска вакансии
        """
        self.vacansies = vacancies
        self.count_page = count_page

        params = {
            'keyword': vacancies,
            'count': {self.count_page},
        }

        response = requests.get(self.url, headers=self.headers, params=params)

        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансии")

        return response.json()


    def formatted_vacancy(self):
        """
        Обработка данных полученных из API HeadHanter
        возвращает список словарей с вакансиями с ключами:
        "title": название вакансии
        "url": сслыка на вакансию
        "salary_from": зарплата от
        "salary_to": зарплата до
        "requirement": требования
        """
        vs = SuperJobAPI()
        vacansies_js = vs.get_vacancies(self.vacansies, self.count_page)

        vacancy_list = []

        for vacancy in vacansies_js['objects']:
            vacancy_salary_from = vacancy['payment_from']
            vacancy_salary_to = vacancy['payment_to']

            if vacancy_salary_from == 0 and vacancy_salary_to == 0:
                vacancy_list.append({
                "title": vacancy['profession'],
                "url": vacancy['link'],
                "salary_from": 0,
                "salary_to": 0,
                "requirement": vacancy['candidat']
                })

            elif vacancy_salary_from == 0:
                vacancy_list.append({
                "title": vacancy['profession'],
                "url": vacancy['link'],
                "salary_from": 0,
                "salary_to": vacancy['payment_to'],
                "requirement": vacancy['candidat']
                })

            elif vacancy_salary_to == 0:
                vacancy_list.append({
                "title": vacancy['profession'],
                "url": vacancy['link'],
                "salary_from": vacancy['payment_from'],
                "salary_to": 0,
                "requirement": vacancy['candidat']
                })

            else:
                vacancy_list.append({
                "title": vacancy['profession'],
                "url": vacancy['link'],
                "salary_from": vacancy['payment_from'],
                "salary_to": vacancy['payment_to'],
                "requirement": vacancy['candidat']
                })

        return vacancy_list