# Documentation For File I/O Code Challenge

###### by Mark Edmunds

#### Overview

Since the program relies on `arrivingAnimals.txt` file existing existing at the `input_file_path` I wanted to make sure it would work with operating sysems that use` /` instead of `\` as path separators so imported the  `os` library. Using this library I am able to check the operation system and change the seprator accordingly.

```python
input_file_path = os.getcwd() + "/arrivingAnimals.txt" if os.name == "posix" else os.getcwd() + r"\\arrivingAnimals.txt"
```
I also do the same thing for the output file
```python
output_file_path = os.getcwd() + "/outputFile.txt" if os.name == "posix" else os.getcwd() + r"\\outputFile.txt"
```
In the `get_species()` function I first wanted to check if the function was called with data that could cause the `split` function to fail such as an interger so I used this:
```python
if type(my_str) != str:
        raise TypeError("my_str must be a string")
```
I then wrapped the `return words[my_str]` in a `try: execpt:` block to catch any possible index errors
```python
 try:
        return words[4]
    except IndexError:
        print(f"IndexError: {my_str} is not long enough")
        return None
```
And I added a `except TypeError:` to the `try: except:` block openning the input_file_paht
```python
except TypeError:
    print("TypeError: my_str must be a string")
```

#### Testting
For testing I created `test_fileIO.py` to store test data and test functions. And used pytest to run them.
I tested `get_species()` using strings with five words as well as strings with only 4 words. And usign empty strings,dictionaries, and intergers
```python
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
```
I also created tests for `input_file_path` and `output_file_path`
```python
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
```