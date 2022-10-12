class CountVectorizer:

    def __init__(self):
        self.dict_to_count = {}

    def get_feature_names(self):
        return list(self.dict_to_count)

    def fit_transform(self, phrases):
        unique_words = []
        for phrase in phrases:
            for element in phrase.lower().split():
                if element not in unique_words:
                    unique_words.append(element)
            for word in unique_words:
                if word not in self.dict_to_count:
                    self.dict_to_count[word] = 0
        count_matrix = []
        for phrase in phrases:
            for word in phrase.lower().split():
                if word in self.dict_to_count:
                    self.dict_to_count[word] += 1
            count_matrix.append(list(self.dict_to_count.values()))
            self.dict_to_count = {key: 0 for key in self.dict_to_count}
        return count_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
