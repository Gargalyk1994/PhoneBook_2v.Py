import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.choice_input)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_massage(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message)+'\n')

def print_contact(pb: list[dict[str, str]], error: str):
    if pb:
        print('\n' + '=' * 72)
        for i, contact in enumerate(pb, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("address"):<20}')
        print('=' * 72 +'\n')
    else:
        print(error)
           