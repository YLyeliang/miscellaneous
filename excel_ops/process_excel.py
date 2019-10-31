import pandas as pd

txt_path = "D:/data/data_extract/20190912_2.txt"
excel_path = 'D:/data/data_extract/提取数据20190912.xlsx'

# debug = 1
# df = pd.read_excel(excel_path)
# data = df.values
# print(data)


class Data_extractor(object):
    def __init__(self, txt_path, excel_path):
        self.txt_path = txt_path
        self.excel_path = excel_path
        self.data_wr = [' ', '#'] * 8 + [' ']
        debug = 1

    def process(self):
        f = open(txt_path, 'w', encoding='utf-8')
        df = pd.read_excel(excel_path,sheet_name=1)
        data = df.values
        for row in data:
            # extract class name and code
            if not isinstance(row[0], float) and '类别' not in row[0]:
                self.data_wr[0] = row[0].split()[0]
                self.data_wr[2] = row[0].split()[1]
            elif not isinstance(row[0], float) and '类别' in row[0]:
                continue

            # extract properties
            if isinstance(row[1], str):
                property_code = self.list2str(row[1].split(), [0, -1])
                property_name = self.list2str(row[1].split(), -1)
                self.data_wr[4] = property_code
                self.data_wr[6] = property_name
            else:
                self.data_wr[4] = " "
                self.data_wr[6] = " "

            # extract common properties
            if isinstance(row[2], str):
                common_properties = row[2].split(';')
                for common_property in common_properties:
                    sp_id = common_property.find('(')
                    common_prop_name = common_property[:sp_id]
                    common_prop_code = common_property[sp_id + 1:-1]
                    self.data_wr[8] = common_prop_name
                    self.data_wr[10] = common_prop_code
                    # extract application properties
                    if isinstance(row[3], str):
                        app_id = row[3].find(')')
                        app_prop_code = row[3][:app_id + 1]
                        app_prop_name = row[3][app_id + 1:]
                        self.data_wr[12] = app_prop_code
                        self.data_wr[14] = app_prop_name
                    else:
                        self.data_wr[12] = " "
                        self.data_wr[14] = " "

                    # extract application property values
                    if isinstance(row[4], str):
                        self.data_wr[16] = row[4]
                    else:
                        self.data_wr[16] = " "
                    write_str = ''.join(self.data_wr)
                    f.write(write_str + ' \n')
            else:
                self.data_wr[8] = " "
                self.data_wr[10] = " "
                # extract application properties
                if isinstance(row[3], str):
                    app_id = row[3].find(')')
                    app_prop_code = row[3][:app_id + 1]
                    app_prop_name = row[3][app_id + 1:]
                    self.data_wr[12] = app_prop_code
                    self.data_wr[14] = app_prop_name
                else:
                    self.data_wr[12] = " "
                    self.data_wr[14] = " "

                # extract application property values
                if isinstance(row[4], str):
                    self.data_wr[16] = row[4]
                else:
                    self.data_wr[16] = " "
                write_str = ''.join(self.data_wr)
                f.write(write_str + ' \n')
                debug = 1

            debug = 1

    def list2str(self, obj_list, index):
        if isinstance(index, list):
            obj_list = obj_list[index[0]:index[1]]
            obj_str = "".join(obj_list)
        else:
            obj_list = obj_list[index]
            obj_str = str(obj_list)
        return obj_str

DE = Data_extractor(txt_path, excel_path)
DE.process()
