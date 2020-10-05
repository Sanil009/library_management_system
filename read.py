def read(): #creating a dictionary to record all the data
    counter=1
    book_read={}
    file=open("Dict.txt","r") #for opening Dict.txt file     
    for line in file: #for reading each line and displaying text to the user
        book_read[counter]=line.replace("\n","").split(",")
        counter=counter+1
    print(book_read)
    return book_read


def borrow_(): #for borrowing the books
    book_id=read() #calling read function
    sorted = False
    while sorted==False:
        sn=int(input("Enter the S.N of the book you like to borrow: "))
        if sn>0 and sn<=len(book_id[2]):
            print(book_id[sn])
            print("Book details are as follows: ")
            print("Book Name: ",book_id[sn][0],"\nAuthor Name: ",book_id[sn][1],"\nQuantity: ",book_id[sn][2],"\nPrice: ",book_id[sn][3])      
            sort=False
            while sort==False:
                ask=input("Is this your book?(y/n)")
                if ask=="n":
                    ans=False
                    while ans==False:
                        var=input("Do you want to exit?(y/n)")
                        if var=="y":
                            sort=True
                            sorted=True
                            ans=True
                        elif var=="n":
                            sort=True
                            ans=True
                        else:
                            print("Enter (y/n)")
                elif ask=="y":
                    if int(book_id[sn][2])==0:
                                print(book_id[sn][0],"is not availabale.")
                                sort=True
                                sorted=True
                    else:
                        sort1=True
                        while sort1==True:        
                            quant=int(input("How many books do you want to borrow?"))
                            if quant>0 and quant<=int(book_id[sn][2]):
                                book_id[sn][2]=str(int(book_id[sn][2])-quant)
                                print(book_id[sn])
                                name=str(book_id[sn][0])
                                author=str(book_id[sn][1])
                                price=str(book_id[sn][3])
                                import bill #this imports bill.py
                                bill.bill_(sn,book_id,name,author,quant,price) #for calling bill_ function with argument passed for filling process
                                sort1=False
                                sort=True
                                sorted=True
                                print("Thank you")
                                print(book_id)
                                filea=open("Dict.txt","w") #this opens Dict.txt for updating the text
                                for i,j in book_id.items():
                                    for k in j:
                                        filea.write(str(k)+",")
                                    filea.write("\n")
                            elif quant<0 or quant>int(book_id[sn][2]):
                                   print(book_id[sn][2])
                                   print("Invalid")
                else:
                    print("Enter(y/n)")
        else:
            print("Invalid")

    print("Thank you")
        


def return_():
    #for returning the books
    book_id=read()
    sorted=False
    while sorted==False:
        
        sn=int(input("Enter the S.N of the book you want to return: "))
        if sn>0 and sn<=len(book_id):
            
            print("Book details are as follows")
            print("Book name: ",book_id[sn][0],"\nAuthor Name: ",book_id[sn][1],"\nQuantity: ",book_id[sn][2],"\nPrice: ",book_id[sn][3])
            sort=False
            while sort==False:
                ask=input("Is this your book?(y/n)")
                if ask=="n":
                    
                    ans=False
                    while ans==False:
                        var=input("Do you want to exit?(y/n)")
                        if var=="n":
                            sort=True
                            ans=True
                        elif var=="y":
                            sort=True
                            sorted=True
                            ans=True
                        else:
                            print("Enter(y/n)")
                elif ask=="y":
                    sort1=False
                    while sort1==False:
                        quant=int(input("How many books do you want to return? "))
                        if quant<=0:
                            print("Invalid")
                        else:
                            book_id[sn][2]=str(int(book_id[sn][2])+quant)
                            sort1=True
                            sort=True
                            sorted=True
                            name=str(book_id[sn][1])
                            author=str(book_id[sn][1])
                            price=str(book_id[sn][3])
                            import bill #for importing bill.py
                            bill.return_(sn,book_id,name,author,quant,price) #for calling return_ fuction with argument passed for filling process
                            print("Thank you")
                            filea=open("Dict.txt","w") #for opening Dict.txt file for updating the text
                            for i,j in book_id.items():
                                for k in j:
                                    filea.write(str(k)+",")
                                filea.write("\n")
                else:
                    print("Enter(y/n)")
        else:
                print("Invalid")
