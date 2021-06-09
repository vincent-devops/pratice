import pdb爱家当代境moma


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
        # pdb.set_trace()

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


# search_engine = SimpleEngine()
# main(search_engine)


import re

class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        """索引器"""
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        """检索器"""
        # 将query打碎成set
        query_words = self.parse_text_to_words(query)
        results = []
        # 检索所有搜索关键词是否都出现在同一篇文章中
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        """将query set中的每个词和文章set核对"""
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        """将文章打碎形成词袋，放入set中"""
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', '', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        world_list = filter(None, word_list)
        # 返回单词的set
        return set(world_list)


# search_engine = BOWEngine()
# main(search_engine)

import re

class BOWinvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWinvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        """索引器"""
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        """检索器"""
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()
        for query_word in query_words:
            query_words_index.append(0)

        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        result = []
        while True:
            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]

                # 已经遍历到了某一个倒序索引的末尾，结束search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1


    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)

search_engine = BOWinvertedIndexEngine()
main(search_engine)



