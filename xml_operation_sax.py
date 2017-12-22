import xml
from xml.sax import parse
from xml.sax.handler import ContentHandler
import tools
import parameters


class DocHandler(ContentHandler):
    def __init__(self, target_file):
        ContentHandler.__init__(self)
        self.current_element = ""
        self.target_file = target_file
        self.has_written = False

    def startElement(self, name, attrs):
        self.current_element = name

    def endElement(self, name):
        self.current_element = None
        if name == 'contenttitle' and self.has_written:
            self.target_file.write('\n')
            self.has_written = False
        elif name == 'content' and self.has_written:
            self.target_file.write('\n\n')
            self.has_written = False

    # handler will call this method if and only if there are some string in element
    def characters(self, content):
        if self.current_element == 'contenttitle' or self.current_element == 'content':
            if content != '\n':
                self.has_written = True
                self.target_file.write(content)


def extract_content_from_xmls(src_xml_parent_path, target_parent_path):
    src_xml_url_list = []
    target_filename_list = []
    tools.get_filenamelist_under_srcpath_and_targetpath(src_xml_parent_path, target_parent_path,
                                                        src_xml_url_list, target_filename_list,
                                                        filename_suffix=".train")
    length = len(src_xml_url_list)
    for i in range(length):
        src_xml_url = src_xml_url_list[i]
        target_filename = target_filename_list[i]
        try:
            with open(target_filename, 'w', encoding='utf-8') as target_file:
                parse(src_xml_url, DocHandler(target_file))
            print('content has been extracted from', src_xml_url)
            print('result has been saved in', target_filename)
            print('------------------------------------------')
        except xml.parsers.expat.ExpatError as error:
            error_output = "################## Error occur ######################\n"
            error_output += error.__str__() + '\n'
            error_output += "maybe there are some illegal char occur in xml.\n"
            error_output += "give up to extract content from " + src_xml_url + '\n'
            error_output += "################## Error occur ######################\n"
            print(error_output)
            with open(parameters.EXCEPTION_FILE, 'a', encoding='utf=8') as exception_file:
                exception_file.write(error_output)
            continue

if __name__ == '__main__':
    xml_url = "E:\自然语言处理数据集\搜狐新闻数据(SogouCS)_xml\\news.sohunews.010801.txt.utf-8.xml"
    target_filename = "E:\\content_from_xml.train"
    with open(target_filename, 'w', encoding="utf-8") as target_file:
        parse(xml_url, DocHandler(target_file))
