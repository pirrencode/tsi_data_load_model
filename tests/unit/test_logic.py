# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# All rights reserved.

import pytest

def extract(data):
    return [d * 2 for d in data]

def generate(data):
    return [d + 10 for d in data]

def generate_augmented(data):
    augmented_data = []
    for d in data:
        augmented_data.append(d + 10)  # Original transformation
        augmented_data.append(d + 10 + 1)  # Synthetic augmentation
    return augmented_data

def transfer(data):
    return [d - 5 for d in data]  # Example transformation

def load(data):
    # Load data into the final storage system
    return sum(data)  # Example aggregation for testing purposes

def test_extract():
    data = [1, 2, 3]
    result = extract(data)
    assert result == [2, 4, 6], "The extract function should double each element."

def test_generate():
    data = [2, 4, 6]
    result = generate(data)
    assert result == [12, 14, 16], "The generate function should add 10 to each element."

def test_transfer():
    data = [12, 14, 16]
    result = transfer(data)
    assert result == [7, 9, 11], "The transfer function should subtract 5 from each element."

def test_load():
    data = [7, 9, 11]
    result = load(data)
    assert result == 27, "The load function should sum all elements."

def test_complete_egtl_process():
    data = [1, 2, 3]
    result = load(transfer(generate(extract(data))))
    assert result == 27, "The complete EGTL process should result in 27."    

def test_generate_with_augmentation():
    data = [10, 20, 30]
    expected_output = [20, 21, 30, 31, 40, 41]  # Expected after transformation and augmentation
    result = generate_augmented(data)
    assert result == expected_output, "The generate function should transform and augment the data correctly."

def test_augmentation_length():
    data = [10, 20, 30]
    result = generate_augmented(data)
    assert len(result) == 2 * len(data), "The generate function should double the length of the input data due to augmentation."

def test_generate_with_zero():
    data = [0, 0, 0]
    assert generate_augmented(data) == [10, 11, 10, 11, 10, 11], "Should handle zeros by adding 10 and augmenting correctly."

def test_generate_with_same_elements():
    data = [2, 2, 2]
    assert generate_augmented(data) == [12, 13, 12, 13, 12, 13], "Should process identical elements correctly."

def test_generate_with_large_numbers():
    data = [100, 200, 300]
    assert generate_augmented(data) == [110, 111, 210, 211, 310, 311], "Should handle large numbers and augment them correctly."

def test_complete_egtl_process_with_augmentation():
    data = [1, 2, 3]
    result = load(transfer(generate_augmented(extract(data))))
    expected_result = sum([7, 8, 9, 10, 11, 12])  # Correct sum of the processed data
    assert result == expected_result, "The complete EGTL process should handle augmented data correctly through all steps."

def test_transfer_subtracting():
    data = [15, 25, 35]
    assert transfer(data) == [10, 20, 30], "Should subtract 5 from each element correctly."

def test_transfer_zeros():
    data = [5, 5, 5]
    assert transfer(data) == [0, 0, 0], "Should handle values equal to the subtraction."

def test_transfer_negative():
    data = [1, 2, 3]
    assert transfer(data) == [-4, -3, -2], "Should correctly subtract 5, resulting in negative values."

def test_load_simple_sum():
    data = [10, 20, 30]
    assert load(data) == 60, "Should sum all elements correctly."

def test_load_empty():
    data = []
    assert load(data) == 0, "Should return 0 for an empty dataset."

def test_load_single_element():
    data = [42]
    assert load(data) == 42, "Should handle a single element correctly."
