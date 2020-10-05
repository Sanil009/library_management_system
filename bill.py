def bill_(sn,book_id,name,author,quant,price):
    import datetime
    from datetime import timedelta
    expirydate=(datetime.datetime.now()+timedelta(days=10)).strftime("%Y-%M-%D")
    todaydate=datetime.datetime.today()
    now=datetime.datetime.now()
    name=input("Full name: ")
    fileb=open("bill.txt","w")
    fileb.write("S.N: "+str(sn))
    fileb.write("Full Name: "+name+"\n")
    fileb.write("Book Name: "+book_id[sn][0]+"\n")
    fileb.write("Book Author: "+author+"\n")
    fileb.write("Quantity borrowed: "+str(quant)+"\n")
    fileb.write("Price: "+book_id[sn][3]+"per unit"+"\n")
    fileb.write("Total price: $"+str(quant*float(book_id[sn][3].replace("$",""))))
    fileb.write("Date: "+str(todaydate)+"\n")
    fileb.write("Time: "+str(now.strftime("%H:%M:%S"))+"\n")
    fileb.write("")

def return_(sn,book_id,name,author,quant,price):
    import datetime
    todaydate=datetime.datetime.today()
    now=datetime.datetime.now()
    name1=input("Full Name: ")
    sorted=False
    while sorted==False:
        try:
            days=int(input("Days borrowed: "))
            sorted=True
        except:
            print("Invalid")
    filer=open("returned book.txt","a")
    filer.write("S.N: "+str(sn)+"\n")
    filer.write("Full Name: "+name1+"\n")
    filer.write("Book name: "+book_id[sn][0]+"\n")
    filer.write("Book author: "+book_id[sn][1]+"\n")
    filer.write("Quantity returned: "+str(quant)+"\n")
    filer.write("Date: "+str(todaydate)+"\n")
    filer.write("Time: "+str(now.strftime("%H:%M:%S"))+"\n")
    if days<1:
        print("Invalid")
    else:
        extra = days-10
        filer.write("Fine: $2 per day"+"\n")
        filer.write("Extra days: "+str(extra)+"\n")
        filer.write("Total: "+"$"+str(extra*2)+"\n")
    filer.write("")