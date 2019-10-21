# Python code to demonstrate working of unittest 
import unittest 
import kwx
from mock import patch
import json
import openpyxl as xl

def mock_keyword_extraction(a):
        list=a.split(' ')
        ans_list=[]
        length=len(list)
        i=0
        print list
        wb = xl.load_workbook('libraryFile.xlsx')
        sheet = wb['Sheet1']
        libInfo = {}
        for row in range(2 , sheet.max_row + 1):
            libInfo[sheet.cell(row, 1).value] = sheet.cell(row, 2).value
        while i<length:
            for r in (libInfo):
                if list[i] in r: 
                    ans_list.append(list[i])
            i=i+1   
        print ans_list    

def read_from_json_and_test(a):
    list=a.split(' ')
    with open("data.json") as json_file:
        data = json.load(json_file)
    i=0
    ans_list=[]
    length=len(list)    
    while i<length:
        for r in (data):
            if list[i] in r: 
                ans_list.append(list[i])
        i=i+1        

    print ans_list  

class TestStringMethods(unittest.TestCase): 
	
	@patch('kwx.keywordExtraction', side_effect=mock_keyword_extraction)
	def test_strings_a(self, keywordExtraction): 
		self.assertEqual(kwx.keywordExtraction("know numpy pandas"), read_from_json_and_test("know numpy pandas")) 

	# Returns True if the string is in upper case. 
	def test_upper(self):		 
		self.assertEqual('foo'.upper(), 'FOO') 

	# Returns TRUE if the string is in uppercase 
	# else returns False. 
	def test_isupper(self):		 
		self.assertTrue('FOO'.isupper()) 
		self.assertFalse('Foo'.isupper()) 

	# Returns true if the string is stripped and 
	# matches the given output. 
	def test_strip(self):		 
		s = 'geeksforgeeks'
		self.assertEqual(s.strip('geek'), 'sforgeeks') 

	# Returns true if the string splits and matches 
	# the given output. 
	def test_split(self):		 
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world']) 
		with self.assertRaises(TypeError): 
			s.split(2) 

if __name__ == '__main__': 
	unittest.main() 
