# Jamie Smith
# Main File

import user_inputs as ui
import conversion as conv
import hamming_weight as hw
import compare
import epi

if __name__ == "__main__":

    # Collect inputs from the user      
    num_inputs = ui.get_inputs()
    minterms = ui.get_minterms(num_inputs)
    dont_cares = ui.get_dont_cares(num_inputs)

    # Combine minterms and dont care terms for processing
    all_terms = minterms + dont_cares

    # Convert all terms (minterms + dont cares) to binary
    terms_binary_array = conv.int_to_binary(all_terms, num_inputs)

    # Group terms based on hamming weight
    grouped_weights, term_mapping, minterm_mapping = hw.hamming_weight(terms_binary_array, all_terms, dont_cares)

    # Display the hamming weight groups
    hw.display_weight_groups(grouped_weights)

    # Combine terms using the Quine-McCluskey method
    combined_terms, prime_implicants = compare.combine_terms(grouped_weights, term_mapping)

    # Display the combined terms
    compare.display_combined_terms(combined_terms, prime_implicants)

    # Identify essential prime implicants
    essential_implicants, covered_minterms = epi.identify_essential_prime_implicants(prime_implicants, minterm_mapping)

    # Create the prime implicant chart
    chart = epi.create_prime_implicant_chart(prime_implicants, minterms)
    
    # Select essential prime implicants
    essential_implicants = epi.select_essential_prime_implicants(chart)

    # Determine remaining minterms not covered
    remaining_minterms = [m for m in minterms if m not in covered_minterms]

    # If there are remaining minterms, apply Petrick's method
    if remaining_minterms:
        petricks_solution = petricks_method(chart, remaining_minterms)
        print("Petrick's Method Solution (remaining prime implicants):", petricks_solution)

    print("Essential Prime Implicants:", essential_implicants)