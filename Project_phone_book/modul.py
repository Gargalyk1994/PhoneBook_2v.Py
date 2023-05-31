class PhoneBook:
    
    def __init__(self, path: str ='phone_book.txt') -> None:
        self.phone_book: list[dict[str, str]] = []
        self.path = path#путь к тел книге
        self.last_id = 0
    
    
    def open(self):
        with open (self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            new = {'id': contact[0], 'name':contact[1], 'phone': contact[2], 'comment':contact[3]}
            self.phone_book.append(new) 

    def save(self):
        data = []
        for contact in self.phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open (self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))   

    def load(self) -> list[dict[str, str]]:
        return self.phone_book

    def add(self, new: dict[str, str]):
        self.last_id += 1
        new['id'] = str(self.last_id)
        self.phone_book.append(new)
        return new.get('name')

    def find(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self.phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result
    
    def change(self, new: dict, index: int) -> str:
        for contact in self.phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')
    
    def delete(self, index: int):
        return self.phone_book.pop(index-1).get('name')
