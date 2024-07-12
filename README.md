
# NATO Phonetic Alphabet Converter

This script converts a user-inputted word into its corresponding NATO phonetic alphabet codes using a CSV file containing the NATO phonetic alphabet.

## Description

The script reads a CSV file containing the NATO phonetic alphabet and maps each letter to its corresponding code. It then prompts the user to input a word and converts each letter of the word to its NATO phonetic code equivalent.

## Usage

1. **Ensure you have the necessary files:**
    - `nato_phonetic_alphabet.csv`: This CSV file should contain the NATO phonetic alphabet with two columns, `letter` and `code`.
    - Your Python script.

2. **Install necessary dependencies:**
    - Make sure you have Python and pandas installed. You can install pandas using pip:
      ```bash
      pip install pandas
      ```

3. **Script Execution:**
    - Run the script in your Python environment. The script will prompt you to enter a word.
    - The script will convert the inputted word to its corresponding NATO phonetic codes and print the result.

## Dependencies

- Python 3.x
- pandas library

## Sample `nato_phonetic_alphabet.csv`

Ensure your CSV file (`nato_phonetic_alphabet.csv`) looks like the following:

```csv
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliett
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu
```

## Example

Here's how to run the script and what to expect:


![Capturewords](https://github.com/user-attachments/assets/18a0208c-1556-46b1-b79b-083d872c08bc)

```bash
$ python nato_phonetic_converter.py
Enter a word: Python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

