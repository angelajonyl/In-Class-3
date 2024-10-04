from PowerofTwo import *
 
if __name__ == "__main__":
    test_numbers = [8, 30036, 256]
    
    for num in test_numbers:
        result = PowerOfTwo.is_power_of_two(num)
        # Using the variable in the output
        if result:
            print(f"{num} is a power of 2.")
        else:
            print(f"{num} is not a power of 2.")