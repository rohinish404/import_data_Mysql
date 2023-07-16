#importing libraries
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

# input variables
database_name = ''
table_name = ''

#reading excel file
empdata = pd.read_excel('add_file_name_here', index_col=False)

#converting excel to csv
empdata.to_csv('add_file_name_here.csv', index=False)

#reading csv
new_data = pd.read_csv('add_file_name_here.csv',index_col=False)

#converting dataframe dtypes to dictonary
column_types = new_data.dtypes
column_types_dict = column_types.to_dict()

# creating new dictonary with sql dtypes
new_dict = {}
for i,key in column_types_dict.items():
    if key == 'O':
        new_dict[i] = 'VARCHAR(255)'
    elif key == 'int64':
        new_dict[i] = 'INT'
    elif key == 'int64':
        new_dict[i] = 'INT'
    elif key == 'float64':
        new_dict[i] = 'FLOAT'
    else:
        new_dict[i] = key
   
#connecting to MySql localhost
try:
    conn = msql.connect(host='localhost', user='root',  # write your Mysql username here
    password='')  # write your Mysql password here
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {database_name}")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

#creating table
try:
    conn = msql.connect(host='localhost', database=database_name, user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
        print('Creating table....') 

        create_table_query = f"CREATE TABLE {table_name} ("

        for column_name, column_type in new_dict.items():
            create_table_query += f"{column_name} {column_type}, "

        # Remove the trailing comma and space
        create_table_query = create_table_query[:-2]

        create_table_query += ")"




        cursor.execute(create_table_query)

        print("Table is created....")

        #loop through the data frame

        for i, row in new_data.iterrows():
            row = [None if pd.isna(value) else value for value in row]
    # here %s means string values
            placeholders = ', '.join(['%s'] * len(row))
            columns = ', '.join(new_data.columns)

            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            cursor.execute(sql, tuple(row))
            print("Record inserted")
            
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()

except Error as e:
        print("Error while connecting to MySQL", e)




