def decode(filename):
    uniqueDigits = ["cf", "bcdf", "acf", "abcdefg"]
    uniqueLens = set(len(digit) for digit in uniqueDigits)
    results = []
    with open(filename) as file:
        for line in file:
            signals, outputs = line.split("|")
            signals = signals.split()
            outputs = outputs.split()

            signals.sort(key=lambda i: len(i))

            digits = {}
            digits[1] = set(signals[0])
            digits[7] = set(signals[1])
            digits[4] = set(signals[2])
            digits[8] = set(signals[9])

            # 5 segment digits (2,3,5)
            for signal in signals[3:6]:
                differenceFromOne = digits[1] - set(signal)
                if differenceFromOne:
                    digitsDifferentFromFour = len(digits[4] - set(signal))
                    if digitsDifferentFromFour == 1:
                        digits[5] = set(signal)
                    else:
                        digits[2] = set(signal)
                else:
                    digits[3] = set(signal)

            # 6 segment digits (0,6,9)
            for signal in signals[6:9]:
                if digits[4] - set(signal):
                    if digits[1] - set(signal):
                        digits[6] = set(signal)
                    else:
                        digits[0] = set(signal)
                else:
                    digits[9] = set(signal)

            # match outputs to the signals
            result = 0
            for output in outputs:
                result *= 10
                for number, segments in digits.items():
                    if segments == set(output):
                        result += number
                        break
            results.append(result)
    return results


if __name__ == "__main__":
    result = decode("test.txt")
    print(sum(result))

    result2 = decode("test2.txt")
    print(sum(result2))

    result3 = decode("input.txt")
    print(sum(result3))
