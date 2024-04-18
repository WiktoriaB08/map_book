from models.data import users
from utils.crud import show_users,add_new_user,search_user,remove_user






if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("Menu:")
        print("0. Zakończ program")
        print("1. Wyświetl co u znajomych")
        print("2. Dodaj użytkownika")
        print("3. Zbajdz użytkownika")
        print("4. Usuń użytkownika")
        menu_option: str = input("dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
           add_new_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)



