import text

def main_menu() -> int: # главное меню
    print(text.main_menu)
    while True:
        choice = input(text.choice_input)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_message(message: str): # ф-ия печатает текст выделением === сверху и снизу
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message)+'\n')

def print_pb(pb: list[dict[str, str]], error: str):
    if pb:
        print('\n' + '=' * 75)
        for i, contact in enumerate(pb, 1):
            print(f'{contact.get("id"):>3}. {contact.get("name"):<30} | {contact.get("phone"):<20} | {contact.get("comment"):<20}')
        print('=' * 75 +'\n')
    else:
        print_message(error)

def input_contact(message: str, cancel: str) -> dict: # принимает строки две и возвращает словарь
    contact = {}
    for key, value in text.input_contact.items():
        data = input(value)
        if data:
            contact[key] = data
        else:
            print_message(cancel)
    return contact

def input_index(message: str, pb: list, error: str) -> int:# удаление по индексу(номеру) контакта
    print_pb(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)
        
# def input_find(pb: dict, message: str, try_again: str):
#     for key, value in pb:
#         if pb.keys == input(message):
#             print(message)
#         else:
#             print_message(try_again)

def input_find(message) -> str:
    return input(message)
           