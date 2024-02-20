# mypython_interpreter.py

class MyPythonInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        lines = code.split('\n')
        print(f"heollo! interpret")
        for line in lines:
            self.execute_line(line)

    def execute_line(self, line):
        tokens = line.split()
        print(f"hello! execute")
        if tokens:
            print(f"what index 0 '{tokens[0]}'", end=' ')
            if tokens[0] == "def":
                self.handle_function_definition(tokens)
            elif tokens[0] == "mult":
                self.handle_mult_statement(tokens)
            elif tokens[0] == "repeat":
                self.handle_repeat_statement(tokens)
            elif tokens[0] == "write":
                self.handle_print_statement(tokens)
            else:
                # Handle other statements or expressions
                pass

    def handle_function_definition(self, tokens):
  	
	
        pass

    def handle_mult_statement(self, tokens):
        print("Welcome to the Multiply Program!")
    
        # Get user input for two single-digit numbers
        num1 = get_single_digit_input("Enter the first single-digit number: ")
        num2 = get_single_digit_input("Enter the second single-digit number: ")

        # Perform multiplication
        result = multiply_numbers(num1, num2)

        # Print the result
        print(f"The result of {num1} * {num2} is: {result}")
    
    def handle_repeat_statement(self, tokens):
        print("Welcome to the Repeater Program!")
    
    
        char_to_repeat = input("Enter the character to repeat: ")
        num_repetitions = get_positive_integer_input("Enter the number of repetitions: ")
        repeated_string = repeat_character(char_to_repeat, num_repetitions)
        print(f"The result of repeating '{char_to_repeat}' {num_repetitions} times is: {repeated_string}")

    

  

    def handle_print_statement(self, tokens):
        if len(tokens) > 1 and tokens[1].startswith("(") and tokens[-1].endswith(")"):
            content = " ".join(tokens[1:])
            content = content[1:-1]  
            print(content)
        else:
            print("Invalid print statement")
def multiply_numbers(num1, num2):
        return num1 * num2
def get_single_digit_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and len(user_input) == 1:
            return int(user_input)
        else:
            print("Please enter a valid single-digit number.")

        pass
def repeat_character(char, repetitions):
        return char * repetitions
        pass
def get_positive_integer_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit() and int(user_input) > 0:
                return int(user_input)
            else:
                print("Please enter a valid positive integer.")



