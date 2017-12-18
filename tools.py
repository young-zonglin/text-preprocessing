import os


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
            print(src_filename, 'is a directory.')
            print("Sorry, we have no ability to handle dir.")
            print(src_filename, 'has been passed.')
            continue
        target_filename = os.path.join(target_parent_path, filename + filename_suffix)
        if not os.path.exists(target_parent_path):
            os.makedirs(target_parent_path)
        src_filename_list.append(src_filename)
        target_filename_list.append(target_filename)
