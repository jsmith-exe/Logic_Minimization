# Jamie Smith
# Compare the Hamming Groups

def combine_terms(weight_groups, term_mapping):
    """Continuously combine terms until no further combinations are possible."""

    combined_terms = []  # Store all combined terms across iterations
    prime_implicants = []  # Store terms that can no longer be combined
    weights = sorted(weight_groups.keys())  # Initial weight groups

    while True:
        new_combinations = []  # To store combinations found in each round
        marked_terms = set()  # To keep track of combined terms

        # Compare adjacent Hamming weight groups
        for i in range(len(weights) - 1):
            current_weight = weights[i]
            next_weight = weights[i + 1]

            for term1 in weight_groups[current_weight]:
                for term2 in weight_groups[next_weight]:
                    # Check if they differ by exactly one bit
                    if differ_by_one(term1, term2):
                        combined_term = combine_binary_terms(term1, term2)
                        # Avoid duplicates and save combination with original minterms
                        if (combined_term, term1, term2) not in new_combinations:
                            # Retrieve original minterms from the mapping
                            minterm1 = term_mapping[term1]
                            minterm2 = term_mapping[term2]

                            # Ensure minterm1 and minterm2 are both lists
                            if not isinstance(minterm1, list):
                                minterm1 = [minterm1]
                            if not isinstance(minterm2, list):
                                minterm2 = [minterm2]

                            # Combine the lists and remove duplicates
                            combined_minterms = sorted(set(minterm1 + minterm2))

                            # Update the mapping for the new combined term
                            term_mapping[combined_term] = combined_minterms

                            new_combinations.append((combined_term, term1, term2))
                            marked_terms.add(term1)
                            marked_terms.add(term2)

        # Collect prime implicants (terms that were not combined in this round)
        for weight in weights:
            for term in weight_groups[weight]:
                # Only add terms that were not marked (i.e., not combined)
                if term not in marked_terms and term not in prime_implicants:
                    prime_implicants.append(term)

        # If no new combinations were found, break the loop
        if not new_combinations:
            break

        # Update combined terms and weight groups for the next iteration
        combined_terms.extend(new_combinations)
        weight_groups = update_weight_groups(new_combinations)
        weights = sorted(weight_groups.keys())  # Recalculate weights for the next round

    return combined_terms, prime_implicants


def differ_by_one(term1, term2):
    """Check if two binary terms differ by exactly one bit."""
    diff_count = sum(b1 != b2 for b1, b2 in zip(term1, term2))
    return diff_count == 1


def combine_binary_terms(term1, term2):
    """Combine two binary terms by replacing differing bits with a dash ('-')."""
    return ''.join(b1 if b1 == b2 else '-' for b1, b2 in zip(term1, term2))


def update_weight_groups(combined_terms):
    """Update the weight groups after a round of combinations."""
    weight_groups = {}
    for term, _, _ in combined_terms:
        weight = term.count('1')  # Calculate Hamming weight
        if weight not in weight_groups:
            weight_groups[weight] = []
        weight_groups[weight].append(term)
    return weight_groups


def display_combined_terms(combined_terms, prime_implicants):
    """Display combined terms and remaining prime implicants."""
    print("Combined Terms with Minterms:")
    print("Combined terms data structure:", combined_terms)

    for item in combined_terms:
        if len(item) == 3:
            combined, term1, term2 = item
            print(f"Combined: {combined} from {term1} and {term2}")
        else:
            print(f"Unexpected item structure: {item}")

    # Display prime implicants
    print("\nPrime Implicants (terms that cannot be combined further):")
    for implicant in prime_implicants:
        print(implicant)
