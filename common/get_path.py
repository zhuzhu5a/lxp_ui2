import os
class Get_path():

    def get_file_path(self,file,folder):
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        path = os.path.join(dir_path, folder,file)


    def get_root_file_path(self,file):
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 要读取data路径下的login.xlsx文件
        self.path = os.path.join(dir_path,file)

