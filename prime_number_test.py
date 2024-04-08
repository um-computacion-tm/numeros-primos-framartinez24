import unittest

#code
def is_prime(x):
    if x < 2 and x != 1:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True
    

#test
class primeTest(unittest.TestCase):
    def test_1(self):
        result = is_prime(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = is_prime(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_prime(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_prime(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_prime(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_prime(6)
        self.assertEqual(result, False)

    def test_7(self):
        result = is_prime(7)
        self.assertEqual(result, True)

    def test_8(self):
        result = is_prime(8)
        self.assertEqual(result, False)

    def test_9(self):
        result = is_prime(9)
        self.assertEqual(result, False)

    def test_10(self):
        result = is_prime(10)
        self.assertEqual(result, False)

    def test_11(self):
        result = is_prime(11)
        self.assertEqual(result, True)

    def test_12(self):
        result = is_prime(12)
        self.assertEqual(result, False)

    def test_13(self):
        result = is_prime(13)
        self.assertEqual(result, True)

    def test_14(self):
        result = is_prime(14)
        self.assertEqual(result, False)

    def test_15(self):
        result = is_prime(15)
        self.assertEqual(result, False)

    def test_49(self):
        result = is_prime(6)
        self.assertEqual(result, False)

    def test_59(self):
        result = is_prime(59)
        self.assertEqual(result, True)

    def test_97(self):
        result = is_prime(97)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
