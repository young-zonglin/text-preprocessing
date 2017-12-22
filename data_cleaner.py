import re
import parameters
from pyparsing import unichr


def remove_comma_from_number(seq):
    pattern = re.compile(r"\d[,，]+\d")
    while True:
        matched_obj = pattern.search(seq)
        if matched_obj:
            matched_str = matched_obj.group()
            seq = seq.replace(matched_str, matched_str.replace(',', '').replace('，', ''))
        else:
            break
    return seq


def remove_blank_from_number_and_chinese(seq):
    chinese_number_blank_chinese_pattern = re.compile(parameters.MATCH_BLANK_PATTERN)
    blank_pattern = re.compile('[\u3000\ue40c ]+')
    while True:
        matched_obj = chinese_number_blank_chinese_pattern.search(seq)
        if matched_obj:
            matched_str = matched_obj.group()
            seq = seq.replace(matched_str, blank_pattern.sub('', matched_str))
        else:
            break
    return seq


def convert_fullwidth_to_halfwidth(in_str):
    """全角转半角"""
    ret_str = ""
    for uni_char in in_str:
        inside_code = ord(uni_char)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        ret_str += unichr(inside_code)
    return ret_str


if __name__ == '__main__':
    seq = '辽机集团将其持有　的沈阳合金投资股份有限公司１，，，０,,００万股股权质押给公司'
    seq = remove_comma_from_number(seq)
    print(seq)
    print(convert_fullwidth_to_halfwidth(seq))
    for i in range(65281, 65375):
        print(i, unichr(i))
    print(ord('　'))
