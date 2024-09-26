# Jamie Smith
# Main File

import user_inputs as ui
import conversion as conv

if __name__ == "__main__":

    num_inputs = ui.get_inputs()
    minterms = ui.get_minterms(num_inputs)

    minterms_binary_array = conv.int_to_binary(minterms, num_inputs)

    print (minterms_binary_array)