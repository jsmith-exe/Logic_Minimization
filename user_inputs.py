# Jamie Smith
# Collecting User Inputs

MAX_INPUTS = 26  # Maximum number of inputs

def get_inputs():
    """Get the number of inputs from the user with validation."""
    while True:
        try:
            num_inputs = int(input("Input the number of inputs: "))
            if num_inputs <= 0 or num_inputs > MAX_INPUTS:
                print(f"Error, number of inputs must be between 1 and {MAX_INPUTS}!")
                continue
            return num_inputs
        except ValueError:
            print("Error: number of inputs must be an integer")

def get_minterms(num_inputs):
    """Get the list of minterms from the user with validation."""
    while True:
        minterms_input = input("Input the minterms as a comma-separated list (e.g., 1,2,3): ")
        try:
            minterms = [int(x) for x in minterms_input.split(',')]
            # Validate that minterms are within the correct range
            if any(m < 0 or m >= (1 << num_inputs) for m in minterms):
                print(f"Error: minterms must be between 0 and {(1 << num_inputs) - 1}")
                continue
            return minterms
        except ValueError:
            print("Error: minterms must be integers separated by commas")

def get_dont_cares(num_inputs):
    """Get the list of don't care terms from the user with validation."""
    while True:
        dont_cares_input = input("Input the don't care terms as a comma-separated list (or press Enter if none): ")
        if not dont_cares_input.strip():
            return []  # If the user presses Enter, return an empty list
        try:
            dont_cares = [int(x) for x in dont_cares_input.split(',')]
            # Validate that don't care terms are within the range [0, 2^num_inputs - 1]
            max_value = (1 << num_inputs) - 1
            if all(0 <= dc <= max_value for dc in dont_cares):
                return dont_cares
            else:
                print(f"Error: don't care terms must be between 0 and {max_value}")
        except ValueError:
            print("Error: don't care terms must be integers separated by commas")
