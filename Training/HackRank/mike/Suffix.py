def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    print(suffixes)
    suffixes.sort()
    print(suffixes)
    return [index for _, index in suffixes]

# Example usage
text = "banana"
sa = build_suffix_array(text)
print(sa)  # Output: [5, 3, 1, 0, 4, 2]

text = "abcbcd"
sa = build_suffix_array(text)
print(sa)  # Output: [0, 1, 3, 2, 4, 5]

