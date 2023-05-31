import view
import modul
import text

def start():
    my_pb = modul.PhoneBook()
    while True:
        choice = view.main_menu()# импортируем функцию из view то есть главное меню
        match choice:
            case 1:
                my_pb.open()# pass - заглушка
                view.print_message(text.load_succes)
            case 2:
                my_pb.save()
                view.print_message(text.save_succes)
            case 3:
                pb = my_pb.load()
                view.print_pb(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_contact)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_succes(name))
            case 5:
                key_word = view.input_find(text.input_change)
                result = my_pb.find(key_word)
                view.print_pb(result, text.f_contact(key_word))
            case 6:
                key_word = view.input_find(text.change_contact)
                result = my_pb.find(key_word)
                if result:
                    if len(result) != 1:
                        view.print_pb(result, '')
                        current_id = view.input_find(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    new_contact = view.input_contact(text.change_contact, text.cancel_contact)
                    name = my_pb.change(new_contact, current_id)
                    view.print_message(text.change_succes(name))
                else:
                    view.print_message(text.not_find)
            case 7:
                pb = my_pb.load()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = my_pb.delete(index)
                view.print_message(text.del_contact(name))
            case 8:
                break
