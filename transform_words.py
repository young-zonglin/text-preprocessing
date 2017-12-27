import tools
import re
import parameters


per_str = '/PER'
loc_str = '/LOC'
org_str = '/ORG'
time_str = '/TIME'
match_number_pattern = re.compile(parameters.MATCH_NUMBER_PATTERN_STR)
match_tag_pattern = re.compile(parameters.MATCH_TAG_PATTERN_STR)


def transform_words(src_filename, target_filename, src_encoding, target_encoding):
    """
    src_filename的格式应为：搜狐/ORG 娱乐/vn 特别/d 企划/v
    :param src_filename:
    :param target_filename:
    :param src_encoding:
    :param target_encoding:
    :return: None
    """
    with open(src_filename, 'r', encoding=src_encoding) as src_file, \
            open(target_filename, 'w', encoding=target_encoding) as target_file:
        for line in src_file:
            line = line.split(' ')
            length = len(line)
            for i in range(length):
                if per_str in line[i]:
                    line[i] = '#人名#'
                elif loc_str in line[i]:
                    line[i] = '#地名#'
                elif org_str in line[i]:
                    line[i] = '#机构名#'
                elif time_str in line[i]:
                    line[i] = '#时间#'
                else:
                    line[i] = match_tag_pattern.sub('', line[i])
            line = ' '.join(line)
            line = match_number_pattern.sub('#数字#', line)
            target_file.write(line)


class WordsTransformer(tools.ProcessPath):
    def do_process_file(self, src_filename, target_filename, src_encoding, target_encoding):
        transform_words(src_filename, target_filename, src_encoding, target_encoding)


if __name__ == '__main__':
    src_filename = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_segment' \
                   '\\news.sohunews.1180802.txt.utf-8.xml.train.seq.clean.gbk.segment'
    target_filename = 'E:\\222.txt'
    transform_words(src_filename, target_filename, 'gbk', 'gbk')
