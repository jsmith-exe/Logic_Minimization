# Jamie Smith
# Get Hamming Weight

def hamming_weight(minterms_binary_array, minterms):
   
    weight_groups = {}
    minterm_mapping = {}

    for i, binary_string in enumerate(minterms_binary_array):
        weight = binary_string.count('1')
        if weight not in weight_groups:
            weight_groups[weight] = []
        weight_groups[weight].append(binary_string)
        minterm_mapping[binary_string] = minterms[i]  # Store mapping from binary string to original minterm

    return weight_groups, minterm_mapping

def display_weight_groups(weight_groups):
  
    for weight in sorted(weight_groups.keys()):
        print(f"Hamming Weight {weight}: {weight_groups[weight]}")
