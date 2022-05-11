class MinMaxWordFinder:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def shortest_words(self):
        shortest = float("inf")
        words = []

        for sentence in self.sentences:
            for word in sentence.split():
                if len(word) < shortest:
                    shortest = len(word)
        for sentence in self.sentences:
            for word in sentence.split():
                if len(word) == shortest:
                    words.append(word)

        words.sort()
        return words

    def longest_words(self):
        longest = float("-inf")
        words = []

        for sentence in self.sentences:
            for word in sentence.split():
                if len(word) > longest:
                    longest = len(word)
        for sentence in self.sentences:
            for word in sentence.split():
                if len(word) == longest and word not in words:
                    words.append(word)

        words.sort()
        return words
