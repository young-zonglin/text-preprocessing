import os
import parameters
import re


newline_match_pattern = re.compile('\n')


# TODO 支持断点续处理
class ProcessPath:
    def do_before_loop(self, src_file, target_file):
        pass

    def do_in_loop(self, line, src_file, target_file):
        pass

    def do_after_loop(self, src_file, target_file):
        pass

    def do_process_file(self, src_filename, target_filename,
                        src_encoding, target_encoding):
        with open(src_filename, 'r', encoding=src_encoding) as src_file, \
                open(target_filename, 'w', encoding=target_encoding) as target_file:
            # 用于在target_file开头写一些东西
            self.do_before_loop(src_file, target_file)
            for line in src_file:
                # 处理src_file的每一行，将结果存入target_file
                self.do_in_loop(line, src_file, target_file)
            # 用于在target_file末尾写一些东西
            self.do_after_loop(src_file, target_file)

    def do_after_process_file(self, src_filename, target_filename):
        print(src_filename, "has been processed.")
        print('result has been saved in', target_filename)
        print('=============================================')

    # template method pattern
    def process_srcpath_to_targetpath(self, src_parent_path, target_parent_path,
                                      filename_suffix="",
                                      src_encoding='utf-8', target_encoding='utf-8'):
        src_filename_list = []
        target_filename_list = []
        get_filenamelist_under_srcpath_and_targetpath(src_parent_path, target_parent_path,
                                                      src_filename_list, target_filename_list,
                                                      filename_suffix)
        length = len(src_filename_list)
        for i in range(length):
            src_filename = src_filename_list[i]
            target_filename = target_filename_list[i]
            # 处理src文件，并将结果放入目标文件
            self.do_process_file(src_filename, target_filename, src_encoding, target_encoding)
            # 处理完一个文件后，控制台打印一些信息
            self.do_after_process_file(src_filename, target_filename)
        print('\n################# Process Finish #####################')
        print(length, 'files have been processed')
        print('################# Process Finish #####################')


def get_filenamelist_under_srcpath_and_targetpath(src_parent_path, target_parent_path,
                                                  src_filename_list, target_filename_list,
                                                  filename_suffix=""):
    """
    get list of filename under src_parent_path and target_parent_path, filename
    under target_parent_path is equal to filename under src_parent_path plus filename_suffix.
    :param src_parent_path:
    :param target_parent_path:
    :param src_filename_list:
    :param target_filename_list:
    :param filename_suffix:
    :return: None
    """
    if src_parent_path == target_parent_path:
        print('source path can not be equal to target.')
        return
    for filename in os.listdir(src_parent_path):
        src_filename = os.path.join(src_parent_path, filename)
        if os.path.isdir(src_filename):
            cannot_handle_output = "############ cannot handle ################\n"
            cannot_handle_output += src_filename + ' is a directory.\n'
            cannot_handle_output += "Sorry, we have no ability to handle dir.\n"
            cannot_handle_output += src_filename + ' has been passed.\n'
            cannot_handle_output += "############ cannot handle ################\n"
            print(cannot_handle_output)
            with open(parameters.CANNOT_HANDLE_OUTPUT_FILE, 'a', encoding='utf-8') as cannot_handle_output_file:
                cannot_handle_output_file.write(cannot_handle_output)
            continue
        target_filename = os.path.join(target_parent_path, filename + filename_suffix)
        if not os.path.exists(target_parent_path):
            os.makedirs(target_parent_path)
        src_filename_list.append(src_filename)
        target_filename_list.append(target_filename)


# 大量字符串拼接的时候避免使用'+'，使用''.join(list)比较好
def get_specify_number_char_from_text(src_file, char_number_one_time_read):
    count = 0
    ret_list = list()
    # line = src_file.readLine()
    # while True:
    #     if line == '' or count >= char_number_one_time_read:
    #         ret_list.append(line)
    #         break
    #     ret_list.append(line)
    #     count += len(line)
    #     line = src_file.readLine()
    for line in src_file:
        if count >= char_number_one_time_read:
            ret_list.append(line)
            break
        else:
            ret_list.append(line)
            count += len(line)
    return ''.join(ret_list)


def get_baidu_segmented_texts():
    processed_texts = list()
    with open(parameters.BAIDU_SEGMENTED_TEXTS_RECORD_FILE, 'r', encoding='utf-8') as record_file:
        for line in record_file:
            processed_texts.append(newline_match_pattern.sub('', line))
    return set(processed_texts)


def update_baidu_segmented_texts(processed_filename):
    with open(parameters.BAIDU_SEGMENTED_TEXTS_RECORD_FILE, 'a', encoding='utf-8') as record_file:
        record_file.write(processed_filename+'\n')


# if __name__ == '__main__':
#     print(get_baidu_segmented_texts())
#     filename = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_segment\\news.sohunews.010801.txt.utf-8.xml.train.seq.clean.gbk.segment'
#     if filename in get_baidu_segmented_texts():
#         print('I am here')

# if __name__ == '__main__':
#     segmented_path = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_segment'
#     count = 0
#     with open(parameters.BAIDU_SEGMENTED_TEXTS_RECORD_FILE, 'a', encoding='utf-8') as record_file:
#         for filename in os.listdir(segmented_path):
#             count += 1
#             record_file.write(os.path.join(segmented_path, filename)+'\n')
#     print(count)
