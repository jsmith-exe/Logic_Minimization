# Jamie Smith
# Main File

import user_inputs as ui
import conversion as conv
import hamming_weight as hw
import compare

if __name__ == "__main__":

    num_inputs = ui.get_inputs()
    minterms = ui.get_minterms(num_inputs)

    minterms_binary_array = conv.int_to_binary(minterms, num_inputs)
    grouped_weights, minterm_mapping = hw.hamming_weight(minterms_binary_array, minterms)

    hw.display_weight_groups(grouped_weights)

    combined_terms = compare.combine_terms(grouped_weights, minterm_mapping)

    compare.display_combined_terms(combined_terms)

    