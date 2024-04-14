class EuclideanAlgorithm:
    def euclidean_algorithm(self, a, b):
        if b == 0:  # Check base case
            return a    # If b is 0, a is its greatest common divisor
        else:
            return self.euclidean_algorithm(b, a % b)   # Recursively call the function

def get_valid_input(prompt):    # Function to get valid input from the user (positive integers)
    while True:  # Keep looping until valid input is received
        try:
            value = int(input(prompt))  # Try to convert user input to an integer
            if value <= 0:
                # If the input is not positive, prompt the user to enter a positive integer
                print("Please enter a positive integer.")
                continue  # Continue to the next iteration of the loop
            return value  # If input is valid, return the value
        except ValueError:
            # If the input cannot be converted to an integer, prompt the user to enter a valid integer
            print("Invalid input. Please enter a valid integer.")



if __name__ == "__main__":
    num1 = get_valid_input("Enter the first positive integer: ")    # Get the first value
    num2 = get_valid_input("Enter the second positive integer: ")   # Get the second value

    euclidean = EuclideanAlgorithm()  # Create an instance of EuclideanAlgorithm
    gcd = euclidean.euclidean_algorithm(num1, num2)  # Call the method on the instance
    print(f"The greatest common divisor of {num1} and {num2} is {gcd}")

