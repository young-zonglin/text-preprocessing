# text-preprocess
Preprocess text, transfer them into format used by language model implemented by Keras with LSTM in Python.

# get started
The main entry is in text_preprocess_main.py.
Maybe you should uncomment the code in the text_preprocess_main.py.

# 步骤
（1）转换编码
（2）转换标记文本为xml
（3）获取content和contenttitle元素内的文本
（4）将全角字符转为半角
（5）去除数字内的逗号
（6）按照停顿符和空格切句
（7）继续清洗文本（不要“福彩”类的文本，去掉不应该出现的空格，去掉不包含中文的行）
