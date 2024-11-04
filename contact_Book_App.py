#empty dictionary
contacts = {}
while True:
    print('\ncontact book app')
    print('1. create contact  ')
    print('2. view contact ')
    print('3. update contact ')
    print('4. delete ccontact ')
    print('5. search contact')
    print('6. count contact ')
    print('7. exist ')


    choice = input('enter your choice =')

    if choice == '1':
        name = input('enter your name ')
        if name in contacts:
            print(f'contact name {name} already exist!')
        else:
            age = input('enter age =')
            email = input('enter email = ')
            mobile = input('enter mobile number =')
            contacts [name] = {'age': int(age), 'email':email, 'mobile':mobile}
            print(f'contact{name} has been created sussesfully')

    elif choice == '2':
        name = input('enter contact name to view =')
        if name in contacts:
            contact = contacts[name]
            print(f'name: {name}, age:{age}, mobile number:{mobile}')
        else:
            print('contact not found')


    elif choice  == '3':
        name = input('enter name to update contact')
        if name in contacts:
            age = input('enter updated age =')
            mobile  = input('enter updated mobile number =')
            email = input('enter update email =')
            contacts[name ] = {'age': int(age), 'email':email, 'mobile':mobile}
        else:
            print('contact not found1 ')


    elif choice =='4':
        name = input('enter name to delete =')
        if name in contacts:
            del contacts[name]
            print(f'contact name {name} has been deleted succesfully')
        else:
            print('contact not found')


    elif choice == '5':
        search_name = input('enter contact name to search')
        found = False 
        for name, contact in contacts.items():
            if search_name. lower() in name.lower():
                print(f'found - name{name}, age:{age}, mobile number:{mobile}, email:{email}')
                found = True
        if not found:
            print('no contact name found with that name')

    elif choice =='6':
        print(f'total contacts in your book : {len(contacts)}') 

    elif choice =='7':
        print('good bye...closing the program ')
        break

    else:
        print('invalid input')