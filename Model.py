import re
import os
class Model():
    def __init__(self):
        self.path=None
        self.folder = os.path.dirname(os.path.abspath(__file__))
        self.config=self.folder+'/config.txt'

    def set_config(self):
        if not self.fileIsValid(self.config):
                print("config file cannot be found")
                return False
        else :
            return True
    def get_config(self):
        
        with open(self.config,"r") as file:
            for line in file.readlines():
                if line[0]=="#":
                    pass #c'est un commentaire
                else :
                    elems=line.split("=")
                    param=elems[0]
                    param.replace(" ", "") # on enlève les espaces potentiels
                    if param=='default_path':
                        self.path=re.sub("\r|\n|\s","",elems[1]) # on enlève les espaces potentiels
                        if self.path[-1]=="/": # au cas où l'utilisateur mette un /
                            self.path=self.path[:-1]

        return self.path


    def fileIsValid(self,file):
        try :
            f=open(file,'r')
            f.close()
            return True
        except :
            return False

    def dirIsValid(self,path):
        if os.path.isdir(path) :
            return True
        else:
            return False
    def set_path(self,path):
        if self.dirIsValid(path):
            self.path=path
            return True
        else :
            return False

    def get_path(self):
        if self.path:
            return self.path
    


a=Model()
print(a.get_config())




