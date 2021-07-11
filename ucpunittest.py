import unittest

class Test(unittest.TestCase):
	# test should start with test prefix
	def test_firstTest(self):
		print("This is to show case the simple Test1")

    def test_secTest(self):
        print("This is to show case the simple Test2")

if __name__ == "__main__":
	unittest.main()