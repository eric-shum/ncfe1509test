import unittest

class test(unittest.TestCase):

    try:
        i = 0
        while i < 10:
            print(i)
            i += 1

    except:
        print("There is an error")

if __name__ == '__main__':
    unittest.main()