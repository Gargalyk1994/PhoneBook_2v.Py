import view
import modul
import text

def start():
    while True:
        choice = view.main_menu()# импортируем функцию из view то есть главное меню
        match choice:
            case 1:
                modul.open_pb()# pass - заглушка
                view.print_massage(text.load_succes)
            case 2:
                pass
            case 3:
                pb = modul.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
