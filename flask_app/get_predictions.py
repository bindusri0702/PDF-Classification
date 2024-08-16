from collections import Counter
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# Predefined target root words and their targets
trgts = ['light', 'fuse', 'cabl', 'others', 'lamp']
replacements = {
    'light': 'lighting',
    'cabl': 'cable',
    'fuse': 'fuses',
    'lamp': 'lighting'
}

def get_predictions(doc):
    words = doc.split()
    root_words = [stemmer.stem(word) for word in words]
    freq = Counter(root_words)

    filtered_freq = Counter({
        word: freq[word] for word in trgts if word in freq
    })

    prediction = filtered_freq.most_common(1)[0][0] if filtered_freq else "others"

    return replacements.get(prediction, prediction)