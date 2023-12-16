input = open ('day-1/input', 'r').read()

# input = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""

# print(input)

lines = input.split("\n")

values = list()
sum_value = 0

for line in lines:
    letters = list(line)
    numbers = list()
    for letter in letters:
        if letter in '123456789':
            # print(letter)
            numbers.append(letter)
    first_number = numbers[0]
    last_number = numbers[-1]
    value = numbers[0] + numbers[-1]
    # print(numbers)
    # print(first_number)
    # print(last_number)
    values.append(int(value))
    # print(values)
    # print(value)
sum_value = sum(values)
print(sum_value)


# input ="""two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

print("---------Part 2---------")

lines = input.split("\n")
values = list()
sum_value = 0

for line in lines:
    numbers = list()
    for i in range(len(line)):
        tail = line[i:]
        if tail[0].isdigit():
            numbers.append(tail[0])
        elif tail.startswith("one"):
            numbers.append('1')
        elif tail.startswith("two"):
            numbers.append('2')
        elif tail.startswith("three"):
            numbers.append('3')
        elif tail.startswith("four"):
            numbers.append('4')
        elif tail.startswith("five"):
            numbers.append('5')
        elif tail.startswith("six"):
            numbers.append('6')
        elif tail.startswith("seven"):
            numbers.append('7')
        elif tail.startswith("eight"):
            numbers.append('8')
        elif tail.startswith("nine"):
            numbers.append('9')

    first_number = numbers[0]
    last_number = numbers[-1]
    value = numbers[0] + numbers[-1]
    values.append(int(value))
# print(line, numbers)
# print(values)
sum_value = sum(values)
print(sum_value)

        