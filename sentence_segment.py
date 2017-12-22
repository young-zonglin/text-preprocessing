import re
import parameters
import tools
import data_cleaner


# 关于顿号'、'，用于句子内部并列词语之间的停顿
# 例如：正方形是四边相等、四角均为直角的四边形。
# 感觉顿号不应该切分句子

# 冒号：用于引出下文，不应该切分句子
# 引号“”‘’不应该切分句子
# 括号（）用于注释句子或词语，不应该切分句子，还有[]、【】等
# 破折号——不应该切分句子
# 省略号......不应该切分句子
# 连接号-不应该切分句子
# 间隔号·（中文输入法，不要按shift键，敲数字1旁边的键）用于外国人名，不应该切分句子
# 书括号《》不应该切分句子

# 是否有英文符号

# 科技文献中会有.这种句号的出现
# 句号。问号？叹号！逗号，分号；这些符号应该切分句子

class SentenceSegment(tools.ProcessPath):
    sentence_split_pattern = re.compile(parameters.SENTENCE_SPLIT_PATTERN)

    def do_in_loop(self, line, src_file, target_file):
        line = data_cleaner.remove_comma_from_number(line)
        line = data_cleaner.convert_fullwidth_to_halfwidth(line)
        line = data_cleaner.remove_blank_from_number_and_chinese(line)
        for seq in self.sentence_split_pattern.split(line):
            if seq != '' and seq != '\n':
                target_file.write(seq+'\n')

    def do_after_process_file(self, src_filename, target_filename):
        print(src_filename, "has been processed.")
        print('result has been saved in', target_filename)
        print('=============================================')


# if __name__ == '__main__':
#     str_test = '跳转至：页４／１０我来说两　句'
#     str_split = re.split(parameters.sentence_split_pattern, str_test)
#     print(type(str_split))
#     print(str_split)
#     for tmp in str_split:
#         print(tmp, end=" ")
