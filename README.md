# BookBot

BookBot is a simple Python command-line tool that analyzes text files (books) and generates a statistical report. It counts the total number of words and the frequency of each character.

This is my first project on [Boot.dev](https://www.boot.dev)!

## Features

- **Word Count**: Calculates the total number of words in the text.
- **Character Frequency**: Counts how many times each alphabetic character appears (case-insensitive).
- **Sorted Report**: Displays character counts sorted from most frequent to least frequent.

## Usage

1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the script from the command line, providing the path to a text file as an argument.

```bash
python3 main.py books/frankenstein.txt
```

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
...
============= END ===============
```