# Jamie Smith
# Get Hamming Weight

def hamming_weight(minterms_binary_array, terms, dont_cares):
    """Calculate Hamming weights of binary terms and return weight groups, minterm mapping, and terms mapping."""
    
    weight_groups = {}
    minterm_mapping = {}
    terms_mapping = {}  # To store mapping for all terms including don't cares

    # Convert dont_cares to a set for faster lookups
    dont_care_set = set(dont_cares)

    for i, binary_string in enumerate(minterms_binary_array):
        weight = binary_string.count('1')
        
        # Group by Hamming weight
        if weight not in weight_groups:
            weight_groups[weight] = []
        weight_groups[weight].append(binary_string)

        # Always map to terms_mapping
        terms_mapping[binary_string] = terms[i]  # Store mapping for all terms

        # Only map to minterm_mapping if the term is not a don't care
        if terms[i] not in dont_care_set:
            minterm_mapping[binary_string] = terms[i]  # Store mapping from binary string to original minterm

    return weight_groups, terms_mapping, minterm_mapping


def display_weight_groups(weight_groups):
  
    for weight in sorted(weight_groups.keys()):
        print(f"Hamming Weight {weight}: {weight_groups[weight]}")
