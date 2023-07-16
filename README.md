# import_data_Mysql

This python script is useful if you want to add data to your Mysql database from an excel file. You do not need to create table. Just add the link to the file and it will do everything on it's own.
To get this script running, 

Setting up
--------------

You need to install certain libraries before running this script.

### Installing using pip


```bash
  pip install pandas
```

```bash
  pip install mysql-connector-python
```



## Run Locally

Clone the project

```bash
  git clone https://github.com/rohinish404/import_data_Mysql
```

Go to the project directory

```bash
  cd import_data_Mysql
```
--------------
#### But before running the file you should add the filename, database_name, table_name, your Mysql username and password in the file (See comments for where to add).
--------------

Run file

```bash
  python main.py
```

## Additional

It's better to move the file to the cloned folder. 
Currently it converts the excel file to csv so it's better to add link of an excel file.
And it supports INT,VARCHAR and FLOAT only for now. The script can be changed accordingly.




    

