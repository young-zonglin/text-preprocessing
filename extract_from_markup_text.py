import os
import tools
import xml_operation_sax
import shutil
import chardet

BLOCK_SIZE = 1048576  # or some other, desired size in bytes


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
    tools.get_filenamelist_under_srcpath_and_targetpath(src_parent_path, target_parent_path,
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


def convert_markup_files_to_xml(src_parent_path, target_parent_path):
    """
    add xml element and root element and remove '&' for each file under src_parent_path, result file
    will be saved under target_parent_path.
    notes: we cannot have any dir under src_parent_path.
    :param src_parent_path:
    :param target_parent_path:
    :return:
    """
    # shutil.copy(raw_filename, result_filename)
    src_filename_list = []
    target_filename_list = []
    tools.get_filenamelist_under_srcpath_and_targetpath(src_parent_path, target_parent_path,
                                                        src_filename_list, target_filename_list,
                                                        filename_suffix=".xml")
    length = len(src_filename_list)
    for i in range(length):
        src_filename = src_filename_list[i]
        target_filename = target_filename_list[i]
        with open(src_filename, 'r', encoding="utf-8") as src_file, \
                open(target_filename, 'w', encoding="utf-8") as target_file:
            target_file.write('<?xml version="1.0" encoding="UTF-8"?>')
            target_file.write('<docroot>')
            for line in src_file:
                target_file.write(line.replace('&', ''))
            target_file.write("</docroot>")
        print(src_filename, "has been processed.")
        print('result has been saved in', target_filename)
        print('=============================================')


# if __name__ == '__main__':
#     # judge encoding of file
#     with open("E:\自然语言处理数据集\搜狐新闻数据(SogouCS)\\news.sohunews.010802.txt", "rb") as f:
#         data = f.read(BLOCK_SIZE)
#         print(chardet.detect(data))
#
# if __name__ == '__main__':
#     path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)"
#     filename_list = ls_each_file(path)
#     print(len(filename_list))
#
# if __name__ == '__main__':
#     src_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)"
#     target_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_utf-8格式"
#     convert_files_encoding(src_path, target_path, src_encoding="gb18030")
#
# if __name__ == '__main__':
#     raw_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_utf-8格式"
#     result_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_xml"
#     convert_markup_files_to_xml(raw_path, result_path)

# if __name__ == '__main__':
#     src_xml_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_xml"
#     target_path = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_train"
#     xml_operation_sax.extract_content_from_xml(src_xml_path, target_path)
