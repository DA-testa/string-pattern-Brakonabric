# python3

def read_input():
    print("[!] \tUse an input to choose files or input - F or I ?")
    textInput = input().lower()

    if "f" in textInput:
        file = input()
        with open(file) as f:
            result = f.readline().rstrip(), f.readline().rstrip()
            return result

    elif "i" in textInput:
        result = input().rstrip(), input().rstrip()
        return result


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []

    if len(pattern) > len(text):
        return occurrences

    hashPattern = 0
    hashText = 0
    for i in range(len(pattern)):
        hashPattern = (hashPattern * 263 + ord(pattern[i])) % 10**9
        hashText = (hashText * 263 + ord(text[i])) % 10**9
    
    for i in range(len(text) - len(pattern) + 1):
        if hashPattern == hashText:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)

        if i < len(text) - len(pattern):
            hashText = (263 * (hashText - ord(text[i]) * pow(
                263, len(pattern)-1, 10**9)) + ord(text[i+len(pattern)])) % 10**9
            hashText = (hashText + 10**9) % 10**9
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
