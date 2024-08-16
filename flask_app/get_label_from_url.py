from get_text_from_url import get_text_from_url
from retain_only_alphabets import retain_only_alphabets
from starts_with_any_prefix import starts_with_any_prefix
from get_predictions import get_predictions
def get_label_from_url(url):
    pdf_text = get_text_from_url(url)
    clean_text = retain_only_alphabets(pdf_text)
    if not isinstance(clean_text, str) or starts_with_any_prefix(clean_text):
        return "Error in reading PDF."
    else:
        label = get_predictions(clean_text)
    return label