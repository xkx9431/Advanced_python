# class SearchEngineBase(object):
#     def __init__(self):
#         pass
#
#     def add_corpus(self, file_path):
#         with open(file_path, 'r') as fin:
#             text = fin.read()
#         self.process_corpus(file_path, text)
#
#     def process_corpus(self, id, text):
#         raise Exception('process_corpus not implemented.')
#
#     def search(self, query):
#         raise Exception('search not implemented.')
#
# def main(search_engine):
#     for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
#         search_engine.add_corpus(file_path)
#
#     while True:
#         query = input()
#         results = search_engine.search(query)
#         print('found {} result(s):'.format(len(results)))
#         for result in results:
#             print(result)


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open('F:\project\Advanced_python\searchEngine\\'+file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implement')

    def search(self):
        raise Exception('search not implement')


def main(searchEngine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt','5.txt']:
        searchEngine.add_corpus(file_path)

    while True:
        query = input()

        results = searchEngine.search(query)
        print('Found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


search_engine = SimpleEngine()
main(search_engine)
