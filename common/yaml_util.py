import yaml
class Yamlutil:
    def get(self,path):
        with open(path,'r',encoding='utf_8') as f :
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data
