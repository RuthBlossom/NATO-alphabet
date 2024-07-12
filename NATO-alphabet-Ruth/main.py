# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Import the pandas library for working with data frames
import pandas

# Read the CSV file containing the NATO phonetic alphabet data into a DataFrame named data.
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary mapping uppercase letters to their corresponding NATO phonetic code
# Create a dictionary (phonetic_dic) that maps uppercase letters to their corresponding NATO phonetic code. The iterrows() method is used to iterate through the rows of the DataFrame.
phonetic_dic = {row.letter.upper(): row.code for (index, row) in data.iterrows()}

# Ask the user to input a word and convert it to uppercase for consistency
word = input("Enter a word: ").upper()

# Create a list of the NATO phonetic code words for each letter in the user's input word
# Create a list (output_list) by using list comprehension to map each letter in the user's input word to its corresponding NATO phonetic code using the phonetic_dic dictionary.
output_list = [phonetic_dic[letter] for letter in word]

# Print the result
print(output_list)



