'''
2. Write a Python class to convert a Roman numeral to an integer.'''

class convertion:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(convertion().roman_to_int('MMMCMLXXXVI'))
print(convertion().roman_to_int('MMMM')) 
print(convertion().roman_to_int('C'))
