import jieba


if __name__ == '__main__':
    text = "我们中出了一位叛徒"
    seg_list = jieba.lcut(text, HMM=False)
    print(type(seg_list))
    print(seg_list)

if __name__ == "__main__":
    text = "今天天气很好"
    jieba.suggest_freq(('今天', '天气'), tune=True)
    seg_generator = jieba.cut(text, HMM=True)
    print(type(seg_generator))
    print(seg_generator)
    for word in seg_generator:
        print(word, end=" ")
