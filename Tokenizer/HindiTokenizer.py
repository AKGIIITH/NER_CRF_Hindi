def tokenize_to_conll(text):
    sentences = text.split("।")  # Split text into sentences based on full stop

    conll_data = ""
    sentence_count = 0
    for sentence in sentences:
        words = sentence.split()  # Split sentence into words
        if len(words) == 0:
            continue

        sentence_count += 1
        for i, word in enumerate(words, start=1):
            # For each word, create a CoNLL formatted line
            conll_data += f"{word}\n"
        conll_data += "\n"  # Separate sentences with empty line
    return conll_data

# Read data from input file
input_filename = "./News.txt"
output_filename = "output.txt"

with open(input_filename, "r", encoding="utf-8") as file:
    hindi_text = file.read()

# Tokenize and format the data
conll_output = tokenize_to_conll(hindi_text)

# Save formatted data to output file
with open("tokenized", "w", encoding="utf-8") as file:
    file.write(conll_output)

print("Data saved to", output_filename)

#After getting Tokenized value, Clean the Data removing Punctuations
