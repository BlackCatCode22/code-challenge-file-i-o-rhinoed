# Tests for fileIO_CC_rhinoed.py
# CIT 95 Fall 2021
# Mark Edmunds
# 9/23/23

# Imports
import random
from fileIO_CC_rhinoed import get_species, input_file_path, output_file_path

gender = ["male", "female"]
species = ["lion", "tiger", "hyena", "bear", "wolf", "bear", "elephant", "giraffe","zebra","rhino","hippo"]
five_word_strings = [f"{random.randint(1,15)} year old {gender[random.randint(0,1)]} " + specie for specie in species]
joined_words_strings = [f"{random.randint(1,15)} year-old {gender[random.randint(0,1)]} " + specie for specie in species]
json_like_obj = {"age": 12,"species": "lion"}
# Test functions
def test_get_species():
    i = 0
    for test_string in five_word_strings:
        assert get_species(test_string) == species[i], "get_species() returned incorrect species"
        assert get_species(test_string) != None, "get_species() returned IndexError"
        i += 1
    j = 0
    for j_string in joined_words_strings:
        assert get_species(j_string) == None, "get_species() returned None"
        assert get_species(j_string) != species[j], "get_species() returned IndexError"
        j += 1
    
    assert get_species("") == None

    try:
        get_species(1)
        assert False, "get_species() did not raise TypeError"
    except TypeError as e:
        assert True, f"get_species() raised {e}"

    try:
        get_species(json_like_obj)
        assert False
    except TypeError as e:
        assert True, print(f"get_species() didi not return error:  {e}")

def test_input_file_path():
    try:
        open(input_file_path, "r")
        assert True
    except FileExistsError as e:
        assert False, f"Exception occured: {e}"


def test_ouput_file_path():
    try:
        open(output_file_path, "w")
        assert True
    except PermissionError as e:
        assert False, f"Exception, occured: {e}"
