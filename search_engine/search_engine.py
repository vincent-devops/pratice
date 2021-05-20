class SearchEngineBase(object):
    """搜索引擎基类"""

    def __init__(self):
        pass

    def add_corpus(self, file_path):
        """
        添加到语料库
        读取文件内容，将文件路径作为ID，连同内容一起送到process_corpus中。
        """
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        """
        索引器
        需要对内容进行处理，然后文件路径作为ID，将处理后的内容存下来。（处理后的内容，就叫索引）
        """
        raise Exception('process_corpus not implemented')

    def search(self, query):
        """
        检索器
        给定一个询问，处理询问，再通过索引检索，然后返回
        """
        raise Exception('search not ')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s)'.format(len(results)))
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    """
    一个最基本的搜索引擎
    """
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}  # 初始化”存储文件名到文件内容的字典“

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
