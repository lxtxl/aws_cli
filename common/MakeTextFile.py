#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

class MakeTextFile:
	fileName=""

	def __init__(self,fileName):
		self.fileName = fileName

	def writeSave(self, str):
		if os.path.isfile(self.fileName):
			f = open(self.fileName, 'a')
		else:
			f = open(self.fileName, 'w')
		f.write(str)
		f.close()

	def writeSaveln(self, str):
		if os.path.isfile(self.fileName):
			f = open(self.fileName, 'a')
		else:
			f = open(self.fileName, 'w')
		f.write(str)
		f.write("\n")
		f.close()

	def writeMultiSave(self, str):
		if os.path.isfile(self.fileName):
			f = open(self.fileName, 'a')
		else:
			f = open(self.fileName, 'w')
		f.writelines(str)
		f.close()


	def closeFile(self):
		pass

	def printMessage(self, message):
		print(message)

if __name__ == "__main__":
	textFile = MakeTextFile("test.txt")
	textFile.writeSave("hello")
