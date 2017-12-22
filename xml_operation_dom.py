from xml.dom import minidom
import tools
import re
import parameters

match_dirty_data_pattern1 = re.compile(parameters.MATCH_DIRTY_DATA_PATTERN1)
match_dirty_data_pattern2 = re.compile(parameters.MATCH_DIRTY_DATA_PATTERN2)


def extract_content_from_xml(src_xml_url, target_filename):
    dom_tree = minidom.parse(src_xml_url)
    doc_root = dom_tree.documentElement
    docs = doc_root.getElementsByTagName('doc')
    with open(target_filename, 'w', encoding='utf-8') as target_file:
        for doc in docs:
            content_title_element = doc.getElementsByTagName('contenttitle')[0]
            content_element = doc.getElementsByTagName('content')[0]
            content_title_str = ''
            content_str = ''
            if content_title_element.hasChildNodes():
                content_title_str = content_title_element.childNodes[0].data
            if content_element.hasChildNodes():
                content_str = content_element.childNodes[0].data
            if match_dirty_data_pattern1.search(content_title_str) \
                    or match_dirty_data_pattern2.search(content_title_str):
                continue
            else:
                if content_title_str != '' and content_title_str != '\n':
                    target_file.write(content_title_str + '\n')
                if content_str != '' and content_str != '\n':
                    target_file.write(content_str + '\n\n')


class XMLsContentExtractor(tools.ProcessPath):
    def do_after_process_file(self, src_xml_url, target_filename):
        extract_content_from_xml(src_xml_url, target_filename)
        print('content has been extracted from', src_xml_url)
        print('result has been saved in', target_filename)
        print('------------------------------------------')


if __name__ == '__main__':
    xml_url = 'E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_xml\\news.sohunews.010802.txt.utf-8.xml'
    target_filename = 'E:\\2222.txt'
    extract_content_from_xml(xml_url, target_filename)

