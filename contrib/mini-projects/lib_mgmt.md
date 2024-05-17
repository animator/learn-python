# Library Management System

This project is a library management system coded in Anaconda using Jupyter Notebook, Python pandas, and CSV. It focuses on basic library operations such as adding new books, issuing and submitting books, searching books by author or title, and deleting unnecessary records.

## Main Functions

### Adding New Book
- **Functionality:** Adds new books to the library.
- **Input:** Book details including title, author, etc.
- **Output:** Updates the library database with the new book information.

### Issuing a Book
- **Functionality:** Allows users to borrow books.
- **Input:** Book details and borrower information.
- **Output:** Records the book loan in the system.

### Submitting Issued Book
- **Functionality:** Facilitates the return process for borrowed books.
- **Input:** Returned book details.
- **Output:** Updates the library database to reflect the returned book.

### Deleting a Record
- **Functionality:** Removes unnecessary records from the system.
- **Input:** Book details to be deleted.
- **Output:** Deletes the specified record from the library database.

### Searching a Specific Record
- **Functionality:** Enables users to search for books by author or title.
- **Input:** Search query (author name, book title, etc.).
- **Output:** Displays matching records found in the library database.

### Displaying the Records
- **Functionality:** Shows all records currently stored in the library database.
- **Output:** Displays a comprehensive list of all books available in the library.

This project provides essential functionality for managing library operations efficiently.

## Hardware Requirements
1. **Operating System:** Windows 10
2. **Processor:** Intel(R) Pentium(R) CPU J2900 @ 2.41GHz 2.41 GHz
3. **RAM:** 4.00 GB
4. **System Type:** 64-bit operating system, x64-based processor

## Software Requirements
1. **Anaconda Navigator (Anaconda 3):**
   - Jupyter Notebook (Python)

2. **Other Tools:**
   - Notepad and Excel (For CSV)
  
## CSV File used
![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/fc6f495e-d289-4d88-a2f1-a43983104803)

## Source Code

```python
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
```
## Output:

Choice 1
ADD BOOK- The record of the book is added
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/a9aa10d1-fc13-4c81-85c7-5efb703c08c1)

Choice 2
ISSUE BOOK- Number of copies of that particular book is reduced by 1
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/d4055cd7-4b30-46c1-ac91-e86eb76ff61d)
 
Choice 3
SUBMIT BOOK- Number of copies of that particular book is increased by 1
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/bfafbdc8-5a30-47b1-b4ae-5754291ba032)

Choice 4
DELETE BOOK- The record of the entered book gets deleted from the Dataframe
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/1e0b5af0-4151-491f-bc5e-6369703ad437)

Choice 5
SEARCH BOOK- Displays the details of the searched book
If the user wants to search a book by its author:
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/4a4d35dd-8743-465f-8813-f7e4ae55a748)

If the user wants to search a book by its name itself:
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/41182fb7-61f0-4606-a7bc-3acd3676abe7)

Choice 6
DISPLAY BOOK- Displays all books with their authors
 ![image](https://github.com/Aditi22Bansal/learn-python/assets/142652964/44904907-1333-48cd-9501-c69542d9a232)
