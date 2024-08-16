error_prefixes = ("request timed", "http error occurred", "error occurred")

# Function to check if `pdf` starts with any of the error prefixes
def starts_with_any_prefix(pdf):
    return any(pdf.startswith(prefix) for prefix in error_prefixes)