from typing import List

def fit_transform(phrases):
    dict_to_count = {}
    unique_words = []
    for phrase in phrases:
        for element in phrase.lower().split():
            if element not in unique_words:
                unique_words.append(element)
        for word in unique_words:
            if word not in dict_to_count:
                dict_to_count[word] = 0
    count_matrix = []
    for phrase in phrases:
        for word in phrase.lower().split():
            if word in dict_to_count:
                dict_to_count[word] += 1
        count_matrix.append(list(dict_to_count.values()))
        dict_to_count = {key: 0 for key in dict_to_count}
    return count_matrix


def tf_transform(matr: List[List[int]]) -> List[List[float]]:
    sum_word = 0
    freq_list = []
    for one_list in matr:
        sum_word = sum(one_list)
        sentence_tf = []
        for number in one_list:
            freq = number / sum_word
            sentence_tf.append(freq)
        freq_list.append(sentence_tf)
    return freq_list


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

matrix = fit_transform(corpus)

# 2
from math import log


def idf_transform(matr: List[List[int]]) -> List[float]:
    docs_count = len(matr)
    column_lens = len(matr[0])
    idf = []
    for i in range(column_lens):
        counter = 0
        for doc in matr:
            if doc[i] != 0:
                counter += 1
        idf.append(log((docs_count + 1) / (counter + 1)) + 1)
    return idf


# 3

class TfidfTransformer:

    def tf_transform(self, matr: List[List[int]]) -> List[List[float]]:
        sum_word = 0
        freq_list = []
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number / sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list

    def idf_transform(self, matr: List[List[int]]) -> List[float]:
        docs_count = len(matr)
        column_lens = len(matr[0])
        idf = []
        for i in range(column_lens):
            counter = 0
            for doc in matr:
                if doc[i] != 0:
                    counter += 1
            idf.append(log((docs_count + 1) / (counter + 1)) + 1)
        return idf

    def fit_transform(self, matr: List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(matr)
        idf = self.idf_transform(matr)
        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]
        return tf_idf


transformer = TfidfTransformer()
tf_idf = transformer.fit_transform(matrix)


# 4

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


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, some_text: List[str]):
        mtrx = super().fit_transform(some_text)
        return self.transformer.fit_transform(mtrx)


if __name__ == '__main__':
    abc = TfidfVectorizer()
    print(abc.fit_transform(corpus))
    print(abc.get_feature_names())