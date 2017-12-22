EXCEPTION_FILE = 'E:\exception.file'
CANNOT_HANDLE_OUTPUT_FILE = 'E:\cannot_handle_output.file'
SENTENCE_SPLIT_PATTERN = "[。？?！!，,；;\n\u3000\ue40c ]+"  # 有两种全角空格，和半角空格
MATCH_BLANK_PATTERN = '[\u4E00-\u9FA5]\d+[\u3000\ue40c ]+[\u4E00-\u9FA5]'
MATCH_DIRTY_DATA_PATTERN1 = '福彩|开奖|足彩|福利彩票'
MATCH_DIRTY_DATA_PATTERN2 = '\d+期'
# 福彩(双色球)?\d+.+\d+期
