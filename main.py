prompt = "Type show, add, edit or remove (type 12345 to exit program): "
user_text = []

while True:
    user_input = input(prompt)
    user_input = user_input.strip()

    match user_input:
        case 'add':
            add = input("Please enter to do: ")
            add = add.strip()
            user_text.append(add)
            print("Current to do list is:")
            for text in user_text:
                print(text)
        case 'show' | 'display':
            if len(user_text) == 0:
                print("List is empty!")
            else:
                print("Current to do list is:")
                for text in user_text:
                    i = 1
                    print(i, text)
                    i+=1
        case 'remove':
            remove = input("What to do would you like to remove?")
            remove = remove.strip()
            if remove in user_text:
                user_text.remove(remove)
                print("Removed", remove, "from to do list.")
            else:
                print("To do does not exist in list!")
        case 'edit':
            user_edit = input("What item would you like to edit?")
            
        case '12345':
            if len(user_text) == 0:
                print("The list is empty...bye")
            else:
                print("final to do list is:")
                for text in user_text:
                    print(text)
                print("\nbye!")
            break
        case whatever:
            print("You entered an unknown command, try again.")


   













