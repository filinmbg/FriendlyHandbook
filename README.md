# Персональний помічник – Friendly Handbook

## Опис

Персональний помічник - це корисна програма з інтерфейсом командного рядка, яка містить контактну книгу, нотатки та може аналізувати папки.
Friendly Handbook вміє:

- зберігати контакти з номером телефону, ім’ям, електронною поштою, датою народження до своєї Книги контактів;
- змінювати та видаляти контакти;
- знаходити контакти за іменами;
- створювати нотатки та працювати з ними (пошук, редагування, видалення, сортування);
- додавати нотатки з тегами;
- сортувати файли у зазначеній папці за категоріями (зображення, документи, відео та ін.).

## Встановлення

Щоб встановити програму потрібно зайти у теку де знаходиться установчий пакет та у командному рядку ввести **pip install**.
Щоб перевірити наявность: команда **pip list**

## Запуск персонального помічника

В командному рядку необхідно ввести команду assistant_bot
pip install -i https://test.pypi.org/simple/ goit-team_project-FriendlyHandbook==1.0.0

## Інструкція для користувача

Відкрийте Персональний помічник та виберіть категорію:

- Книга контактів (PhoneBook)
- Нотатки (NoteBook)
- Сортувач папок (CleanFolder)

  Після цього можуть бути використані наступні команди:
  | Команди | Аргументи | Результат |
  |---------|:---------:|-----------|
  | help | - | Показати список усіх команд |
  | hello | - | Почати роботу з помічником |
  | add contact | - | Додати новий контакт до Книги контактів |
  | add phone | name, phone | Додати номер телефону до існуючого контакту чи створити новий контакт з телефоном |
  | add email | name, email | Додати електронну пошту до існуючого контакту чи створити новий контакт з електронною поштою |
  | add birthday | name, birthday | Додати чи змінити день народження до існуючого контакту чи створити новий контакт з днем народження |
  | change phone | name, old phone, new phone | Змінити номер телефону вказаного контакту |
  | change email | name, old email, new email | Змінити електронну пошту вказаного контакту |
  | change birthday | name, old birthday, new birthday | Змінити день народження вказаного контакту |
  | delete contact | name | Видалити контакт за вказаним ім’ям з Книги контактів |
  | delete phone | name, phone | Видалити номер телефону контакту з Книги контактів |
  | delete email | name, email | Видалити електронну пошту контакту з Книги контактів |
  | delete birthday | name, birthday | Видалити день народження контакту з Книги контактів |
  | get birthday | days | Показати в кого день народження через введену кількість днів |
  | show all | - | Показати всі контакти з Книги контактів |
  | find name | name | Знайти контакт |
  | exit, close, goodbye | - | Закінчити роботу або повернутися в головне меню |

Команди для нотатків (NoteBook):
| Команда | Результат |
|---------|-----------|
| help | Показати список всих команд |
| add note | Створити новий нотаток та зберегти в папку «Нотатки» |
| read note | Відкрити нотаток та прочитати текст з нього |
| delete note | Видалити нотаток з папки |
| find by tag | Знайти всі нотатки за вказаним тегом |
| find by name | Знайти всі нотатки за вказаним ім’ям |
| show all notes | Показати список контактів, які збереженні в папці |
| add tag | Додати тег до існуючого нотатку |
| add text | Додати текст до існуючого нотатку |
| change tag | Змінити тег існуючого нотатку |
| change text | Змінити текст існуючого нотатку |
| delete tag | Видалити тег |
| delete text | Видалити текст |
| close | Закінчити роботу з Нотатками |

## Наша команда

- Team Lead: Олександр Юха
- Scrum Master: Олександр Куспис
- Python Developers: Іван Марковський, Олександр Кострицький, Олександр Коваленко
