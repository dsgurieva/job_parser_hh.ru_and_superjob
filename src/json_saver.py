from operator import itemgetter
from vacancy import Vacancy
import json


class JSONSaver():

    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        """
        Добавление вакансии в файл, созхранение в формате словаря с ключом 'data'
        и списком словарей с вакансиями
        """
        self.vacancy = vacancy
        with open('vacancy.json', "w", encoding="utf-8") as file:
            data = {"data": self.vacancy}
            json.dump(data, file)



    def sorted_vacancies_by_salary(self):
        """
        Сортировка вакансий по возрастанию зарплаты и создание списка вакансий
        с экземплярами класса Vacancy
        """

        with open('vacancy.json', 'r', encoding='utf-8') as file:
            data = json.load(file)['data']

        s_data = sorted(data, key=itemgetter('salary_from'))
        sorted_data = [Vacancy(x) for x in s_data]

        return sorted_data



    def delete_vacancy(self):
        """ Удаление вакансий по ключу 'data'"""
        with open('vacancy.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        data.pop('data')

        with open('vacancy.json', 'w', encoding="utf-8") as file:
            json.dump(data, file)