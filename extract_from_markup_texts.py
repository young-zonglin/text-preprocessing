import os
import tools
import xml_operation_sax
import parameters
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
            error_output = "################## Error occur ######################\n"
            error_output += error.__str__() + '\n'
            error_output += "maybe there are some illegal char we cannot decode.\n"
            error_output += "give up to convert encoding of " + src_filename + '\n'
            error_output += target_filename + " has been deleted because of incomplete."
            error_output += "################## Error occur ######################\n"
            print(error_output)
            with open(parameters.EXCEPTION_FILE, 'a', encoding='utf=8') as exception_file:
                exception_file.write(error_output)
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


def extract_content_from_markup_text(src_parent_path):
    """
    extract content of element of 'content'.
    :param src_parent_path: some markup texts under here
    :return: None
    """
    utf8_files_parent_path = src_parent_path + "_utf-8格式"
    convert_files_encoding(src_parent_path, utf8_files_parent_path, src_encoding="gb18030")
    xml_files_parent_path = src_parent_path + "_xml"
    convert_markup_files_to_xml(utf8_files_parent_path, xml_files_parent_path)
    train_texts_parent_path = src_parent_path + "_train"
    xml_operation_sax.extract_content_from_xml(xml_files_parent_path, train_texts_parent_path)


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
