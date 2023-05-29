phone_book = []
path = 'phone_book.txt'#путь к тел книге

def open_pb():
    global phone_book, path
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone': contact[1], 'address':contact[2]}) 

def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book  