from pathlib import Path
import sort_folder

# import phone_book
# import note_book


def run_folder():
    folder_path = input("Введіть шлях до теки для сортування: ")
    sort_folder.main(Path(folder_path))


bot_command_dict = {
    # "1": phone_book,
    # "2": note_book,
    "3": run_folder,
}


def assistant_bot():
    print("Вас вітає персональний помічник FriendlyHandbook")
    print(
        """
    Виберіть одну з наступних опцій:
    - Книга контактів (PhoneBook) -> Натисніть '1'
    - Нотатки (NoteBook) -> Натисніть '2'
    - Сортувач папок (CleanFolder) -> Натисніть '3'
    - Вийти з помічника -> Натисніть '0'
    """
    )

    while True:
        command = input("Введіть номер опції (від 0 до 3): ").strip()

        if command == "0":
            raise SystemExit("\nДо побачення!\n")

        elif command in bot_command_dict.keys():
            handler = bot_command_dict[command]
            answer = handler()
            print(answer)

        else:
            print("Некоректне число. Будь ласка, введіть число від 0 до 3")


if __name__ == "__main__":
    assistant_bot()
