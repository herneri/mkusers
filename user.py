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

import pycurl
import json
from io import BytesIO

class user:
	API_URL = "https://randomuser.me/api/"
	
	def __init__(self, first, last, username, password, email, phoneNumber, dateRegistered, birthDate, gender):
		self.name = first + " " + last
		self.username = username
		self.password = password
		self.email = email
		self.birthDate = birthDate
		self.gender = gender
		self.phoneNumber = phoneNumber
		self.dateRegistered = dateRegistered

	@classmethod
	def createUser(cls):
		buffer = BytesIO()
		curl = pycurl.Curl()

		curl.setopt(curl.URL, cls.API_URL)
		curl.setopt(curl.WRITEDATA, buffer)
		curl.perform()
		curl.close()

		data = json.loads(buffer.getvalue())
		output = user(data["results"][0]["name"]["first"], data["results"][0]["name"]["last"],\
		data["results"][0]["login"]["username"], data["results"][0]["login"]["password"],\
		data["results"][0]["email"], data["results"][0]["phone"],\
		data["results"][0]["registered"]["date"], data["results"][0]["dob"]["date"],\
		data["results"][0]["gender"])

		return output

	def printUser(self):
		print(self.name)
		print(self.username)
		print(self.password)
		print(self.email)
		print(self.birthDate)
		print(self.gender)
		print(self.phoneNumber)
		print(self.dateRegistered)
		return
