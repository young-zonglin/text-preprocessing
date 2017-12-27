EXCEPTION_FILE = 'E:\自然语言处理数据集\exception.file'
CANNOT_HANDLE_OUTPUT_FILE = 'E:\自然语言处理数据集\cannot_handle_output.file'
BAIDU_LEXER_RESULT_FILE = 'E:\自然语言处理数据集\\baidu_lexer_result.file'
BAIDU_SEGMENTED_TEXTS_RECORD_FILE = 'E:\自然语言处理数据集\\baidu_segmented_texts_record.file'
BAIDU_SEGMENT_ERROR_FILE = 'E:\自然语言处理数据集\\baidu_segment_error.file'
SENTENCE_SPLIT_PATTERN_STR = "[。？?！!，,；;\n\u3000\ue40c ]+"  # 有两种全角空格，和半角空格
MATCH_BLANK_PATTERN_STR = '[\u4E00-\u9FA5]\d+[\u3000\ue40c ]+[\u4E00-\u9FA5]'
MATCH_DIRTY_DATA_PATTERN1_STR = '福彩|开奖|足彩|福利彩票'
MATCH_DIRTY_DATA_PATTERN2_STR = '\d+期'
MATCH_CHINESE_PATTERN_STR = '[\u4E00-\u9FA5]'
MATCH_NUMBER_PATTERN_STR = '[0-9]+\.*[0-9]*'
MATCH_TAG_PATTERN_STR = '/[a-z]+'
# 福彩(双色球)?\d+.+\d+期
