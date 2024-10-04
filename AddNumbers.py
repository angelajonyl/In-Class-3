# In-Class 3
# Angela Jonyl Reyes & Harlan Dela Rosa
# 4.	sum_of_digits(): A function that takes an integer parameter and adds up its individual digits, returning the sum of its digits
class AddNumbers:
    def __init__(self):
        self.total_number = 0
 
    def sum_of_digits(self, digits):
        self.total_number = 0
        while digits > 0:
            self.total_number += digits % 10  
            digits //= 10  
        return self.total_number  