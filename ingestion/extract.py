def clean_name(name_string):

    cleaned = name_string.strip().capitalize()

    if cleaned.isalpha():
        return cleaned
    else:
        return None
