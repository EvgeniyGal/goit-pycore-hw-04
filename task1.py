def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                person_data = line.strip().split(",")
                if len(person_data) == 2:
                    try:
                        salary = float(person_data[1])
                        salaries.append(salary)
                    except ValueError:
                        print(
                            f"Неправильне значення заробітної плати: {person_data[1]}"
                        )

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)

        return (total, average)

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


# Приклад використання функції:
cats_info = total_salary("salaries.txt")
print(cats_info)
