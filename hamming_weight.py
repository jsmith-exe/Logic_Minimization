# Jamie Smith
# Get Hamming Weight

def hamming_weight(binary_numbers):

    weight_groups = {}
    
    for binary in binary_numbers:
        # Calculate the Hamming weight
        weight = binary.count('1')
        
        # Group the binary numbers by their Hamming weight
        if weight not in weight_groups:
            weight_groups[weight] = []
        weight_groups[weight].append(binary)
    
    return weight_groups

def display_weight_groups(weight_groups):
   
    for weight in sorted(weight_groups.keys()):
        
        print(f"Hamming Weight {weight}: {weight_groups[weight]}")