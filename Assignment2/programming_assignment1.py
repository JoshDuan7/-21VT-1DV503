from enum import Flag
import os
import csv
import mysql.connector
from mysql.connector import errorcode
cnx = mysql.connector.connect(host='localhost',
                              port='3306',
                              user='root',
                              passwd='rootroot',
                              )
# Note! Please put the .csv files in the same directory(folder) as this .py file.

# Database name, group members: Yuyao Duan, Fredric Eriksson 
DB_NAME = 'Duan_Eriksson' 

cursor = cnx.cursor()

# Create database
def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Create table planets for 'planets.csv'
def create_table_planets(cursor):
    create_planets = "CREATE TABLE planets ( \
                    name varchar(25) NOT NULL, \
                    rotation_period varchar(50), \
                    orbital_period varchar(50), \
                    diameter varchar(50), \
                    climate varchar(50), \
                    gravity varchar(50), \
                    terrain varchar(50), \
                    surface_water varchar(50), \
                    population varchar(50), \
                    PRIMARY KEY (name) \
                   )ENGINE=InnoDB"
    try: # Handle table creation exception
        print("Creating table planets: ") 
        cursor.execute(create_planets)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists! ")
        else:
            print(err.msg)
    else:
        print("OK")      

# Create table species for 'species.csv'
def create_table_species(cursor):
    create_species = "CREATE TABLE species ( \
                   sp_name varchar(25) NOT NULL, \
                   classification varchar(50), \
                   designation varchar(50), \
                   average_height varchar(50), \
                   skin_colors varchar(50), \
                   hair_colors varchar(50) , \
                   eye_colors varchar(50), \
                   average_lifespan varchar(50), \
                   language varchar(50), \
                   homeworld varchar(50), \
                   PRIMARY KEY (sp_name) \
                  ) ENGINE=InnoDB"
    # Handle table creation exception
    try: 
        print("Creating table species: ")
        cursor.execute(create_species)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Create a table for question 5 calculation
def create_table_calcu(cursor):
    create_calcu = "CREATE TABLE calcu ( \
                   sp_name varchar(25) NOT NULL, \
                   classification varchar(25), \
                   average_lifespan int (11), \
                   PRIMARY KEY (sp_name) \
                  ) ENGINE=InnoDB"
    try:
        print("Creating table calcu: ")
        cursor.execute(create_calcu)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Function for return to main menu
def return_to_menu(flag):
    if flag == False:
        print()
        input("Please click any key to continue: ")
        print()
        flag = True
        return flag

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
        cursor.execute('DROP TABLE IF EXISTS planets')
        create_table_planets(cursor)
        cursor.execute('DROP TABLE IF EXISTS species')
        create_table_species(cursor)
        cursor.execute('DROP TABLE IF EXISTS calcu')
        create_table_calcu(cursor)
    else:
        print(err)

# Read planets.csv to database, please put the .csv in the same directory of this .py file
with open ('planets.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        name = row[0]
        rotation_period = row[1]
        orbital_period = row[2]
        diameter = row[3]
        climate = row[4]
        gravity = row[5]
        terrain = row[6]
        surface_water = row[7]
        population = row[8]
        # Handle exception when data has been inserted
        try:
            cursor.execute("INSERT INTO planets(name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population)\
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

# Read species.csv to database, please put the .csv in the same directory of this .py file
with open ('species.csv','r') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    next(csv_reader2)
    for row in csv_reader2:
        sp_name = row[0]
        classification= row[1]
        designation = row[2]
        average_height = row[3]
        skin_colors = row[4]
        hair_colors = row[5]
        eye_colors = row[6]
        average_lifespan = row[7]
        language = row[8]
        homeworld = row[9]
        # Handle exception when data has been inserted
        try:
            cursor.execute('''INSERT INTO species(sp_name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',(sp_name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, language, homeworld)) 
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()

# Main menu 
flag = True
while(flag):
    print("1. List all planets.")
    print("2. Search for planet details.")
    print("3. Search for species with height higher than given number.")
    print("4. What is the most likely desired climate of the given species?")
    print("5. What is the average lifespan per species classification?")
    print("0. Quit")
    
    # Receive user input
    selection = input("Enter number: ")
    if selection.isdigit() and -1 < int(selection) < 6: # solve if user inputs anything else than desired values.
        selection = int(selection)
        # Selection 1 answers question 1 
        if selection == 1:
            query = "SELECT name FROM planets"
            cursor.execute(query)
            print("All planets in the database are: ")
            # Print all planets in database
            for name in cursor:
                for i in name:
                    print(">",i)
            flag = False
            flag = return_to_menu(flag)
        
        # Selection 2 answers question 2 
        elif selection == 2:
            planet_name = input("Please enter the name of the planet: ")
            planet_name2 = planet_name.lower()
            ident = [] # To find if the planet is in the database or not
            query = (''' SELECT name FROM planets ''')
            cursor.execute(query)
            for name in cursor:
                for i in name:
                    ident.append(i.lower())
            if planet_name2 not in ident:
                print("Planet not found")
                flag = False
                flag = return_to_menu(flag)
            else:
                query = (('''SELECT rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population
                            FROM planets
                            WHERE name = "{}" ''').format(planet_name))
                cursor.execute(query)
                for(rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population) in cursor:
                    # Print all details of the input planet
                    print("> rotation_period: {:<10}\n> orbital_period: {:<10}\n> diameter: {:<10}\n> climate: {:<10}\n> gravity: {:<10}\n> terrain: {:<10}\n> surface_water: {:<10}\n> population: {:<10}".format\
                        (rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population))
                flag = False
                flag = return_to_menu(flag)
        
        # Selection 3 answers question 3 
        elif selection == 3:
            average_height = input("Enter a height for query: ")
            if average_height.isdigit(): # To make sure that the user types a digit
                average_height = int(average_height)
                query = ("SELECT sp_name, average_height FROM species ")
                cursor.execute(query)
                lst1 = []
                lst2 = []
                for i in cursor:
                    lst1.append(i)
                for j in lst1:
                    if j[1] != 'NA': # Filter the species without height information which showing 'NA' in the table
                        height = int(j[1])
                        if height > average_height:
                            lst2.append(j)
                if not lst2:
                    print(f"\nNo species found with height higher than {average_height}.")  
                    flag = False
                    flag = return_to_menu(flag)
                else:
                    print(f"\nThe species with height higher than {average_height}: ")  
                    for sp in lst2:
                        print(">", sp[0] + ":  " + sp[1])
                    flag = False
                    flag = return_to_menu(flag)
            else:
                print("Invalid Input")
                flag = False
                flag = return_to_menu(flag)
        
        # Selection 4 answers question 4
        elif selection == 4:
            species_name = input("Please enter the name of the specie for query: ")
            species_name2 = species_name.lower()
            ident = [] # To identify if the specie is in the database.
            query = ('''SELECT sp_name FROM species''')
            cursor.execute(query)
            for sp_name in cursor:
                for i in sp_name:
                    ident.append(i.lower())
            if species_name2 not in ident:
                print("Species not found")
                flag = False
                flag = return_to_menu(flag)
            else:
                query1 = ('''SELECT homeworld FROM species WHERE sp_name= "{}" '''.format(species_name))
                cursor.execute(query1)
                for i in cursor:
                    for j in i:
                        if j == 'NA': # Identify the species without 'homeworld' which means it has not desired climate in database
                            print(f"\n>The most desired climate for {species_name} is : NA") 
                        else:
                            # Query for the species has 'homeworld'
                            query2 = (('''SELECT planets.climate
                                        FROM planets 
                                        JOIN species ON species.homeworld = planets.name
                                        WHERE species.sp_name = "{}" ''').format(species_name))          
                            cursor.execute(query2)
                            for climate in cursor:
                                for i in climate:
                                    print(">The most likely desired climate for " + species_name + " is : {}".format(i))
                flag = False
                flag = return_to_menu(flag)
        
        # Selection 5 answers question 5 
        elif selection == 5:
            print("The average lifespan per species classification: ")
            lst1 = []
            # Query species, classification, average_lifespan from table species
            query1 = ('''SELECT sp_name, classification, average_lifespan
                        FROM species
                        WHERE classification != 'NA' AND average_lifespan != 'NA' AND  average_lifespan != 'indefinite' ''')
            cursor.execute(query1)
            # Save the above query result to list lst1
            for i in cursor:
                lst1.append(list(i))
            # Insert the result to the table calcu for further query, which the average_lifespan turns to integer
            for i in lst1:
                try:
                    cursor.execute('''INSERT INTO calcu (sp_name, classification, average_lifespan) VALUES (%s,%s,%s)''',(i[0], i[1],int(i[2])) )
                    cnx.commit()
                except mysql.connector.Error as err:
                    cnx.rollback()
            # Query from table calcu for the requirement of question 5
            query2 = ('''SELECT classification, avg(average_lifespan) AS al
                        FROM calcu
                        GROUP BY classification
                        ORDER BY al ASC ''') # result will be shown as ASC
            cursor.execute(query2)   
            # Print average lifespan per species classification
            for i in cursor:
                decimal = i[1] 
                decimal = round(decimal, 2) # Fixing decimal values
                print('>', i[0], decimal) 
            flag = False
            flag = return_to_menu(flag)
        
        # Selection 0 quit the query system
        elif selection == 0:
            print("Query exit!")
            break
    else:
        print("please select one of the digits")
        flag = False
        flag = return_to_menu(flag)
cursor.close()
cnx.close()