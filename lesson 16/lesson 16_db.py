import sqlite3

sql_table_comp = """CREATE TABLE IF NOT EXISTS competetion (
  	competetion_id INTEGER PRIMARY KEY,
  	competetion_name VARCHAR,
  	world_record TIME,
  	set_data DATE
);
CREATE TABLE IF NOT EXISTS results (
  	competetion_id INTEGER ,
  	sportsman_id INTEGER PRIMARY KEY,
  	results TIME,
  	hold_date DATE,
  	city VARCHAR
);
CREATE TABLE IF NOT EXISTS sportman (
  	ranks INTEGER PRIMARY KEY,
  	sportsmans_id INTEGER,
  	sportsman_name VARCHAR,
  	year_of_birth DATE,
  	personal_record time,
  	country VARCHAR
);"""

inserts = """INSERT INTO competetion VALUES
	('1', 'run', '9:58', '2009-08-16'),
	('2', 'run', '10:10', '2010-10-22'),
	('3', 'run', '10:25', '2008-05-11'),
	('4', 'run', '10:30', '2008-03-07');

INSERT INTO results VALUES
	('1', '10', '9:58' , '2010-05-12','Moscow'),
	('2', '12', '10:10' , '2010-10-22', 'New Yourk'),
	('3', '15', '10:25' , '2008-05-11', 'Dubai'),
	('4', '2', '9:00' , '2008-05-11', 'Brazil');

INSERT INTO sportman VALUES
	('2', '10', 'Max', '1999-04-10','10:15','Russia'),
  	('3', '12', 'Donj', '2001-12-9','10:30','Brazil'),
  	('4', '15', 'Bony', '2002-10-15','10:35','USA'),
  	('1', '2', 'Bolt', '2006-2-3','09:58','Kenuy')
"""

selects = ("SELECT * FROM sportman", "SELECT competetion_name, world_record FROM competetion",)

with sqlite3.connect('my_db.sqlite') as connection:
    cursor = connection.cursor()
    for select in selects:
        data = cursor.execute(str(select))  # передаем список выборки(для пробы)
        for i in data:
            print(i)
