class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        #for char in reversed(s):
        for char in s.reversed():
            current_value = roman_values[char]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value

        return total

sol=Solution()
print(sol.romanToInt("IV"))
print(sol.romanToInt("IIIV"))
print(sol.romanToInt("LVIIIV"))
print(sol.romanToInt("MCMXCIV"))