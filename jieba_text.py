import jieba
import jieba.posseg as pseg


def jieba_load():
    jieba.load_userdict("jib.txt")  # jieba加辭典
    jieba.load_userdict("text.txt")  # jieba加權重'


def jieba_cut_word(test):
    word = jieba.cut(test)  # jieba 分割句子
    print('/'.join(word))
