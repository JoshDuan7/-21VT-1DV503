import csv
import mysql.connector
import getpass
from mysql.connector import errorcode

cnx = mysql.connector.connect(
    user='root',
    passwd='rootroot',
    host='127.0.0.1')
# Note! Please put the .csv files in the same directory(folder) as this .py file.

# Database name, group members: Fabian Dacic, Yuyao Duan
DB_NAME = 'Dacic_Duan' 

cursor = cnx.cursor()

# Create database
def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Create table customers for 'customer_contact_info.csv'
def create_table_customers(cursor):
    create_customers = ('''CREATE TABLE customers ( \
                    id INT NOT NULL, \
                    register_number VARCHAR(50), \
                    first_name VARCHAR(50), \
                    last_name VARCHAR(50), \
                    telephone_number BIGINT, \
                    address VARCHAR(50), \
                    email VARCHAR(50), \
                    PRIMARY KEY (id) \
                   )ENGINE=InnoDB''')
    try: # Handle table creation exception
        print("Creating table customers: ") 
        cursor.execute(create_customers)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists! ")
        else:
            print(err.msg)
    else:
        print("OK")      

# Create table cars for 'customer_car_info.csv'
def create_table_cars(cursor):
    create_cars = ('''CREATE TABLE cars ( \
                   register_number VARCHAR(25) NOT NULL, \
                   car_make VARCHAR(50), \
                   car_model VARCHAR(50), \
                   car_model_year INT, \
                   mile_age INT, \
                   tire_size INT, \
                   color VARCHAR(50), \
                   car_VIN VARCHAR(50), \
                   PRIMARY KEY (register_number) \
                  ) ENGINE=InnoDB''')
    # Handle table creation exception
    try: 
        print("Creating table cars: ")
        cursor.execute(create_cars)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Already exists!")
        else:
            print(err.msg)
    else:
        print("OK")

# Create a table for summer tires
def create_table_summer_tire(cursor):
    create_s_tire = ('''CREATE TABLE summer_tires ( \
                   prod_id VARCHAR(25) NOT NULL, \
                   brand VARCHAR(25), \
                   size INT, \
                   inventory INT, \
                   buying_price INT, \
                   selling_price INT, \
                   change_fee INT, \
                   PRIMARY KEY (prod_id) \
                  ) ENGINE=InnoDB''')
    try:
        print("Creating table summer_tire: ")
        cursor.execute(create_s_tire)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Create a table for winter tires
def create_table_winter_tire(cursor):
    create_w_tire = ('''CREATE TABLE winter_tires ( \
                   prod_id varchar(25) NOT NULL, \
                   brand varchar(25), \
                   size int (11), \
                   inventory int (11), \
                   buying_price int(11), \
                   selling_price int(11), \
                   change_fee int(11), \
                   PRIMARY KEY (prod_id) \
                  ) ENGINE=InnoDB''')
    try:
        print("Creating table summer_tire: ")
        cursor.execute(create_w_tire)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Create a table for orders
def create_table_order(cursor):
    create_order = ('''CREATE TABLE orders ( \
                   order_id int(11) NOT NULL, \
                   prod_id varchar(25), \
                   brand varchar(25), \
                   size int (11), \
                   quantity int(11), \
                   register_number varchar(25), \
                   remark varchar(25), \
                   PRIMARY KEY (order_id) \
                  ) ENGINE=InnoDB''')
    try:
        print("Creating table orders: ")
        cursor.execute(create_order)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Query all customer's contact information
def query_admin_1(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT * FROM Dacic_Duan.customers;''')
    cursor.execute(query)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for id, register_number, first_name, last_name, telephone, address, email in cursor:
        print("ID: {:<5} Register Number: {:<10} First Name:{:<20} Last Name: {:<20} Address:{:<25} Email: {:<20}".format(id,register_number,first_name,last_name,address,email))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    cursor.close()

# Query all customer's car information
def query_admin_2(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT * FROM Dacic_Duan.cars;''')
    cursor.execute(query)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for register_number, car_make, car_model, car_model_year, mile_age, tire_size, color, car_VIN in cursor:
        print("Register Num:", register_number, "|", "Make:", car_make, "|", "Model:", car_model , "|", "Year:", car_model_year , "|", "Mile Age:", mile_age , "|", "Tire Size:", tire_size, "|", "Color:", color, "|", "Car VIN:", car_VIN, "|")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    cursor.close()

# Query all summer tires' information
def query_admin_3(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT * 
                FROM Dacic_Duan.summer_tires
                ORDER BY size ASC;''')
    cursor.execute(query)
    print()
    print("All summer tire information: ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for prod_id, brand, size, inventory, buying_price, selling_price, change_fee in cursor:
        print("Product ID:", prod_id, "|", "Brand:", brand, "|", "Size:", size , "|", "Inventory Num:", inventory , "|", "Buying Price:", buying_price , "|", "Selling Price:", selling_price, "|", "Change Fee:", change_fee, "|")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    cursor.close()

# Query all winter tires' information
def query_admin_4(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT * 
                FROM Dacic_Duan.winter_tires
                ORDER BY size ASC;''')
    cursor.execute(query)
    print()
    print("All winter tire information: ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for prod_id, brand, size, inventory, buying_price, selling_price, change_fee in cursor:
        print("Product ID:", prod_id, "|", "Brand:", brand, "|", "Size:", size , "|", "Inventory Num:", inventory , "|", "Buying Price:", buying_price , "|", "Selling Price:", selling_price, "|", "Change Fee:", change_fee, "|")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    cursor.close()

def query_admin_5(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT brand as TireBrand, SUM(inventory) as Inventory, SUM(buying_price) as Cost
                  FROM ((SELECT brand, inventory, buying_price FROM Dacic_Duan.summer_tires ) UNION ALL
                        (SELECT brand, inventory, buying_price FROM Dacic_Duan.winter_tires )) 
                         sl GROUP BY TireBrand HAVING Inventory > 0;''')
    print()
    print("Current inventory cost: ")
    print("-------------------------------------------------------------------------")
    cursor.execute(query)
    cost = 0
    for Brand, Amount, Cost in cursor:
        cost += Cost
        print(" Brand: {:<20} Amount: {:<10} Inventory Cost: {:<5} SEK".format(Brand, Amount, Cost))
    print("-------------------------------------------------------------------------")
    print("(Total inventory cost: {} SEK)".format(cost))
    cursor.close()

def query_admin_6(DB_NAME):
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    query = ('''SELECT * FROM Dacic_Duan.orders ORDER BY order_id;''')
    cursor.execute(query)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for order_id, prod_id, brand, size, quantity, register_number, remark in cursor:
        print("OrderID: {:<5} ProdID: {:<10} Brand: {:<20} Size: {:<5} Quantity: {:<10} Register Number: {:<10}  Remark: {}".format(order_id, prod_id, brand, size, quantity, register_number, remark))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    cursor.close()

# Average price of tire based on size
def query_1(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    query_1 = ('''SELECT id AS CustomerID, register_number AS CarRegisterNumber
                  FROM customers;''')
    cursor.execute(query_1)
    print("Customers and car register numbers")
    print("--------------------------------------------------------------")
    for CustomerID, CarRegisterNumber in cursor:
        print("Customer ID: {:<5} Register Number: {:<5}".format(CustomerID, CarRegisterNumber))
    print("--------------------------------------------------------------")
    cursor.close()


# Summer tires available for the register number
def query_2(DB_NAME, register_number): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    query_2 = ('''SELECT a.register_number, a.tire_size, b.size, b.brand, b.selling_price 
                  FROM Dacic_Duan.cars AS a 
                  JOIN Dacic_Duan.summer_tires AS b ON a.tire_size = b.size
                  WHERE a.register_number = {}
                  ORDER BY b.selling_price ASC;'''.format(register_number))
    cursor.execute(query_2)
    
    print("------------------------------------------------------------------------------")
    for RegisterNumber, TireSize, Size, Brand, Price in cursor: 
        print("Register number: ", RegisterNumber,"|", "Tire size: ", Size, "|", "Brand: ", Brand+"\t", "|", "Price:", Price)
    print("------------------------------------------------------------------------------")
    cursor.close()

# Winter tires available for the register number
def query_3(DB_NAME, register_number): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    query_3 = ('''SELECT a.register_number, a.tire_size, b.size, b.brand, b.selling_price 
                  FROM Dacic_Duan.cars AS a 
                  JOIN Dacic_Duan.winter_tires AS b ON a.tire_size = b.size
                  WHERE a.register_number = {}
                  ORDER BY b.selling_price ASC;'''.format(register_number))
    cursor.execute(query_3)
    
    print("------------------------------------------------------------------------------")
    for RegisterNumber, TireSize, Size, Brand, Price in cursor: 
        print("Register number: ", RegisterNumber,"|", "Tire size: ", Size, "|", "Brand: ", Brand+"\t", "|", "Price:", Price)
    print("------------------------------------------------------------------------------")
    cursor.close()

# Average price, maximum and minimum in regards to tire size
def query_4(DB_NAME): 
    cursor = cnx.cursor()

    cursor.execute("USE {}".format(DB_NAME))

    query_4 = ('''SELECT size as TireSize, MIN(selling_price) as MinPrice, MAX(selling_price) as MaxPrice, AVG(selling_price) as AveragePrice  
                  FROM ((SELECT size, selling_price FROM Dacic_Duan.summer_tires ) UNION ALL 
                  (SELECT size, selling_price FROM Dacic_Duan.winter_tires )) 
                    sl GROUP BY TireSize 
                       ORDER BY TireSize ASC;''')
    cursor.execute(query_4)
    print("Average, maximum and minimum price of all tire sizes:")
    print("--------------------------------------------------------------------------------------------------")
    for TireSize, MinPrice, MaxPrice, AveragePrice in cursor: 
        print(" Tire size: {} Inch \t Min price: {} SEK \t Max price: {} SEK \t Average Price: {} SEK".format(TireSize, MinPrice, MaxPrice, round(AveragePrice)))
    print("--------------------------------------------------------------------------------------------------") 
    cursor.close()

def query_5(DB_NAME,order_id, prod_id, brand, size, quantity, register_number, remark): 
    cursor = cnx.cursor()

    cursor.execute("USE {}".format(DB_NAME))

    query_5 = ('''INSERT INTO orders VALUES ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_id, prod_id, brand, size, quantity, register_number, remark))
    cursor.execute(query_5)
    print("Generate an order!")
    cursor.close()

# View for workshop employees / workers to see client IDs and their vehicles 
def view_1(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    # creating the view 
    
    try: 
        creating_view_1 = ('''
                            CREATE OR REPLACE VIEW Workshop_Employees
                            AS SELECT a.ID, a.register_number AS c_r_num, 
                                      b.register_number AS cc_r_num, b.car_make, b.car_model, b.tire_size
                            FROM dacic_duan.customers AS a JOIN dacic_duan.cars AS b
                            USING (register_number); 
                           ''')
    except mysql.connector.Error as err:
        print("The error in question is: ", err)

    cursor.execute(creating_view_1)
    cursor.close()

# View for workshop employees / workers to see winter tires details 
def view_2(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    # creating the view 
    try: 
        creating_view_2 = ('''
        CREATE OR REPLACE VIEW wt_employees AS SELECT 
        prod_id as wt_prod_id, brand as wt_brand, size as wt_size, SUM(inventory) as wt_inventory, 
        AVG(selling_price) as wt_sell_price, AVG(change_fee) as wt_changing_fee 
        FROM (SELECT prod_id, brand, size, inventory, selling_price, change_fee FROM Dacic_Duan.winter_tires)
        sl GROUP BY wt_prod_id
           ORDER BY wt_size; 
        ''')
    except mysql.connector.Error as err:
        print("The error in question is: ", err)

    cursor.execute(creating_view_2)
    cursor.close()

# View for workshop employees / workers to see summer tires details 
def view_3(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))

    # creating the view 
    try: 
        creating_view_3 = ('''
        CREATE OR REPLACE VIEW st_employees AS SELECT 
        prod_id as st_prod_id, brand as st_brand, size as st_size, SUM(inventory) as st_inventory, 
        AVG(selling_price) as st_sell_price, AVG(change_fee) as st_changing_fee 
        FROM (SELECT prod_id, brand, size, inventory, selling_price, change_fee FROM Dacic_Duan.summer_tires)
        sl GROUP BY st_prod_id
           ORDER BY st_size; 
        ''')
    except mysql.connector.Error as err:
        print("The error in question is: ", err)

    cursor.execute(creating_view_3)
    cursor.close()


# Select all from the view 
def select_view_1(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    view_1 = ('''SELECT * FROM Workshop_Employees''')
    cursor.execute(view_1)
    print("Customer information: ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    for ID, reg_num, __, car_make, car_model, tire_size in cursor:
        print((" Customer ID: {:<5} Registration number: {} \t Car make: {:<20} Car model: {:<20} Tire size: {}".format(ID, reg_num, car_make, car_model, tire_size))) 
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

    cursor.close()

def select_view_2(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    view_2 = ('''SELECT * FROM wt_employees''')
    cursor.execute(view_2)

    print("Winter Tire Information: ")
    print("---------------------------------------------------------------------------------------------------------------")
    for prod_id, bra, siz, inv, spr, wcf in cursor:
        print(" ProductID: {:<10} Brand: {:<15} Size: {:<5} Inventory: {:<5} Price: {:<10} Changing Fee: {}".format(prod_id, bra, siz, inv, round(spr), round(wcf))) 
    print("---------------------------------------------------------------------------------------------------------------")

    cursor.close()

def select_view_3(DB_NAME): 
    cursor = cnx.cursor()
    cursor.execute("USE {}".format(DB_NAME))
    
    view_2 = ('''SELECT * FROM st_employees''')
    cursor.execute(view_2)

    print("Summer Tire Information: ")
    print("---------------------------------------------------------------------------------------------------------------")
    for prod_id, bra, siz, inv, spr, wcf in cursor:
        print(" ProductID: {:<10} Brand: {:<15} Size: {:<5} Inventory: {:<5} Price: {:<10} Changing Fee: {}".format(prod_id, bra, siz, inv, round(spr), round(wcf))) 
    print("---------------------------------------------------------------------------------------------------------------")

    cursor.close()

def access_entry():
    print()
    print("#######    WELCOME USE DACIC & DUAN TIRE SERVICE DATABASE SYSTEM    #######")
    print("""
        1. Managers and administrators access  
        2. Employees and workers access 
        Q. Quit""")
    print()
    global secure_count
    while(True):
        ans = input("Please make a selection: ")
        if ans == "1":
            password = getpass.getpass("Please enter admin password: ")
            if password == "admin" and secure_count < 3: # 
                menu_admin()
            elif secure_count < 3:
                print("Invalid admin password!")
                secure_count += 1
            else:
                print("Password verification error more than three times! System quit!")
                break
        elif ans == "2":
            password = getpass.getpass("Please enter worker password: ")
            if password == "worker" and secure_count < 3:
                menu_worker()
            elif secure_count < 3:
                print("Invalid worker password!")
                secure_count += 1
            else:
                print("Password verification error more than three times! System quit!")
                break
        elif ans == "q" or ans == "Q":
            print("Exit the database management system.")
            break

def return_admin_menu():
    input("Press any key and press 'Enter' to return : ")
    menu_admin()

def return_worker_menu():
    input("Press any key and press 'Enter' to return : ")
    menu_worker()

def menu_admin():
    print("""
        1. Query customer's contact information.  
        2. Query customer's car information.
        3. Query all summer tires' information.
        4. Query all winter tires' information.
        5. Query current inventory cost.
        6. Query all orders.
        7. Back to the previous menu
        Q. Quit""")
    print()
    ans = input("Please make a choice: ")
    if ans == "1":
        query_admin_1(DB_NAME)
        return_admin_menu()
    elif ans == "2":
        query_admin_2(DB_NAME)
        return_admin_menu()
    elif ans == "3":
        query_admin_3(DB_NAME)
        return_admin_menu()
    elif ans == "4":
        query_admin_4(DB_NAME)
        return_admin_menu()
    elif ans == "5":
        query_admin_5(DB_NAME)
        return_admin_menu()
    elif ans == "6":
        query_admin_6(DB_NAME)
        return_admin_menu()
    elif ans == "7":
        access_entry()
    elif ans == "Q" or ans == "q":
        cnx.close() 
        print("Exit database system.")
        exit()
    else:
        print(">>> Invalid input! Please re-enter according to the options！<<<")
        menu_admin()


def menu_worker():
    print("""
        1. Query customerIDs and car register numbers.  
        2. List all available tires for the car.
        3. Query the average, maximum and minimum price of all tire sizes.
        4. All information of the customers (view for workers).
        5. All information of winter tires (view for workers).
        6. All information of summer tires (view for workers).
        7. Generate a new order for tires.
        8. Back to the previous menu  
        Q. Quit""")
    print()
    ans = input("Query for: ") 

    if ans == "1": 
        query_1(DB_NAME)
        return_worker_menu()
    elif ans == "2":
        print('''
              1. Summer tire
              2. Winter tire
              3. Return to previous menu
              ''')
        choice = input("Query for: ")
        if choice == "1":
            stuc = (input("Please enter car register number: ")) 
            st_cm = ("'{}'".format(stuc))
            print("Summer tire selections for the car: ")
            query_2(DB_NAME, st_cm)
            return_worker_menu()
        elif choice == "2":
            stuc = (input("Please enter car register number: "))
            st_cm = ("'{}'".format(stuc)) 
            print("Winter tire selections for the car: ")
            query_3(DB_NAME, st_cm)
            return_worker_menu()
        elif choice == "3":
            return_worker_menu()
        else:
            print("Invalid input! Exit!")
            return_worker_menu()
    elif ans == "3": 
        query_4(DB_NAME)
        return_worker_menu()
    elif ans == "4":
        view_1(DB_NAME) 
        select_view_1(DB_NAME)
        return_worker_menu()
    elif ans == "5": 
        view_2(DB_NAME)
        select_view_2(DB_NAME)
        return_worker_menu()
    elif ans == "6": 
        view_3(DB_NAME)
        select_view_3(DB_NAME)
        return_worker_menu()
    elif ans == "7":
        order_id = int(input("Please enter order id: "))
        prod_id = input("Please enter product id: ")
        brand = input("Please enter brand: ")
        size = int(input("Please enter size: "))
        quantity = int(input("Please enter quantity: "))
        register_number = input("Please enter register number: ")
        remark = input("Please enter remark: ")
        query_5(DB_NAME, order_id, prod_id, brand, size, quantity, register_number, remark)
        return_worker_menu()
    elif ans == "8":
        access_entry()
    elif ans == "Q" or ans == "q":
        # disconnecting from MySQL connection  
        cnx.close() 
        print("Exit database system.")
        exit()
    else: 
        print(menu_worker())

# Function for return to main menu
# def return_to_menu(flag):
#     if flag == False:
#         print()
#         input("Please click any key to continue: ")
#         print()
#         flag = True
#         return flag

# Program starts
try:
    cursor.execute("USE {}".format(DB_NAME)) 
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        # Create database
        create_database(cursor, DB_NAME)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
        # Create three tables
        cursor.execute('DROP TABLE IF EXISTS customers')
        create_table_customers(cursor)
        cursor.execute('DROP TABLE IF EXISTS cars')
        create_table_cars(cursor)
        cursor.execute('DROP TABLE IF EXISTS summer_tires')
        create_table_summer_tire(cursor)
        cursor.execute('DROP TABLE IF EXISTS winter_tires')
        create_table_winter_tire(cursor)
        cursor.execute('DROP TABLE IF EXISTS orders')
        create_table_order(cursor)
    else:
        print(err)

# Read customer_contact_info.csv to database, please put the .csv in the same directory of this .py file
with open ('customer_contact_info.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        id = row[0]
        register_number = row[1]
        first_name = row[2]
        last_name = row[3]
        telephone_number = row[4]
        address = row[5]
        email = row[6]
        # Handle exception when data has been inserted
        try:
            cursor.execute('''INSERT INTO customers(id, register_number, first_name, last_name, telephone_number, address, email)
                              VALUES (%s, %s, %s, %s, %s, %s, %s)''',(id, register_number, first_name, last_name, telephone_number, address, email)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

# Read customer_car_info.csv to database, please put the .csv in the same directory of this .py file
with open ('customer_car_info.csv','r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    next(csv_reader2)
    for row in csv_reader2:
        register_number = row[0]
        car_make = row[1]
        car_model = row[2]
        car_model_year = row[3]
        mile_age = row[4]
        tire_size = row[5]
        color = row[6]
        car_VIN = row[7]
        # Handle exception when data has been inserted
        try:
            cursor.execute('''INSERT INTO cars(register_number, car_make, car_model, car_model_year, mile_age, tire_size, color, car_VIN) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',(register_number, car_make, car_model, car_model_year, mile_age, tire_size, color, car_VIN)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

with open ('car_tire_summer.csv','r') as csv_file3:
    csv_reader3 = csv.reader(csv_file3)
    next(csv_reader3)
    for row in csv_reader3:
        prod_id = row[0]
        brand = row[1]
        size = row[2]
        inventory = row[3]
        buying_price = row[4]
        selling_price = row[5]
        change_fee = row[6]
        # Handle exception when data has been inserted
        try:
            cursor.execute('''INSERT INTO summer_tires(prod_id, brand, size, inventory, buying_price, selling_price, change_fee) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)''',(prod_id, brand, size, inventory, buying_price, selling_price, change_fee)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

with open ('car_tire_winter.csv','r') as csv_file4:
    csv_reader4 = csv.reader(csv_file4)
    next(csv_reader4)
    for row in csv_reader4:
        prod_id = row[0]
        brand = row[1]
        size = row[2]
        inventory = row[3]
        buying_price = row[4]
        selling_price = row[5]
        change_fee = row[6]
        # Handle exception when data has been inserted
        try:
            cursor.execute('''INSERT INTO winter_tires(prod_id, brand, size, inventory, buying_price, selling_price, change_fee) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)''',(prod_id, brand, size, inventory, buying_price, selling_price, change_fee)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

# Database system start
secure_count = 0 # Count invalid password input, more than 3 times will quit the query
access_entry()

# cursor.close()
# cnx.close()