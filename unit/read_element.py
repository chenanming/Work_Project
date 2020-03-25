import configparser

class ReadInit:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'F:/Work_Project/YouShuYun_UI/testconfig/element.ini'
        else:
            self.file_path = file_path
        self.data = self.read_init()

    def read_init(self):
        read_init = configparser.ConfigParser()
        read_init.read(self.file_path, encoding='utf-8-sig')
        return read_init

    def get_value(self, key, section=None):
        if section == None:
            section = 'UserPage'
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value

if __name__ == '__main__':
    d = ReadInit()
    print(d.get_value('search_input'))