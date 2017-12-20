import jieba


if __name__ == '__main__':
    text = "我们中出了一位叛徒"
    seg_list = jieba.lcut(text, HMM=False)
    print(type(seg_list))
    print(seg_list)

if __name__ == "__main__":
    text = "我们中出了一位叛徒"
    seg_generator = jieba.cut(text, HMM=False)
    print(type(seg_generator))
    print(seg_generator)
    for word in seg_generator:
        print(word, end=" ")
