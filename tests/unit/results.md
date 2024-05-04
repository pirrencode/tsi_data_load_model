# Test Model Logic

collected 17 items                                                                                                                                                                                              

tests/unit/test_logic.py::test_extract PASSED                                                                                                                                                            [  5%] 
tests/unit/test_logic.py::test_generate PASSED                                                                                                                                                           [ 11%] 
tests/unit/test_logic.py::test_transfer PASSED                                                                                                                                                           [ 17%]
tests/unit/test_logic.py::test_load PASSED                                                                                                                                                               [ 23%] 
tests/unit/test_logic.py::test_complete_egtl_process PASSED                                                                                                                                              [ 29%] 
tests/unit/test_logic.py::test_generate_with_augmentation PASSED                                                                                                                                         [ 35%] 
tests/unit/test_logic.py::test_augmentation_length PASSED                                                                                                                                                [ 41%] 
tests/unit/test_logic.py::test_generate_with_zero PASSED                                                                                                                                                 [ 47%] 
tests/unit/test_logic.py::test_generate_with_same_elements PASSED                                                                                                                                        [ 52%] 
tests/unit/test_logic.py::test_generate_with_large_numbers PASSED                                                                                                                                        [ 58%] 
tests/unit/test_logic.py::test_complete_egtl_process_with_augmentation PASSED                                                                                                                            [ 64%] 
tests/unit/test_logic.py::test_transfer_subtracting PASSED                                                                                                                                               [ 70%] 
tests/unit/test_logic.py::test_transfer_zeros PASSED                                                                                                                                                     [ 76%] 
tests/unit/test_logic.py::test_transfer_negative PASSED                                                                                                                                                  [ 82%] 
tests/unit/test_logic.py::test_load_simple_sum PASSED                                                                                                                                                    [ 88%] 
tests/unit/test_logic.py::test_load_empty PASSED                                                                                                                                                         [ 94%] 
tests/unit/test_logic.py::test_load_single_element PASSED                                                                                                                                                [100%] 

============================================================================================= 17 passed in 0.02s ============================================================================================== 

# Test Data Load Simulation

============================================================================================= 17 passed in 0.03s ============================================================================================== 
PS D:\DTP\PhD\papers\EGTL\egtl-validation> pytest --tb=long -vv tests/unit/test_data_load.py
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-8.2.0, pluggy-1.5.0 -- D:\DTP\PhD\papers\EGTL\egtl-validation\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\EGTL\egtl-validation
collected 5 items                                                                                                                                                                                               

tests/unit/test_data_load.py::test_fusion_extract PASSED                                                                                                                                                 [ 20%] 
tests/unit/test_data_load.py::test_fusion_generate PASSED                                                                                                                                                [ 40%] 
tests/unit/test_data_load.py::test_staging_transform PASSED                                                                                                                                              [ 60%]
tests/unit/test_data_load.py::test_alliance_load PASSED                                                                                                                                                  [ 80%] 
tests/unit/test_data_load.py::test_complete_process PASSED                                                                                                                                               [100%] 

============================================================================================== 5 passed in 0.01s ==============================================================================================