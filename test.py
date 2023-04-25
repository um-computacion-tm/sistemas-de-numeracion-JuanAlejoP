import unittest
from binary2decimal import binary_to_decimal, binary_to_octal, binary_to_hexadecimal, decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal, octal_to_binary, octal_to_decimal, octal_to_hexadecimal, hexadecimal_to_binary, hexadecimal_to_decimal, hexadecimal_to_octal


class TestNumerción(unittest.TestCase):
    
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('101010'), 42)
        self.assertEqual(binary_to_decimal('11111111'), 255)
        self.assertEqual(binary_to_decimal('0'), 0)
        
    def test_binary_to_octal(self):
        self.assertEqual(binary_to_octal('101010'), '52')
        self.assertEqual(binary_to_octal('11111111'), '377')
        self.assertEqual(binary_to_octal('0'), '0')
        
    def test_binary_to_hexadecimal(self):
        self.assertEqual(binary_to_hexadecimal('101010'), '2A')
        self.assertEqual(binary_to_hexadecimal('11111111'), 'FF')
        self.assertEqual(binary_to_hexadecimal('0'), '0')
        
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(42), '101010')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(0), '0')
        
    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal(42), '52')
        self.assertEqual(decimal_to_octal(255), '377')
        self.assertEqual(decimal_to_octal(0), '0')
        
    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimal_to_hexadecimal(42), '2A')
        self.assertEqual(decimal_to_hexadecimal(255), 'FF')
        self.assertEqual(decimal_to_hexadecimal(0), '0')
        
    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal('52'), 42)
        self.assertEqual(octal_to_decimal('377'), 255)
        self.assertEqual(octal_to_decimal('0'), 0)
        
    def test_octal_to_binary(self):
        self.assertEqual(octal_to_binary('52'), '101010')
        self.assertEqual(octal_to_binary('377'), '11111111')
        self.assertEqual(octal_to_binary('0'), '0')
        
    def test_octal_to_hexadecimal(self):
        self.assertEqual(octal_to_hexadecimal('52'), '2A')
        self.assertEqual(octal_to_hexadecimal('377'), 'FF')
        self.assertEqual(octal_to_hexadecimal('0'), '0')
        
    def test_hexadecimal_to_decimal(self):
        self.assertEqual(hexadecimal_to_decimal('2A'), 42)
        self.assertEqual(hexadecimal_to_decimal('FF'), 255)
        self.assertEqual(hexadecimal_to_decimal('0'), 0)
        
    def test_hexadecimal_to_binary(self):
        self.assertEqual(hexadecimal_to_binary('2A'), '101010')
        self.assertEqual(hexadecimal_to_binary('FF'), '11111111')
        self.assertEqual(hexadecimal_to_binary('0'), '0')
        
    def test_hexadecimal_to_octal(self):
        self.assertEqual(hexadecimal_to_octal('2A'), '52')
        self.assertEqual(hexadecimal_to_octal('FF'), '377')
        self.assertEqual(hexadecimal_to_octal('0'), '0')


if __name__ == '__main__':
    unittest.main()