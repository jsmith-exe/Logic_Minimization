# Jamie Smith
# Compare the Hamming Groups

def combine_terms(weight_groups, minterm_mapping):
  
    combined_terms = []
    weights = sorted(weight_groups.keys())
    
    for i in range(len(weights) - 1):
        current_weight = weights[i]
        next_weight = weights[i + 1]

        # Compare terms from current and next weight groups
        for term1 in weight_groups[current_weight]:
            for term2 in weight_groups[next_weight]:
                # Check if they differ by exactly one bit
                if differ_by_one(term1, term2):
                    combined_term = combine_binary_terms(term1, term2)
                    if (combined_term, term1, term2) not in combined_terms:
                        # Retrieve the original minterms from the mapping
                        minterm1 = minterm_mapping[term1]
                        minterm2 = minterm_mapping[term2]
                        combined_terms.append((combined_term, minterm1, minterm2))

    return combined_terms



def differ_by_one(term1, term2):
  
    # Count the number of differing bits
    diff_count = sum(b1 != b2 for b1, b2 in zip(term1, term2))
    return diff_count == 1

def combine_binary_terms(term1, term2):
  
    combined = []
    for b1, b2 in zip(term1, term2):
        combined.append(b1 if b1 == b2 else '-')
    return ''.join(combined)

def display_combined_terms(combined_terms):
    
    print("Combined Terms with Minterms:")
    
    # Debugging output to check the structure of combined_terms
    print("Combined terms data structure:", combined_terms)

    for item in combined_terms:
        # Ensure each item is a tuple of three elements
        if len(item) == 3:
            combined, term1, term2 = item
            print(f"Combined: {combined} from {term1} and {term2}")
        else:
            print(f"Unexpected item structure: {item}")
