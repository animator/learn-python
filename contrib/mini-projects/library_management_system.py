# importing pandas library 
import pandas as pd

#function for adding books to library
def addBook():
    choice= input("Do you want to add books to library?(yes/no)")
    if choice=='yes' or choice=='Yes':
            n= input("Enter name of book: ")
            a= input("Enter the name of author: ")
            copy=input("Enter number of copies: ")
            category= input("Enter category: ")
            # converting data entered into a dataframe
            df=pd.DataFrame( {'Author':a,'No_of_Copies':copy,'Book_Name':n,'Category':category},index=[1])
            # Adding data to existing csv
            df.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",mode = 'a',index=False,header=False)
            # Creating a dataframe after addition
            df = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    elif(choice=='no' or choice=='No'):
        print("Addition program terminated")
    print("record saved successfully.")
    print(df)

#function for issuing a book from the library
def issueBook():
    df1 = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    bookName = input("Enter the book Name to be Issued: ")
    # df2 another Dataframe to store the entered book
    df2 =  df1[df1.Book_Name == bookName]   
    # df1 same Dataframe storing all other books other than the entered one
    df1 = df1[df1.Book_Name != bookName]
    df1.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
    if df2.empty:
        print("book doesn't exist")
    elif int(df2.No_of_Copies) > 0:
        df2.No_of_Copies = df2.No_of_Copies-1
        print("Book issued: ")
    else:
        print("book doesn't exist")
    df2.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",mode='a',index=False,header=False)
    print(df2)
    
# function to submit book to library 
def submitBook():
    df1 = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    bookName = input("Enter the book Name to Submit:- ")
    df2 =  df1[df1.Book_Name == bookName]
    df1 = df1[df1.Book_Name != bookName]
    df1.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
    if df2.empty:
        print("Book doesn't exists in the system, please add this book ")
        addBook()  
    else:
        df2.No_of_Copies = df2.No_of_Copies+1
        print("Book Submitted Successfully")
    df2.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",mode='a',index=False,header=False)
    print(df2)

# function for deleting a book from the library
def deleteBook():
    df = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    bookName = input("Enter the book Name to delete:- ")
    dff =  df[df.Book_Name == bookName]
    df = df[df.Book_Name != bookName]
    df.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
    if dff.empty:
        print("book doesn't exist")
    else:
        df.drop(df.index[df['Book_Name']==bookName],inplace=True)
        df.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
        print(df)
    
#function to search whether a book is available in the library or not
def SearchBook():
    df3 = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    c= input("Search by Author Name (A) /Book Name (B).....enter A/B:- ")
    if(c=='B' or c=='b'):
        bookName = input("Enter the book Name to be searched: ")
        df4 =  df3[df3.Book_Name == bookName]
        df3.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
        if df4.empty:
            print("book doesn't exist")
        else:
            print(df4)
    if(c=='A' or c=='a'):
        auth= input("Enter name of the author to be searched:- ")
        af2 =  df3[df3.Author == auth]
        df3.to_csv(r"C:\Users\aditi bansal\Desktop\records.csv",index=False)
        if af2.empty:
            print("book doesn't exist")
        else:
            print(af2)
    
# function to display books
def displayBook():
    df = pd.DataFrame(pd.read_csv(r"C:\Users\aditi bansal\Desktop\records.csv"))
    print(df.iloc[:,[0,1]])
    
ch = 'yes'
while ch == "yes" or ch == 'Yes': 
    print("Library Management System")
    print("1-ADD BOOK") 
    print("2-ISSUE BOOK") 
    print("3-SUBMIT BOOK") 
    print("4-DELETE BOOK")  
    print("5-SEARCH BOOK")
    print("6-DISPLAY BOOK")  
    choice=int(input("Enter task number: "))
    if(choice==1):
        addBook()
    elif(choice==2):
        issueBook()
    elif(choice==3):
        submitBook()
    elif(choice==4):
        deleteBook()
    elif(choice==5):
        SearchBook()
    elif(choice==6):
        displayBook()
    else:
        print("Wrong choice...")
    ch = input("Enter Yes/yes if you want to do more operations: ")
