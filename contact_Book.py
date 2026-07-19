contacts = {}

while True:

    print("_____MENU______")
    print("1. Add Contact \n2.View Contact \n3.Search Contact \n4.Delete Contact \n5.Exit\n")
    choice= int(input("Enter your Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        number = int(input("Enter phone number: "))
        contacts[name] = number
        print("Contact added successfully")


    elif choice == 2:
        for name, number in contacts.items():
            print(name,"-",number)

    elif choice == 3:
        search_name = input("Search Contact: ")
        for name in contacts:
            if name == search_name:
                print("Contact Found")
                print(name,"-",number)
                break
            else:
                print("not found")
    
    elif choice == 4:
        delete_name = input("Search Contact: ")
        for name in contacts:
            if name == delete_name:
                del contacts[delete_name]
                print("Conatct deleted succesfully")
                break
    
    elif choice == 5:
        exit()

    else:
        print("Invalid Choice")
