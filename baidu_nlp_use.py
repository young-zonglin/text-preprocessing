import baidu_nlp_parameters
import parameters
from aip import AipNlp
import tools


char_number_one_time_read = 10000


def get_client():
    """
    获取百度nlp client
    :return: 百度nlp client
    """
    client = AipNlp(baidu_nlp_parameters.APP_ID, baidu_nlp_parameters.API_KEY, baidu_nlp_parameters.SECRET_KEY)
    client.setConnectionTimeoutInMillis(20000)
    client.setSocketTimeoutInMillis(60000)
    return client


def segment_baidu(client, text):
    """
    使用百度词法分析接口进行分词
    :param client: 百度nlp client
    :param text: 待分词文本
    :return: (list of seg word, baidu_lexer_result_dictionary)
    """
    # baidu_result: dict
    baidu_result = client.lexer(text)
    # items: list
    items = baidu_result.get('items')
    seg_result = list()
    if items:
        length = len(items)
        for i in range(length):
            # item: dict
            item = items[i]
            seg_result.append(item.get('item'))
    else:
        pass
    return seg_result, baidu_result


def segment_text(client, src_filename, target_filename):
    with open(src_filename, 'r', encoding='utf-8') as src_file:
        with open(target_filename, 'w', encoding='utf-8') as target_file, \
                open(parameters.BAIDU_LEXER_RESULT_FILE, 'a', encoding='utf-8') as baidu_lexer_res_file:
            text = tools.get_specify_number_char_from_text(src_file, char_number_one_time_read)
            while text != '':
                seg_baidu_tuple = segment_baidu(client, text)
                seg_result = seg_baidu_tuple[0]
                seg_text_str = ' '.join(seg_result)
                baidu_result = seg_baidu_tuple[1]
                target_file.write(seg_text_str)
                baidu_lexer_res_file.write(baidu_result.__str__()+'\n')
                text = tools.get_specify_number_char_from_text(src_file, char_number_one_time_read)


class TextsSegmentation(tools.ProcessPath):
    def __init__(self):
        self.baidu_nlp_client = get_client()

    def do_process_file(self, src_filename, target_filename):
        segment_text(self.baidu_nlp_client, src_filename, target_filename)


if __name__ == "__main__":
    text = "同意在新起点上退动中美关析取得更大法展"
    client = get_client()
    seg_result = segment_baidu(client, text)
    for word in seg_result[0]:
        print(word, end=" ")
    src_filename = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_clean\\news.sohunews.010801.txt.utf-8.xml.train.seq.clean'
    target_filename = 'E:\\333.txt'
    segment_text(client, src_filename, target_filename)
