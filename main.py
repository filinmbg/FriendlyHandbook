# import address_book
# import notes_book
import sort_folder
from pathlib import Path


while True:
    print("Меню:")
    print("1. Вибір 1")
    print("2. Вибір 2")
    print("3. Вибір 3")
    print("0. Вихід")

    choice = input("Введіть номер вибору: ")
    
    if choice == "1":
        # address_book.main()
        print("Ви обрали варіант 1")
    elif choice == "2":
        # notes_book.main()
        print("Ви обрали варіант 2")
    elif choice == "3":
        folder_path = input("Введіть шлях до теки для сортування: ")
        sort_folder.main(Path(folder_path))
        print("Ви обрали варіант 3")
    elif choice == "0":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Введіть 1, 2, 3 або 0 для виходу.")