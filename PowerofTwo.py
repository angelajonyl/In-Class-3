# In-Class 3
# Angela Jonyl Reyes & Harlan Dela Rosa
#2.	is_power_of_two(): A function that will return True if its parameter is a power of 2 (e.g. 2, 4, 8, 16, 32), and return False otherwise. 
class PowerOfTwo:
 
    def is_power_of_two(n):
        # To check if the number is a power of 2
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
 
