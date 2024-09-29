# Jamie Smith
# Main File

import user_inputs as ui
import conversion as conv
import hamming_weight as hw
import compare

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
    grouped_weights, term_mapping = hw.hamming_weight(terms_binary_array, all_terms)

    # Display the hamming weight groups
    hw.display_weight_groups(grouped_weights)

    # Combine terms using the Quine-McCluskey method
    combined_terms, prime_implicants = compare.combine_terms(grouped_weights, term_mapping)

    # Display the combined terms
    compare.display_combined_terms(combined_terms, prime_implicants)

    