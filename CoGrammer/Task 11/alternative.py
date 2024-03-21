# Code to alternate between upper and lowercase each word

def alternate_case_words2(input_string2):
    words = input_string2.split()
    result = []

    for i, word in enumerate(words):
        if i % 2 == 0:  # Check if the index is even
            result.append(word.upper())
        else:
            result.append(word.lower())

    return ' '.join(result)

# Area to input string
input_text2 = "I am learning to code"
output_text2 = alternate_case_words2(input_text2)
print(output_text2)

# Code to alternate between upper and lowercase each character

def alternate_case(input_string):
    result = []
    upper = True  # Flag to track whether the next character should be uppercase or lowercase

    for char in input_string:
        if char.isalpha():
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper  # Toggle the flag for the next character
        else:
            result.append(char)

    return ''.join(result)

# Area to input string
input_text = "HelloWorld"
output_text = alternate_case(input_text)
print(output_text)