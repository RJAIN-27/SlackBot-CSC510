# Python code to demonstrate working of unittest
import unittest
import json
import KeywordExtraction as ke

with open("/home/ubuntu/CSC510-23/Code/data.json") as json_file:
    data = json.load(json_file)

libraries = data["libraries"]

class TestKEMethods(unittest.TestCase):
    # usecase 1 - happy flow
    def test_KELib1(self):
        self.assertIsNotNone(ke.keywordExtraction("I wanna know about numpy, scipy, keras and someLib","Sheet1"))

    def test_KEFun1(self):
        self.assertIsNotNone(ke.keywordExtraction("I wanna know about sin, cos, and tan","Sheet3"))

if __name__ == '__main__':
    unittest.main()
