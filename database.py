"""
    Copyright 2024 Eric Hernandez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sqlite3

class sqlite:
	def __init__(self, dbName):
		self.DB_NAME = dbName
	
	def setupDB(self):
		sql = """CREATE TABLE IF NOT EXISTS users(
					id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
					name VARCHAR(30) NOT NULL,
					username VARCHAR(10),
					password VARCHAR(20),
					email VARCHAR(30),
					birth_date VARCHAR(10),
					gender VARCHAR(7),
					phone_number VARCHAR(20),
					date_registered VARCHAR(20)
				)"""

		connection = sqlite3.connect(self.DB_NAME)
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.close()
		return

	def insertUser(self, user):
		sql = f"""INSERT INTO users(name, username, password, email, birth_date, gender,
				 phone_number, date_registered) VALUES(
				 	'{user.name}',
					'{user.username}',
					'{user.password}',
					'{user.email}',
					'{user.birthDate}',
					'{user.gender}',
					'{user.phoneNumber}',
					'{user.dateRegistered}'
				 )"""

		connection = sqlite3.connect(self.DB_NAME)
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.commit()
		connection.close()
		return
