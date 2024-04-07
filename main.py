# Write a function to convert numbers to text numerals

def text_numeral(num):
    """
    Converts a positive integer less than one hundred 
    to its corresponding text representation.

    Parameter
    ---------
    num: int
        A positive integer less than one hundred

    Returns
    -------
    text_form: str
        The text representation of the integer
    """

    NUM_WORD = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'    
    }

    # check input is of int format and it is in the correct range
    if  type(num) == int and (0 < num < 100):
        key_list_reversed = list(NUM_WORD.keys())[::-1]
        assoc_word = {}
        counter = 0
        while num > 0:
            key = key_list_reversed[counter]
            if num >= key:
                assoc_word[NUM_WORD[key]] = 1
                num = num - key
            else:
                counter = counter + 1

        text_form = ' '.join(list(assoc_word.keys()))
        return text_form
    else:
        return 'Error: Invalid input'
