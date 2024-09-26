# Jamie Smith
# Collecting User Inputs

import conversion as conv

MAX_INPUTS = 26  # Maximum number of inputs

def get_inputs():
    while True:
        try:
            num_inputs = int(input("Input the number of inputs: "))
            if num_inputs <= 0 or num_inputs > MAX_INPUTS:
                print(f"Error, number of inputs must be between 1 and {MAX_INPUTS}!")
                continue
            return num_inputs
        except ValueError:
            print("Error: number of inputs must be an integer")

def get_minterms():
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
