corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]


class CountVectorizer:

    @staticmethod
    def get_feature_names(phrases):
        lowered = []
        for string in phrases:
            a = string.lower().split()
            lowered.extend(a)
        unique_words = []
        for element in lowered:
            if element not in unique_words:
                unique_words.append(element)
        return unique_words

    @staticmethod
    def fit_transform(phrases):
        list_of_dicts = []
        unique_words = []
        for phrase in phrases:
            dict_to_count = dict()
            lowered = []
            for string in phrases:
                a = string.lower().split()
                lowered.extend(a)
            for element in lowered:
                if element not in unique_words:
                    unique_words.append(element)
            for word in unique_words:
                if word not in dict_to_count:
                    dict_to_count[word] = 0
            list_of_dicts.append(dict_to_count)
        for num, phrase in enumerate(phrases):
            words = phrase.lower().split()
            for word in words:
                if word in list_of_dicts[num]:
                    list_of_dicts[num][word] += 1
        matrix = []
        for element in list_of_dicts:
            count = []
            for word in unique_words:
                count.append(element[word])
            matrix.append(count)
        return matrix


if __name__ == '__main__':
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names(corpus))
