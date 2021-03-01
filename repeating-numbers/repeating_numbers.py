def find_repeating_numbers(n, input):
    repeating_numbers, hashmap = [], dict()

    for number in input.split(" "):
        number = int(number)

        hashmap[number] = 1 if number not in hashmap.keys() else hashmap[number] + 1

        if hashmap[number] > 1 and number not in repeating_numbers:
            repeating_numbers.append(number)

    return (
        " ".join([str(number) for number in sorted(repeating_numbers)])
        if len(repeating_numbers) > 0
        else "0"
    )
