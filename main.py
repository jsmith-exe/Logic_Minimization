# Jamie Smith
# Main File

import user_inputs as ui
import conversion as conv
import hamming_weight as hw

if __name__ == "__main__":

    num_inputs = ui.get_inputs()
    minterms = ui.get_minterms(num_inputs)

    minterms_binary_array = conv.int_to_binary(minterms, num_inputs)
    weight_groups = hw.hamming_weight(minterms_binary_array)

    print (minterms_binary_array)
    hw.display_weight_groups(weight_groups)