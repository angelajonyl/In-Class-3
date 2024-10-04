# In-Class 3
# Angela Jonyl Reyes & Harlan Dela Rosa
# 1.	is_positive(): A function that will return True if its parameter is a positive number (i.e. float), and return False otherwise.
class RealNumbers:
    def __init__(self):
        self.number = 0
 
    def if_positive(self, num):
        self.number = num
        if self.number > 0:
            print("The number is positive")
        else:
            print("The number is negative")