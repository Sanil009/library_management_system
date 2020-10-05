def user_request():
    sort=True
    while sort==True:
        try:
            import book_detail
            book_detail.display()
            print("Please press (1) for borrowing books.")
            print("Please press (2) for returing books.")
            print("Please press (3) to exit.")
            user_input=int(input())
            import read
            if user_input==1:
                read.borrow_()              
            elif user_input==2:
                read.return_()                
            elif user_input==3:
                 sort=False
                 print("Thank you")
            elif user_input<1 or user_input>3:
                print("Please enter (1 or 2 or 3)")
                sort=True
        except:
            print("Invalid input")
            print("Please enter a valid number")
            sort=True

user_request()


