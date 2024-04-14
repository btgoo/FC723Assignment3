class EuclideanAlgorithm:
    def __init__(self):
        pass  # No initialisation needed in this case

    def euclidean_algorithm(self, a, b):
        while b != 0:  # Loop until b becomes 0
            temp = b  # Store the current value of b in temp
            b = a % b  # Update b to the remainder when a is divided by b
            a = temp  # Update a to the previous value of b (stored in temp)
        return a  # Return the last non-zero remainder, which is the GCD


# Any number can be used, for this example, finding out GCD of 4 and 6
num1 = 4
num2 = 6
euclidean = EuclideanAlgorithm()    # Create an instance of EuclideanAlgorithm
gcd = euclidean.euclidean_algorithm(num1, num2)     # Call the method on the instance
print(f"The greatest common divisor of {num1} and {num2} is {gcd}")
