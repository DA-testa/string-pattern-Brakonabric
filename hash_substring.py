# python3

def read_input():
    print("[!] \tUse an input to choose files or input - F or I ?")
    textInput = input(">:: \t").lower()
    if "f" in textInput:
        with open(input().rstrip) as f:
            return (f.readline().rstrip(), f.readline().rstrip())

    elif "i" in textInput:
        return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    occurrences = []
    hashPattern = 0
    hashText = 0

    if len(pattern) > len(text):
        return occurrences

    for s in pattern:
        hashPattern = (hashPattern * 256 + ord(s)) % 10**8

    for i in range(len(pattern)):
        hashText = (hashText * 256 + ord(text[i])) % 10**8

    if hashText == hashPattern:
        if text[:len(pattern)] == pattern:
            occurrences.append(0)

    x = 1
    for i in range(len(pattern)):
        x = (x * 256) % 10**8

    for i in range(1, len(text) - len(pattern) + 1):
        hashText = (256 * (hashText - ord(text[i - 1]) * x) + ord(text[i + len(pattern) - 1])) % 10**8
        if hashText == hashPattern:
            if text[i:i + len(pattern)] == pattern:
                occurrences.append(i)

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
