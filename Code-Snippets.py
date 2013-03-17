from string import ascii_letters, digits
from unicodedata import normalize

def filename_sanitization(filename):
    """Removes invalid characters in the arguments passed to it. Used for folder- and filenames."""
    if filename:
        valid_characters = str('-_.() {0}{1}'.format(ascii_letters, digits))
        clean_filename = str(normalize('NFKD', filename).encode('ASCII', 'ignore'))
        return ''.join(char for char in clean_filename if char in valid_characters)[1:]
    else:
        return 'None'
