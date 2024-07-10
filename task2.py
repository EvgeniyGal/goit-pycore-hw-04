#
def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_info = []
            for line in file:
                cat_data = line.strip().split(",")
                if len(cat_data) == 3:
                    cat_id, name, age = cat_data
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


# Приклад використання функції:
cats_info = get_cats_info("cats-data.txt")
print(cats_info)
