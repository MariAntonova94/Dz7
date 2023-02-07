import model
import view
 

def start():
    user_choice = 0
    while user_choice == 8:
        user_choice = view.main_menu()
        
        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.save_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
            case 5:
                model.update_user()
                view.update_user() 
            case 6:
                model.delete_user()
                view.delete_user()      
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)

