import unittest
from binary2decimal import binary_to_decimal
from binary2decimal import decimal_to_binary

class TestNumeración(unittest.TestCase):
    def testBinario2Decimal(self):
        self.assertEqual(binary_to_decimal(('01011100'),92))

    def testDecimal2Binario(self):
        self.assertEqual(decimal_to_binary((97),'01100001'))


if __name__ == '__main__':
    unittest.main()