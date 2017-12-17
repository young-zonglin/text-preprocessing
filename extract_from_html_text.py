import os
import shutil
import chardet

BLOCK_SIZE = 1048576  # or some other, desired size in bytes


# # 判断文件的编码格式
# with open("E:\自然语言处理数据集\搜狐新闻数据(SogouCS)\\news.sohunews.010802.txt", "rb") as f:
#     data = f.read(BLOCK_SIZE)
#     print(chardet.detect(data))

def ls_each_file(parent_path):
    """
    list all filename including dir under parent_path
    :param parent_path: path of folder
    :return: List<String>, list of filename
    """
    child_filename_list = os.listdir(parent_path)
    for filename in child_filename_list:
        print(filename, end="\n")
    return child_filename_list


def same_operation_this_module(src_parent_path, target_parent_path,
                               src_filename_list, target_filename_list,
                               filename_suffix=""):
    if src_parent_path == target_parent_path:
        print('source path can not be equal to target.')
        return
    for filename in os.listdir(src_parent_path):
        src_filename = os.path.join(src_parent_path, filename)
        if os.path.isdir(src_filename):
            print(src_filename, 'is a directory.')
            print("Sorry, we have no ability to handle dir.")
            print(src_filename, 'has been passed.')
            continue
        target_filename = os.path.join(target_parent_path, filename + filename_suffix)
        if not os.path.exists(target_parent_path):
            os.makedirs(target_parent_path)
        src_filename_list.append(src_filename)
        target_filename_list.append(target_filename)


def convert_files_encoding(src_parent_path, target_parent_path, src_encoding, target_encoding="utf-8"):
    """
    convert encoding of files under src_parent_path to target_encoding.
    :param src_parent_path: there are some files waited to be converted
    :param target_parent_path: result file will be saved here
    :param src_encoding: it should be equal to save encoding
    :param target_encoding: default utf-8
    :return: None
    """
    src_filename_list = []
    target_filename_list = []
    same_operation_this_module(src_parent_path, target_parent_path,
                               src_filename_list, target_filename_list,
                               filename_suffix=".utf-8")
    length = len(src_filename_list)
    for i in range(length):
        src_filename = src_filename_list[i]
        target_filename = target_filename_list[i]
        try:
            with open(src_filename, "r", encoding=src_encoding) as source_file, \
                    open(target_filename, "w", encoding=target_encoding) as target_file:
                for line in source_file:
                    target_file.write(line)
            print('convert encoding from', src_encoding, 'to', target_encoding)
            print('result has been saved in', target_filename)
            print('------------------------------------------')
        except UnicodeDecodeError as error:
            os.remove(target_filename)
            print("################## Error occur ######################")
            print(error)
            print("maybe there are some illegal char we cannot decode.")
            print("give up to convert encoding of", src_filename)
            print(target_filename, "has been deleted because of incomplete.")
            print("################## Error occur ######################")
            continue


def add_root_element_each_file(src_parent_path, target_parent_path):
    """
    add root element for each file under src_parent_path, result file
    will be saved under target_parent_path.
    notes: we cannot have any dir under src_parent_path.
    :param src_parent_path:
    :param target_parent_path:
    :return:
    """
    # shutil.copy(raw_filename, result_filename)
    src_filename_list = []
    target_filename_list = []
    same_operation_this_module(src_parent_path, target_parent_path,
                               src_filename_list, target_filename_list,
                               filename_suffix=".added")
    length = len(src_filename_list)
    for i in range(length):
        src_filename = src_filename_list[i]
        target_filename = target_filename_list[i]
        with open(src_filename, 'r', encoding="utf-8") as src_file, \
                open(target_filename, 'w', encoding="utf-8") as target_file:
            target_file.write('<docroot>')
            for line in src_file:
                target_file.write(line)
            target_file.write("</docroot>")
        print(src_filename, "has been processed.")
        print('result has been saved in', target_filename)
        print('=============================================')

# path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)"
# filename_list = ls_each_file(path)
# print(len(filename_list))

src_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)"
target_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_utf-8格式"
convert_files_encoding(src_path, target_path, src_encoding="gb18030")

raw_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_utf-8格式"
result_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_添加root标签"
add_root_element_each_file(raw_path, result_path)
