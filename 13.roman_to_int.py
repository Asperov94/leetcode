class Solution:
    def romanToInt(self, s: str) -> int:
        rom={
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        sum = 0
        
        for i in range(len(s)):
            if s[0:2] in rom:
                sum+=rom[s[0:2]]
                s= s.replace(s[0:2], '', 1)
            elif s[0:1]in rom:
                sum+=rom[s[0:1]]
                s = s.replace(s[0:1], '', 1)
        return sum
