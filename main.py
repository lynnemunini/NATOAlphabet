import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nano = pandas.read_csv("nato_phonetic_alphabet.csv")
nano_dict = {row.letter: row.code for (index, row) in nano.iterrows()}
# print(nano_dict)
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
name = input("Enter a word: ").upper()
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Remove space in input
name = name.replace(" ", "")
name_list = [nano_dict[letter] for letter in name if letter in nano_dict]
print(name_list)
