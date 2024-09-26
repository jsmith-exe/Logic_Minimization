#Jamie Smith
# Converter Integer to Binary format

def int_to_binary(minterms, num_inputs):
    minterm_binary_array = []
    for n in minterms:
        int_val = int(n)
        binary = bin(int_val)[2:].zfill(num_inputs)

        minterm_binary_array.append(binary)

    return minterm_binary_array
        