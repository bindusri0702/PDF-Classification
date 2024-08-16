import re

def retain_only_alphabets(input_string):
    # Retain only alphabets and spaces, and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string).lower()
    
    # Remove words that are less than length 4
    filtered_string = ' '.join([word for word in cleaned_string.split() if len(word) >= 4])
    
    return filtered_string