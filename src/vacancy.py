class Vacancy():
    """ Класс для работы с вакансиями"""


    def __init__(self, vacancies):
        """
        Инициализатор класса Vacancy
        """
        self.title = vacancies['title']
        self.url = vacancies['url']
        self.salary_from = vacancies['salary_from']
        self.salary_to = vacancies['salary_to']
        self.requirement = vacancies['requirement']

    def __str__(self):
        """
        :return: возвращает данные в формате строки
        """
        if not self.salary_from and not self.salary_to:
            salary = "Заработная плата не указана"
        elif not self.salary_from:
            salary = self.salary_to
        elif not self.salary_to:
            salary = self.salary_from
        else:
            salary = f"{self.salary_to}-{self.salary_to}"

        return f"{self.title} \n" \
               f"{self.url} \n" \
               f"{salary} \n" \
               f"{self.requirement}"