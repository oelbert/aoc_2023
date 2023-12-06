alphanum = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_number_from_text(text: str) -> str:
    for character in text:
        if character.isnumeric():
            return character


def get_number_from_mixed_text(text: str) -> str:
    buff = ""
    for character in text:
        if character.isnumeric():
            return character
        else:
            buff += character
            for key in alphanum.keys():
                if key in buff:
                    return alphanum[key]


def get_number_from_mixed_reversed_text(text: str) -> str:
    buff = ""
    for character in text:
        if character.isnumeric():
            return character
        else:
            buff = character + buff
            for key in alphanum.keys():
                if key in buff:
                    return alphanum[key]


def run_day1(file: str) -> int:
    dat = open(file, 'r')
    lines = dat.readlines()
    sum1 = 0
    sum2 = 0
    for line in lines:
        num1 = ''
        num1 += get_number_from_text(line)
        num1 += get_number_from_text(line[::-1])
        sum1 += int(num1)
        num2 = ''
        num2 += get_number_from_mixed_text(line)
        num2 += get_number_from_mixed_reversed_text(line[::-1])
        sum2 += int(num2)
    return sum1, sum2


def main():
    print(run_day1('data/day1.txt'))


if __name__ == '__main__':
    main()
