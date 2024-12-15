def parse_line(line, doToggle, multi_on):
    search_phrase = "mul("
    do_phrase = "do()"
    dont_phrase = "don't()"


    line_total = 0

    i = 0
    while i < len(line):

        if line[i:i+4] == search_phrase and multi_on:
            total, i = parse_inner_line(line, i)
            line_total = line_total + total
        elif doToggle and line[i:i+4] == do_phrase:
            multi_on = True
            i += 3
        elif doToggle and line[i:i+7] == dont_phrase:
            multi_on = False
            i += 7
        else:
            i += 1

    return line_total, multi_on


def parse_inner_line(line, i):
    end_index = 4

    number1 = ""
    number2 = ""

    comma_found = False

    while True:

        c, p, n, invalid = is_valid_multi(line[i + end_index])
        if invalid:
            i += end_index
            return 0, i
        elif p:
            i += end_index
            return multiply_two_numbers(number1, number2), i
        elif c:
            if not comma_found:
                comma_found = True
            else:
                i += end_index
                return 0, i
        elif n:
            if not comma_found:
                number1 = number1 + line[i + end_index]
            else:
                number2 = number2 + line[i + end_index]

        end_index += 1

def multiply_two_numbers(number1, number2):
    if len(number1) > 0 and len(number2) > 0:
        return int(number1) * int(number2)
    else:
        return 0


def is_valid_multi(char):

    isComma = False
    isClosingParen = False
    isNumber = False
    isInvalid = False

    if char == ',':
        isComma = True
    elif char == ')':
        isClosingParen =  True
    elif char.isdigit():
        isNumber = True
    else:
        isInvalid = True


    return isComma, isClosingParen, isNumber, isInvalid
