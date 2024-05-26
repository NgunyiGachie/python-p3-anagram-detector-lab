class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, anagram_list):
        matches = []
        for candidate in anagram_list:
            if ''.join(sorted(candidate)) == self.sorted_word:
                matches.append(candidate)
        return matches

listen = Anagram('listen')
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)

