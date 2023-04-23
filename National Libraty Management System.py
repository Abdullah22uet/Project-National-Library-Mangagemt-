# National Library Management System 
# before running this code you have to install "pyttsx3" module
import pyttsx3
dic,count,rent = {},0,[]
engine = pyttsx3.init()
engine.say("Welcome to National Library Management System. This system is developed by abdullah khan")
engine.runAndWait()
while 1:
    print("""\n <----- National Library Management System ----->
    Press 1 : Add books in library
    Press 2 : Show all(no of) books in library
    Press 3 : Search books in library 
    Press 4 : Giving books to rent
    Press 5 : Return books from rent
    Press 6 : Delete books from library
    Press 7 to exit""")
    
    try:
        uc = int(input("\n\tEnter your choice: "))
        
        # user choice 1
        if uc==1:
            x = int(input("\n\t\tEnter number of books you want to add --> "))
            for i in range(x):
                count+=1
                print("\t\t",count)
                book_n = str(input("\t\t\tEnter name for book --> "))
                if book_n in dic:
                    count-=1
                    print("\t\t\tBook is already available with this name")
                    engine = pyttsx3.init()
                    engine.say("Book is already available in library with this name")
                    engine.runAndWait()
                    break
                book_loc = str(input("\t\t\tEnter location for book --> "))
                dic[f"{book_n}"] = f"{book_loc}"
        
        # user choice 2
        elif uc==2:
            print("\n\t\t Total number of books --> ",count)
            for i in dic:
                print("\t\t",i)
        
        # user choice 3
        elif uc==3:
            search_book = str(input("\n\t\tEnter name of book : "))
            for book in dic:
                if book == search_book:
                    print("\t\t\tBook (",search_book ,") is available at location : ",dic[book])
                    break
            else:
                print("\t\t\tBook is not available in library")
                engine = pyttsx3.init()
                engine.say("Book is not available in library")
                engine.runAndWait()
                        
        # user choice 4
        elif uc == 4:
            search_b = str(input("\n\t\tEnter the name of book --> "))
            if search_b in rent:
                print("\t\t\tBook (",search_b,") is already on rent")
                engine = pyttsx3.init()
                engine.say("Book is already on rent")
                engine.runAndWait()
            elif search_b in dic:
                rent.append(search_b)
                print("\t\t\t Now book (",search_b,") is on rent")
            else:
                print("\t\t\t Book (",search_b,") is not available in library")
                engine = pyttsx3.init()
                engine.say("Book is not available in library")
                engine.runAndWait()
        # user choice 5
        elif uc == 5:
            search_return = str(input("\n\t\tEnter the name of book --> "))
            if search_return in rent:
                if search_return not in dic:
                    rent.remove(search_return)
                    print("\t\t\tThis book (", search_return, ") was deleted from library record. It was on rent. Now book successfully returned but not exist in library anymore.")
                    engine = pyttsx3.init()
                    engine.say("Book successfully returned but \n not available in library anymore.")
                    engine.runAndWait()
                else:
                    rent.remove(search_return)
                    print("\t\t\tBook (", search_return, ") successfully returned")
                    engine = pyttsx3.init()
                    engine.say("Book successfully returned")
                    engine.runAndWait()
            elif search_return not in rent:
                print("\t\t\tBook is not on rent. It seems that you did not put book on rent.")
            elif search_return not in dic:
                print("\t\t\tBook (", search_return, ") is not in the library.")
                engine = pyttsx3.init()
                engine.say("Book is not available in library.")
                engine.runAndWait()
        # user choice 6
        elif uc == 6:
            search_delete = str(input("\n\t\tEnter name of book --> "))
            if search_delete in dic:
                count-=1
                dic.pop(search_delete)
                print("\t\t\t Book (",search_delete,") successfully deleted")
                engine = pyttsx3.init()
                engine.say("Book successfully deleted")
                engine.runAndWait()
            else:
                print("\t\t\t Book (",search_delete,") is not available in library")
                engine = pyttsx3.init()
                engine.say("Book is not available in library")
                engine.runAndWait()
        # user choice 7
        elif uc == 7:
            print("\n\t\tSuccessfully exit from library")
            engine = pyttsx3.init()
            engine.say("Successfully exit")
            engine.runAndWait()
            break    
        
        # else case
        else:
            print("Invalid choice. Kindly enter your choice again between (1 to 7) according to menu")
    except:
        print("Kindly enter your choice again between (1 to 7) according to menu")    
# end of code        