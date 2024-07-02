import inflect

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

# Example usage
number = 12345678956941236987132664222222222
print(number_to_words(number))