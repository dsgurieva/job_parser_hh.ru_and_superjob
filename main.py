from src.json_saver import JSONSaver
from src.job_vacancy import HeadHunterAPI, SuperJobAPI


def main():

    # Создание экземпляров класса HeadHunterAPI, SuperJobAPI
    hh_vacansies = HeadHunterAPI()
    sj_vacansies = SuperJobAPI()

    while True:

        print(f"Введите платформу с которой хотите осуществить запрос: \n"
            f"1 - HeadHunter \n"
            f"2 - SuperJob ")

        # Ввод значений пользователем
        user_job_platform = input()

        if not user_job_platform.isdigit():
            print('Введите цифру')

        # Получение списка вакансий с платформы hh.ru по ключевому слову, отсартирванных по возрастанию
        if user_job_platform == "1":
            top_n = int(input("Введите количество вакансий для вывода: "))
            keyword = input("Введите ключевое слово для поиска: ")
            print("Вакансии отсартированы по возрастанию")

            # Получение вакансий и их форматирование
            hh_vacansies.get_vacancies(keyword, top_n)
            formatted_vacancy = hh_vacansies.formatted_vacancy()

            # Создание экземпляра класса JSONSaver сохранение в файл и сортировка по возрастанию
            js = JSONSaver()
            js.add_vacancy(formatted_vacancy)
            sorted_vacancy = js.sorted_vacancies_by_salary()

            for i in range(len(sorted_vacancy)):
               print(sorted_vacancy[i])
               print()

            break

        # Получение списка вакансий с платформы superjob по ключевому слову, отсартирванных по возрастанию
        if user_job_platform == "2":
            top_n = int(input("Введите количество вакансий для вывода: "))
            keyword = input("Введите ключевое слово для поиска: ")
            print("Вакансии отсартированы по возрастанию заработной платы")

            # Получение вакансий и их форматирование
            sj_vacansies.get_vacancies(keyword, top_n)
            formatted_vacancy = sj_vacansies.formatted_vacancy()

            # Создание экземпляра класса JSONSaver сохранение в файл и сортировка по возрастанию
            js = JSONSaver()
            js.add_vacancy(formatted_vacancy)
            sorted_vacancy = js.sorted_vacancies_by_salary()

            for i in range(len(sorted_vacancy)):
                print(sorted_vacancy[i])
                print()

            break


if __name__ == "__main__":
    main()
