# Jamie Smith
# Main File

import conversion as conv

if __name__ == "__main__":
    try:
        num_inputs = int(input("Input the number of inputs: "))
        if (num_inputs > 26):
            print ("Error, number of inputs must be less than 26!")
            exit()
    except ValueError:
        print ("Error: number of inputs must be an integer")
    
    # Ensure consistent use of minterms_input
    minterms_input = input("Input the minterms as a comma-separated list (e.g., 1,2,3): ")

    try:
        minterms = [int(x) for x in minterms_input.split(',')]
    except ValueError:
        print("Error: minterms must be integers separated by commas")
        exit()

    minterms_binary_array = conv.int_to_binary(minterms, num_inputs)

    print (minterms_binary_array)