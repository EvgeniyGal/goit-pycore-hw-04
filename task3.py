import sys
from pathlib import Path
from colorama import init, Fore, Style


def print_directory_structure(directory, prefix=""):
    for path in sorted(directory.iterdir()):
        if path.is_dir():
            print(f"{prefix}{Fore.BLUE}{path.name}{Style.RESET_ALL}")
            print_directory_structure(path, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: task3.py <шлях_до_директорії>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Шлях {directory_path} не існує.")
        return

    if not directory_path.is_dir():
        print(f"{directory_path} не є директорією.")
        return

    print(f"Структура директорії {directory_path}:\n")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
