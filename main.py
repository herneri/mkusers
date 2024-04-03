#!/usr/bin/env python3

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

from user import user
from database import sqlite
from time import sleep
import sys

if len(sys.argv) == 2 and sys.argv[1] == "h":
	print("usage: mkusers [DATABASE NAME] [NUMBER OF USERS]")
	exit(0)
elif len(sys.argv) < 3 or len(sys.argv) > 3:
	sys.stderr.write("mkusers: Improper amount of arguments, use 'mkusers h' for help \n")
	exit(1)

DATABASE_NAME = sys.argv[1]
USER_COUNT = int(sys.argv[2])

db = sqlite(DATABASE_NAME)
db.setupDB()

for i in range(USER_COUNT):
	user = user.createUser()
	db.insertUser(user)

	if i % 5 == 0:
		sleep(1.5)
