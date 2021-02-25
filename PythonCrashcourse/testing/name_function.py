# Testing a function
def get_formatted_name(first,last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

print(get_formatted_name('hanwei','li'))

def get_formatted_name(first,last,middle = ''):
    full_name = first + ' ' + middle + ' ' + last
    if middle:
        return full_name.title()
    else:
        full_name = first + ' ' + last
    return full_name.title()
