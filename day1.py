DIGITS = '0123456789'
NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',    
}


def calibration_value(text, convert_letters=False):    
    first, last = None, None
    text_length = len(text)    
    for i in range(text_length):
        j = text_length - i - 1
        
        if first is None:
            if text[i] in DIGITS:
                first = text[i]
            elif convert_letters:
                converted_i = replace_letters_x(text[:i+1])[-1]
                if converted_i in DIGITS:
                    first = converted_i

        if last is None:
            if text[j] in DIGITS:
                last = text[j]
            elif convert_letters:
                converted_j = replace_letters_x(text[j:text_length])[0]
                if converted_j in DIGITS:
                    last = converted_j
        
        if first is not None and last is not None:
            return int(first + last)    

def replace_letters_x(text: str):
    for k,v in NUMBERS.items():
        text = text.replace(k, v)
    return text


with open('data/day1.txt', 'r') as f:
    lines = f.readlines()    
    part1_values = [calibration_value(line, convert_letters=False) for line in lines]
    part2_values = [calibration_value(line, convert_letters=True) for line in lines]
    
print(sum(part1_values))
print(sum(part2_values))



