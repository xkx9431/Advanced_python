# 基于规则的正向分词方法
class MM(object):
    def __init__(self):
        self.window_size = 3  # max length of the word in the vocabulary

    def cut(self, text):
        result = []
        text_length = len(text)
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        index = 0
        while index < text_length:
            for i in range(self.window_size+index, index, -1):
                piece = text[index:i]
                if piece in dic:
                    index = i - 1
                    break
            index = index+1
            result.append(piece)
        return result

# 基于规则的逆向分词方法


class BM(object):
    def __init__(self):
        self.window_size = 3  # max length of the word in the vocabulary

    def cut(self, text):
        result = []
        text_length = len(text)
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        index = text_length
        while index > 0:
            for i in range(index - self.window_size, index):
                piece = text[i:index]
                if piece in dic:
                    index = i + 1
                    break
            index = index-1
            result.append(piece)
        result.reverse()
        return result


def test():
    tozkener1 = MM()
    tozkener2 = BM()
    text = "研究生命的起源"
    print("正向分词方法为：")
    print("-->".join(tozkener1.cut(text)))
    print('\n##'+'**'*8+'##\n')
    print("逆向分词方法为：")
    print("-->".join(tozkener2.cut(text)))


test()
