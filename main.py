# Jamie Smith
# Main File

import int_to_binary as itb

if __name__ == "__main__":
    num_inputs = int(input("Input the number of inputs: "))
    minterms = str(input("Input the Minterms as an array: "))
    
    if (num_inputs != int):
        print("Error, number of nnputs must be an Integer")

    if (num_inputs > 26):
        print("Error, number of inputs must be less than 26!")

    minterms_array = []

    minterms_array = itb.int_to_binary(minterms)

    print (minterms_array)