from Tkinter import *
import tkMessageBox
import sqlite3
import ttk
import time;

root=Tk()
root.title("LIBRARY MANAGEMENT SYSTEM")
root.geometry("1600x800+0+0")
root.config(bg="#FFE4B5")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
USERNAME1 = StringVar()
PASSWORD1 = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
EMAIL = StringVar()
ADDR = StringVar()
CITY_NAME = StringVar()
STATE_NAME = StringVar()
PHONE = IntVar()
BOOK_NAME = StringVar()
BOOK_PRICE = IntVar()
BOOK_QTY = IntVar()
SEARCH = StringVar()


#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `user` (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT, email TEXT, address TEXT, city TEXT, state TEXT, phone_no INTEGER)")
    #cursor.execute("CREATE TABLE IF NOT EXISTS `user` (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, email TEXT, address TEXT, city TEXT, state TEXT, phone_no INTEGER, username TEXT password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `book` (book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, book_name TEXT, book_qty TEXT, book_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

        #firstname, lastname, email, address, city, state, phone_no, username, password

        #cursor.execute("SELECT * FROM `user` WHERE `username` = 'user' AND `password` = 'user'")
        #if cursor.fetchone() is None:
        #cursor.execute("INSERT INTO `user` (username, password) VALUES('user', 'user')")
        #conn.commit()


        def Exit():
            result = tkMessageBox.askquestion('Library Management System', 'Are you sure you want to exit?', icon="warning")
            if result == 'yes':
                root.destroy()
                exit()

                def Exit2():
                    result = tkMessageBox.askquestion('Library Management System', 'Are you sure you want to exit?', icon="warning")
                    if result == 'yes':
                        Home.destroy()
                        exit()
                        def Exit3():
                            result = tkMessageBox.askquestion('Library Management System', 'Are you sure you want to exit?', icon="warning")
                            if result == 'yes':
                                Home1.destroy()
                                exit()


                                def ShowLoginForm():
                                    global loginform
                                    loginform = Toplevel()
                                    loginform.title("Library Management System/Admin's Account")
                                    width = 600
                                    height = 400
                                    screen_width = root.winfo_screenwidth()
                                    screen_height = root.winfo_screenheight()
                                    x = (screen_width/2) - (width/2)
                                    y = (screen_height/2) - (height/2)
                                    loginform.resizable(0, 0)
                                    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                    LoginForm()
                                    def ShowLoginForm1():
                                        global loginform
                                        loginform = Toplevel()
                                        loginform.title("Library Management System/User's Account")
                                        width = 600
                                        height = 400
                                        screen_width = root.winfo_screenwidth()
                                        screen_height = root.winfo_screenheight()
                                        x = (screen_width/2) - (width/2)
                                        y = (screen_height/2) - (height/2)
                                        loginform.resizable(0, 0)
                                        loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                        LoginForm1()

                                        def ShowAccntCreate():
                                            global details
                                            details = Toplevel()
                                            details.title("Library Management System/Create Account")
                                            width = 1300
                                            height = 700
                                            screen_width = root.winfo_screenwidth()
                                            screen_height = root.winfo_screenheight()
                                            x = (screen_width/2) - (width/2)
                                            y = (screen_height/2) - (height/2)
                                            details.resizable(0, 0)
                                            details.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                            Details()

                                            def Showabout():
                                                global loginform
                                                loginform = Toplevel()
                                                loginform.title("Library Management System/About")
                                                width = 1300
                                                height = 700
                                                screen_width = root.winfo_screenwidth()
                                                screen_height = root.winfo_screenheight()
                                                x = (screen_width/2) - (width/2)
                                                y = (screen_height/2) - (height/2)
                                                loginform.resizable(0, 0)
                                                loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                Abcd()

                                                def Abcd():

                                                    global lbl_result
                                                    TopLoginForm = Frame(loginform, width=1600, height=800, bd=1, relief=SOLID)
                                                    TopLoginForm.pack(side=TOP, pady=20)
                                                    lbl_text = Label(TopLoginForm, text="Library Management System APP", font=('Georgia', 18), width=1600)
                                                    lbl_text.pack(fill=X)
                                                    MidLoginForm = Frame(loginform, width=1600)
                                                    MidLoginForm.pack(side=TOP, pady=50)
                                                    lbl_text = Label(TopLoginForm, text="Version-1.0", font=('Georgia', 18), width=1600)
                                                    lbl_text.pack(fill=X)
                                                    MidLoginForm = Frame(loginform, width=1600)
                                                    MidLoginForm.pack(side=TOP, pady=50)
                                                    lbl_text = Label(TopLoginForm, text="e mail-group4librarydatabase@gmail.com\n", font=('Georgia', 18), width=1600)
                                                    lbl_text.pack(fill=X)
                                                    MidLoginForm = Frame(loginform, width=1600)
                                                    MidLoginForm.pack(side=BOTTOM)



                                                    def LoginForm():

                                                        global lbl_result
                                                        TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
                                                        TopLoginForm.pack(side=TOP, pady=20)
                                                        lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
                                                        lbl_text.pack(fill=X)
                                                        MidLoginForm = Frame(loginform, width=600)
                                                        MidLoginForm.pack(side=TOP, pady=50)
                                                        lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
                                                        lbl_username.grid(row=0)
                                                        lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
                                                        lbl_password.grid(row=1)
                                                        lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
                                                        lbl_result.grid(row=3, columnspan=2)
                                                        username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
                                                        username.grid(row=0, column=1)
                                                        password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
                                                        password.grid(row=1, column=1)
                                                        btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
                                                        btn_login.grid(row=2, columnspan=2, pady=20)
                                                        btn_login.bind('<Return>', Login)

                                                        def LoginForm1():
                                                            global lbl_result
                                                            TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
                                                            TopLoginForm.pack(side=TOP, pady=20)
                                                            lbl_text = Label(TopLoginForm, text="User Login", font=('arial', 18), width=600)
                                                            lbl_text.pack(fill=X)
                                                            MidLoginForm = Frame(loginform, width=600)
                                                            MidLoginForm.pack(side=TOP, pady=50)
                                                            lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
                                                            lbl_username.grid(row=0)
                                                            lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
                                                            lbl_password.grid(row=1)
                                                            lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
                                                            lbl_result.grid(row=3, columnspan=2)
                                                            username = Entry(MidLoginForm, textvariable=USERNAME1, font=('arial', 25), width=15)
                                                            username.grid(row=0, column=1)
                                                            password = Entry(MidLoginForm, textvariable=PASSWORD1, font=('arial', 25), width=15, show="*")
                                                            password.grid(row=1, column=1)
                                                            btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login1)
                                                            btn_login.grid(row=2, columnspan=2, pady=20)
                                                            btn_login.bind('<Return>', Login1)

                                                            def Details():
                                                                global lbl_detail
                                                                TopLoginForm = Frame(details, width=1600, height=100, bd=1, relief=SOLID)
                                                                TopLoginForm.pack(side=TOP, pady=20)
                                                                lbl_text = Label(TopLoginForm, text="Create new Account", font=('arial', 18), width=1600)
                                                                lbl_text.pack(fill=X)
                                                                MidLoginForm = Frame(details, width=1600)
                                                                MidLoginForm.pack(side=TOP, pady=50)


                                                                fnameLabel=Label(MidLoginForm,text='ENTER First Name')
                                                                fnameLabel.pack(side=TOP)
                                                                fnameTextField = Entry(MidLoginForm, textvariable=FIRST_NAME, bd =7)
                                                                fnameTextField.pack(side = TOP)
                                                                lnameLabel=Label(MidLoginForm,text='ENTER Last Name')
                                                                lnameLabel.pack(side=TOP)
                                                                lnameTextField = Entry(MidLoginForm, textvariable=LAST_NAME, bd =7)
                                                                lnameTextField.pack(side = TOP)
                                                                emailLabel=Label(MidLoginForm,text='ENTER Email')
                                                                emailLabel.pack(side=TOP)
                                                                emailTextField = Entry(MidLoginForm, textvariable=EMAIL, bd =7)
                                                                emailTextField.pack(side = TOP)
                                                                addressLabel=Label(MidLoginForm,text='ENTER Address')
                                                                addressLabel.pack(side=TOP)
                                                                addressTextField = Entry(MidLoginForm, textvariable=ADDR, bd =7)
                                                                addressTextField.pack(side = TOP)
                                                                cityLabel=Label(MidLoginForm,text='ENTER City')
                                                                cityLabel.pack(side=TOP)
                                                                cityTextField = Entry(MidLoginForm, textvariable=CITY_NAME, bd =7)
                                                                cityTextField.pack(side = TOP)
                                                                stateLabel=Label(MidLoginForm,text='ENTER State')
                                                                stateLabel.pack(side=TOP)
                                                                stateTextField = Entry(MidLoginForm, textvariable=STATE_NAME, bd =7)
                                                                stateTextField.pack(side = TOP)
                                                                phoneLabel=Label(MidLoginForm,text='ENTER Phone Number')
                                                                phoneLabel.pack(side=TOP)
                                                                phoneTextField = Entry(MidLoginForm, textvariable=PHONE, bd =7)
                                                                phoneTextField.pack(side = TOP)
                                                                UsernameLabel=Label(MidLoginForm,text='ENTER UserName')
                                                                UsernameLabel.pack(side=TOP)
                                                                UsernameTextField = Entry(MidLoginForm, textvariable=USERNAME1, bd =7)
                                                                UsernameTextField.pack(side = TOP)
                                                                PasswordLabel=Label(MidLoginForm,text='ENTER Password')
                                                                PasswordLabel.pack(side=TOP)
                                                                PasswordTextField = Entry(MidLoginForm, textvariable=PASSWORD1, bd =7)
                                                                PasswordTextField.pack(side = TOP)

                                                                btn_submit = Button(MidLoginForm, text="Submit", font=('arial', 18), width=30, command=Submit)
                                                                #btn_submit.grid(row=2, columnspan=2, pady=20)
                                                                btn_submit.pack(side=LEFT);
                                                                btn_submit.bind('<Return>', Submit)



                                                                def Home():
                                                                    global Home
                                                                    Home = Tk()
                                                                    Home.title("Library Management System/Home")
                                                                    width = 1300
                                                                    height = 700
                                                                    screen_width = Home.winfo_screenwidth()
                                                                    screen_height = Home.winfo_screenheight()
                                                                    x = (screen_width/2) - (width/2)
                                                                    y = (screen_height/2) - (height/2)
                                                                    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                                    Home.resizable(0, 0)
                                                                    Title = Frame(Home, bd=1, relief=SOLID)
                                                                    Title.pack(pady=10)
                                                                    lbl_display = Label(Title, text="Library Mangement System", font=('Georgia', 45))
                                                                    lbl_display.pack()
                                                                    menubar = Menu(Home)
                                                                    filemenu = Menu(menubar, tearoff=0)
                                                                    filemenu2 = Menu(menubar, tearoff=0)
                                                                    filemenu3 = Menu(menubar, tearoff=0)
                                                                    filemenu4 = Menu(menubar, tearoff=0)
                                                                    filemenu5 = Menu(menubar, tearoff=0)
                                                                    filemenu.add_command(label="Logout", command=Logout)
                                                                    filemenu.add_command(label="Exit", command=Exit2)
                                                                    filemenu2.add_command(label="Book", command=ShowAddNew)
                                                                    filemenu2.add_command(label="View", command=ShowView)
                                                                    filemenu2.add_command(label="User View", command=ShowUserView)
                                                                    menubar.add_cascade(label="Account", menu=filemenu)
                                                                    menubar.add_cascade(label="Management", menu=filemenu2)
                                                                    menubar.add_cascade(label="Book Info", menu=filemenu3)
                                                                    menubar.add_cascade(label="Notify", menu=filemenu4)
                                                                    Home.config(menu=menubar)
                                                                    Home.config(bg="teal")

                                                                    def Home1():
                                                                        global Home1
                                                                        Home1 = Tk()
                                                                        Home1.title("Library Management System/Home")
                                                                        width = 1300
                                                                        height = 700
                                                                        screen_width = Home1.winfo_screenwidth()
                                                                        screen_height = Home1.winfo_screenheight()
                                                                        x = (screen_width/2) - (width/2)
                                                                        y = (screen_height/2) - (height/2)
                                                                        Home1.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                                        Home1.resizable(0, 0)
                                                                        Title = Frame(Home1, bd=1, relief=SOLID)
                                                                        Title.pack(pady=10)
                                                                        lbl_display = Label(Title, text="Library Mangement System", font=('Georgia', 45))
                                                                        lbl_display.pack()
                                                                        menubar = Menu(Home1)
                                                                        filemenu = Menu(menubar, tearoff=0)
                                                                        filemenu.add_command(label="Logout", command=Logout1)
                                                                        filemenu.add_command(label="Exit", command=Exit3)
                                                                        menubar.add_cascade(label="Account", menu=filemenu)
                                                                        Home1.config(menu=menubar)
                                                                        Home1.config(bg="teal")

                                                                        def ShowAddNew():
                                                                            global addnewform
                                                                            addnewform = Toplevel()
                                                                            addnewform.title("Library management System/Add new")
                                                                            width = 600
                                                                            height = 800
                                                                            screen_width = Home.winfo_screenwidth()
                                                                            screen_height = Home.winfo_screenheight()
                                                                            x = (screen_width/2) - (width/2)
                                                                            y = (screen_height/2) - (height/2)
                                                                            addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                                            addnewform.resizable(0, 0)
                                                                            AddNewForm()

                                                                            def AddNewForm():
                                                                                TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
                                                                                TopAddNew.pack(side=TOP, pady=20)
                                                                                lbl_text = Label(TopAddNew, text="Add New book", font=('arial', 18), width=600)
                                                                                lbl_text.pack(fill=X)
                                                                                MidAddNew = Frame(addnewform, width=600)
                                                                                MidAddNew.pack(side=TOP, pady=50)
                                                                                lbl_productname = Label(MidAddNew, text="Book Name:", font=('arial', 25), bd=10)
                                                                                lbl_productname.grid(row=0, sticky=W)
                                                                                lbl_qty = Label(MidAddNew, text="No of books:", font=('arial', 25), bd=10)
                                                                                lbl_qty.grid(row=1, sticky=W)
                                                                                lbl_price = Label(MidAddNew, text="Fine:", font=('arial', 25), bd=10)
                                                                                lbl_price.grid(row=2, sticky=W)
                                                                                productname = Entry(MidAddNew, textvariable=BOOK_NAME, font=('arial', 25), width=15)
                                                                                productname.grid(row=0, column=1)
                                                                                productqty = Entry(MidAddNew, textvariable=BOOK_QTY, font=('arial', 25), width=15)
                                                                                productqty.grid(row=1, column=1)
                                                                                productprice = Entry(MidAddNew, textvariable=BOOK_PRICE, font=('arial', 25), width=15)
                                                                                productprice.grid(row=2, column=1)
                                                                                btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
                                                                                btn_add.grid(row=3, columnspan=2, pady=20)

                                                                                def AddNew():
                                                                                    Database()
                                                                                    cursor.execute("INSERT INTO `book` (book_name, book_qty, book_price) VALUES(?, ?, ?)", (str(BOOK_NAME.get()), int(BOOK_QTY.get()), int(BOOK_PRICE.get())))
                                                                                    conn.commit()
                                                                                    BOOK_NAME.set("")
                                                                                    BOOK_PRICE.set("")
                                                                                    BOOK_QTY.set("")
                                                                                    cursor.close()
                                                                                    conn.close()


                                                                                    def Submit():
                                                                                        Database()
                                                                                        cursor.execute("INSERT INTO `user` (firstname, lastname, email, address, city, state, phone_no, username, password) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(FIRST_NAME.get()), str(LAST_NAME.get()), str(EMAIL.get()), str(ADDR.get()), str(CITY_NAME.get()), str(STATE_NAME.get()), int(PHONE.get()), str(USERNAME1.get()), str(PASSWORD1.get())))
                                                                                        conn.commit()
                                                                                        FIRST_NAME.set("")
                                                                                        LAST_NAME.set("")
                                                                                        EMAIL.set("")
                                                                                        ADDR.set("")
                                                                                        CITY_NAME.set("")
                                                                                        STATE_NAME.set("")
                                                                                        PHONE.set("")
                                                                                        USERNAME1.set("")
                                                                                        PASSWORD1.set("")
                                                                                        cursor.close()
                                                                                        conn.close()

                                                                                        def ViewForm():
                                                                                            global tree
                                                                                            TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
                                                                                            TopViewForm.pack(side=TOP, fill=X)
                                                                                            LeftViewForm = Frame(viewform, width=600)
                                                                                            LeftViewForm.pack(side=LEFT, fill=Y)
                                                                                            MidViewForm = Frame(viewform, width=600)
                                                                                            MidViewForm.pack(side=RIGHT)
                                                                                            lbl_text = Label(TopViewForm, text="View books", font=('arial', 18), width=600)
                                                                                            lbl_text.pack(fill=X)
                                                                                            lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
                                                                                            lbl_txtsearch.pack(side=TOP, anchor=W)
                                                                                            search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
                                                                                            search.pack(side=TOP,  padx=10, fill=X)
                                                                                            btn_search = Button(LeftViewForm, text="Search", command=Search)
                                                                                            btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                            btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
                                                                                            btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                            btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
                                                                                            btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                            scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
                                                                                            scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
                                                                                            tree = ttk.Treeview(MidViewForm, columns=("BookID", "Book Name", "Book Qty", "Book Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
                                                                                            scrollbary.config(command=tree.yview)
                                                                                            scrollbary.pack(side=RIGHT, fill=Y)
                                                                                            scrollbarx.config(command=tree.xview)
                                                                                            scrollbarx.pack(side=BOTTOM, fill=X)
                                                                                            tree.heading('BookID', text="BookID",anchor=W)
                                                                                            tree.heading('Book Name', text="Book Name",anchor=W)
                                                                                            tree.heading('Book Qty', text="Book Qty",anchor=W)
                                                                                            tree.heading('Book Price', text="Book Price",anchor=W)
                                                                                            tree.column('#0', stretch=NO, minwidth=0, width=0)
                                                                                            tree.column('#1', stretch=NO, minwidth=0, width=0)
                                                                                            tree.column('#2', stretch=NO, minwidth=0, width=200)
                                                                                            tree.column('#3', stretch=NO, minwidth=0, width=120)
                                                                                            tree.column('#4', stretch=NO, minwidth=0, width=120)
                                                                                            tree.pack()
                                                                                            DisplayData()


                                                                                            def UViewForm():
                                                                                                global tree
                                                                                                TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
                                                                                                TopViewForm.pack(side=TOP, fill=X)
                                                                                                LeftViewForm = Frame(viewform, width=600)
                                                                                                LeftViewForm.pack(side=LEFT, fill=Y)
                                                                                                MidViewForm = Frame(viewform, width=600)
                                                                                                MidViewForm.pack(side=RIGHT)
                                                                                                lbl_text = Label(TopViewForm, text="Users", font=('arial', 18), width=600)
                                                                                                lbl_text.pack(fill=X)
                                                                                                lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
                                                                                                lbl_txtsearch.pack(side=TOP, anchor=W)
                                                                                                search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
                                                                                                search.pack(side=TOP,  padx=10, fill=X)
                                                                                                btn_search = Button(LeftViewForm, text="Search", command=Search1)
                                                                                                btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                                btn_reset = Button(LeftViewForm, text="Reset", command=Reset1)
                                                                                                btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                                btn_delete = Button(LeftViewForm, text="Delete", command=Delete1)
                                                                                                btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
                                                                                                scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
                                                                                                scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
                                                                                                tree = ttk.Treeview(MidViewForm, columns=("user_id","username","password","firstname", "lastname", "email", "address", "city", "state", "phone_no"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
                                                                                                scrollbary.config(command=tree.yview)
                                                                                                scrollbary.pack(side=RIGHT, fill=Y)
                                                                                                scrollbarx.config(command=tree.xview)
                                                                                                scrollbarx.pack(side=BOTTOM, fill=X)
                                                                                                tree.heading('user_id', text="UserID",anchor=W)
                                                                                                tree.heading('username', text="UserName",anchor=W)
                                                                                                tree.heading('password', text="Password",anchor=W)
                                                                                                tree.heading('firstname', text="Firstname",anchor=W)
                                                                                                tree.heading('lastname', text="Lastname",anchor=W)
                                                                                                tree.heading('email', text="Email-ID",anchor=W)
                                                                                                tree.heading('address', text="Address",anchor=W)
                                                                                                tree.heading('city', text="City",anchor=W)
                                                                                                tree.heading('state', text="State",anchor=W)
                                                                                                tree.heading('phone_no', text="PhoneNO",anchor=W)

                                                                                                tree.column('#0', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#1', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#2', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#3', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#4', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#5', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#6', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#7', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#8', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#9', stretch=NO, minwidth=0, width=120)
                                                                                                tree.column('#10', stretch=NO, minwidth=0, width=120)
                                                                                                tree.pack()
                                                                                                DisplayData1()

                                                                                                def DisplayData():
                                                                                                    Database()
                                                                                                    cursor.execute("SELECT * FROM `book`")
                                                                                                    fetch = cursor.fetchall()
                                                                                                    for data in fetch:
                                                                                                        tree.insert('', 'end', values=(data))
                                                                                                        cursor.close()
                                                                                                        conn.close()

                                                                                                        def DisplayData1():
                                                                                                            Database()
                                                                                                            cursor.execute("SELECT * FROM `user`")
                                                                                                            fetch = cursor.fetchall()
                                                                                                            for data in fetch:
                                                                                                                tree.insert('', 'end', values=(data))
                                                                                                                cursor.close()
                                                                                                                conn.close()

                                                                                                                def Search():
                                                                                                                    if SEARCH.get() != "":
                                                                                                                        tree.delete(*tree.get_children())
                                                                                                                        Database()
                                                                                                                        cursor.execute("SELECT * FROM `book` WHERE `book_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
                                                                                                                        fetch = cursor.fetchall()
                                                                                                                        for data in fetch:
                                                                                                                            tree.insert('', 'end', values=(data))
                                                                                                                            cursor.close()
                                                                                                                            conn.close()

                                                                                                                            def Search1():
                                                                                                                                if SEARCH.get() != "":
                                                                                                                                    tree.delete(*tree.get_children())
                                                                                                                                    Database()
                                                                                                                                    cursor.execute("SELECT * FROM `user` WHERE `username` LIKE ?", ('%'+str(SEARCH.get())+'%',))
                                                                                                                                    fetch = cursor.fetchall()
                                                                                                                                    for data in fetch:
                                                                                                                                        tree.insert('', 'end', values=(data))
                                                                                                                                        cursor.close()
                                                                                                                                        conn.close()


                                                                                                                                        def Reset():
                                                                                                                                            tree.delete(*tree.get_children())
                                                                                                                                            DisplayData()
                                                                                                                                            SEARCH.set("")

                                                                                                                                            def Reset1():
                                                                                                                                                tree.delete(*tree.get_children())
                                                                                                                                                DisplayData1()
                                                                                                                                                SEARCH.set("")

                                                                                                                                                def Delete():
                                                                                                                                                    if not tree.selection():
                                                                                                                                                        print("ERROR")
                                                                                                                                                    else:
                                                                                                                                                        result = tkMessageBox.askquestion('Library management System', 'Are you sure you want to delete this record?', icon="warning")
                                                                                                                                                        if result == 'yes':
                                                                                                                                                            curItem = tree.focus()
                                                                                                                                                            contents =(tree.item(curItem))
                                                                                                                                                            selecteditem = contents['values']
                                                                                                                                                            tree.delete(curItem)
                                                                                                                                                            Database()
                                                                                                                                                            cursor.execute("DELETE FROM `book` WHERE `book_id` = %d" % selecteditem[0])
                                                                                                                                                            conn.commit()
                                                                                                                                                            cursor.close()
                                                                                                                                                            conn.close()

                                                                                                                                                            def Delete1():
                                                                                                                                                                if not tree.selection():
                                                                                                                                                                    print("ERROR")
                                                                                                                                                                else:
                                                                                                                                                                    result = tkMessageBox.askquestion('Library management System', 'Are you sure you want to delete this record?', icon="warning")
                                                                                                                                                                    if result == 'yes':
                                                                                                                                                                        curItem = tree.focus()
                                                                                                                                                                        contents =(tree.item(curItem))
                                                                                                                                                                        selecteditem = contents['values']
                                                                                                                                                                        tree.delete(curItem)
                                                                                                                                                                        Database()
                                                                                                                                                                        cursor.execute("DELETE FROM `user` WHERE `username` = %d" % selecteditem[0])
                                                                                                                                                                        conn.commit()
                                                                                                                                                                        cursor.close()
                                                                                                                                                                        conn.close()


                                                                                                                                                                        def ShowView():
                                                                                                                                                                            global viewform
                                                                                                                                                                            viewform = Toplevel()
                                                                                                                                                                            viewform.title("Library management System/View Book")
                                                                                                                                                                            width = 600
                                                                                                                                                                            height = 400
                                                                                                                                                                            screen_width = Home.winfo_screenwidth()
                                                                                                                                                                            screen_height = Home.winfo_screenheight()
                                                                                                                                                                            x = (screen_width/2) - (width/2)
                                                                                                                                                                            y = (screen_height/2) - (height/2)
                                                                                                                                                                            viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                                                                                                                                            viewform.resizable(0, 0)
                                                                                                                                                                            ViewForm()

                                                                                                                                                                            def ShowUserView():
                                                                                                                                                                                global viewform
                                                                                                                                                                                viewform = Toplevel()
                                                                                                                                                                                viewform.title("Library management System/View User")
                                                                                                                                                                                width = 600
                                                                                                                                                                                height = 400
                                                                                                                                                                                screen_width = Home.winfo_screenwidth()
                                                                                                                                                                                screen_height = Home.winfo_screenheight()
                                                                                                                                                                                x = (screen_width/2) - (width/2)
                                                                                                                                                                                y = (screen_height/2) - (height/2)
                                                                                                                                                                                viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                                                                                                                                                                viewform.resizable(0, 0)
                                                                                                                                                                                UViewForm()

                                                                                                                                                                                def Logout():
                                                                                                                                                                                    result = tkMessageBox.askquestion('Library management System', 'Are you sure you want to logout?', icon="warning")
                                                                                                                                                                                    if result == 'yes':
                                                                                                                                                                                        admin_id = ""
                                                                                                                                                                                        root.deiconify()
                                                                                                                                                                                        Home.destroy()
                                                                                                                                                                                        def Logout1():
                                                                                                                                                                                            result = tkMessageBox.askquestion('Library management System', 'Are you sure you want to logout?', icon="warning")
                                                                                                                                                                                            if result == 'yes':
                                                                                                                                                                                                user_id = ""
                                                                                                                                                                                                root.deiconify()
                                                                                                                                                                                                Home1.destroy()

                                                                                                                                                                                                def Login(event=None):
                                                                                                                                                                                                    global admin_id
                                                                                                                                                                                                    Database()
                                                                                                                                                                                                    if USERNAME.get == "" or PASSWORD.get() == "":
                                                                                                                                                                                                        lbl_result.config(text="Please complete the required field!", fg="red")
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
                                                                                                                                                                                                        if cursor.fetchone() is not None:
                                                                                                                                                                                                            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
                                                                                                                                                                                                            data = cursor.fetchone()
                                                                                                                                                                                                            admin_id = data[0]
                                                                                                                                                                                                            USERNAME.set("")
                                                                                                                                                                                                            PASSWORD.set("")
                                                                                                                                                                                                            lbl_result.config(text="")
                                                                                                                                                                                                            ShowHome()
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            lbl_result.config(text="Invalid username or password", fg="red")
                                                                                                                                                                                                            USERNAME.set("")
                                                                                                                                                                                                            PASSWORD.set("")
                                                                                                                                                                                                            cursor.close()
                                                                                                                                                                                                            conn.close()

                                                                                                                                                                                                            def Login1(event=None):
                                                                                                                                                                                                                global user_id
                                                                                                                                                                                                                Database()
                                                                                                                                                                                                                if USERNAME1.get == "" or PASSWORD1.get() == "":
                                                                                                                                                                                                                    lbl_result.config(text="Please complete the required field!", fg="red")
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    cursor.execute("SELECT * FROM `user` WHERE `username` = ? AND `password` = ?", (USERNAME1.get(), PASSWORD1.get()))
                                                                                                                                                                                                                    if cursor.fetchone() is not None:
                                                                                                                                                                                                                        cursor.execute("SELECT * FROM `user` WHERE `username` = ? AND `password` = ?", (USERNAME1.get(), PASSWORD1.get()))
                                                                                                                                                                                                                        data = cursor.fetchone()
                                                                                                                                                                                                                        user_id = data[0]
                                                                                                                                                                                                                        USERNAME1.set("")
                                                                                                                                                                                                                        PASSWORD1.set("")
                                                                                                                                                                                                                        lbl_result.config(text="")
                                                                                                                                                                                                                        ShowHome1()
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        lbl_result.config(text="Invalid username or password", fg="red")
                                                                                                                                                                                                                        USERNAME1.set("")
                                                                                                                                                                                                                        PASSWORD1.set("")
                                                                                                                                                                                                                        cursor.close()
                                                                                                                                                                                                                        conn.close()



                                                                                                                                                                                                                        def ShowHome():
                                                                                                                                                                                                                            root.withdraw()
                                                                                                                                                                                                                            Home()
                                                                                                                                                                                                                            loginform.destroy()

                                                                                                                                                                                                                            def ShowHome1():
                                                                                                                                                                                                                                root.withdraw()
                                                                                                                                                                                                                                Home1()
                                                                                                                                                                                                                                loginform.destroy()
                                                                                                                                                                                                                                #========================================MENUBAR WIDGETS==================================
                                                                                                                                                                                                                                menubar = Menu(root)
                                                                                                                                                                                                                                filemenu = Menu(menubar, tearoff=0)
                                                                                                                                                                                                                                helpmenu = Menu(menubar, tearoff=0)
                                                                                                                                                                                                                                filemenu.add_command(label="Admin's Account", command=ShowLoginForm)
                                                                                                                                                                                                                                filemenu.add_command(label="User's Account", command=ShowLoginForm1)
                                                                                                                                                                                                                                filemenu.add_command(label="Create Account", command=ShowAccntCreate)
                                                                                                                                                                                                                                helpmenu.add_command(label="About", command=Showabout)
                                                                                                                                                                                                                                filemenu.add_command(label="Exit", command=Exit)
                                                                                                                                                                                                                                menubar.add_cascade(label="||||", menu=filemenu)
                                                                                                                                                                                                                                menubar.add_cascade(label="Help",menu=helpmenu)
                                                                                                                                                                                                                                helpmenu.add_command(label="Guidelines")
                                                                                                                                                                                                                                root.config(menu=menubar)

                                                                                                                                                                                                                                #========================================FRAME============================================
                                                                                                                                                                                                                                Title = Frame(root,width=1600,height=100, relief="solid",bg='#FFE4B5')
                                                                                                                                                                                                                                Title.pack(side=TOP)

                                                                                                                                                                                                                                f1= Frame(root,width=400,height=500,relief="solid",bg='#FFE4B5')
                                                                                                                                                                                                                                f1.pack(side=BOTTOM)

                                                                                                                                                                                                                                localtime=time.asctime(time.localtime(time.time()))




                                                                                                                                                                                                                                #========================================LABEL WIDGET=====================================
                                                                                                                                                                                                                                lbl_display = Label(Title, text="LIBRARY MANAGEMENT SYSTEM", font=('Forte',50,'underline'),fg='steel Blue',bg='#FFE4B5')
                                                                                                                                                                                                                                lbl_display.grid(row=0,column=0)

                                                                                                                                                                                                                                lbl_display = Label(Title, text=localtime, font=('arial', 37,'underline'),fg='#00BFFF',bg="#FFE4B5")
                                                                                                                                                                                                                                lbl_display.grid(row=1,column=0)

                                                                                                                                                                                                                                cont1=Canvas(f1,width=400,height=400,bg="#FFE4B5")
                                                                                                                                                                                                                                cont1.grid(row=0,column=0)
                                                                                                                                                                                                                                image5=PhotoImage(file="")
                                                                                                                                                                                                                                cont1.create_image(200,200,image=image5)



                                                                                                                                                                                                                                #========================================INITIALIZATION===================================
                                                                                                                                                                                                                                if __name__ == '__main__':
                                                                                                                                                                                                                                    root.mainloop()
