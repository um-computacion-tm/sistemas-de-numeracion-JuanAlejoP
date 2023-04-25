def binary_to_decimal(binary):
    
    decimal = 0
    binary = binary[::-1]

    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i

    return decimal


def binary_to_octal(binary):

    decimal = binary_to_decimal(binary)
    octal = ''

    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal


def binary_to_hexadecimal(binary):
    
    decimal = binary_to_decimal(binary)
    hexadecimal_digits = '0123456789ABCDEF'
    hexadecimal = ''

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal //= 16

    return hexadecimal


def decimal_to_binary(decimal):

    binary = ''

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary


def decimal_to_octal(decimal):
    
    octal = ''

    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    return octal


def decimal_to_hexadecimal(decimal):

    hexadecimal_digits = '0123456789ABCDEF'
    hexadecimal = ''

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal //= 16

    return hexadecimal


def octal_to_decimal(octal):
    
    decimal = 0
    octal = str(octal)[::-1]

    for i in range(len(octal)):
        decimal += int(octal[i]) * 8 ** i

    return decimal


def octal_to_binary(octal):
    
    decimal = octal_to_decimal(octal)
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
        
    return binary


def octal_to_hexadecimal(octal):
    
    decimal = octal_to_decimal(octal)
    hexadecimal_digits = '0123456789ABCDEF'
    hexadecimal = ''
    
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal //= 16
        
    return hexadecimal


def hexadecimal_to_decimal(hexadecimal):
    
    decimal = 0
    hexadecimal = hexadecimal[::-1]
    hexadecimal_digits = '0123456789ABCDEF'
    
    for i in range(len(hexadecimal)):
        decimal += hexadecimal_digits.index(hexadecimal[i]) * 16 ** i
        
    return decimal


def hexadecimal_to_binary(hexadecimal):
    
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = ''
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
        
    return binary


def hexadecimal_to_octal(hexadecimal):
    
    decimal = int(hexadecimal, 16)
    octal = decimal_to_octal(decimal)
	
    return octal