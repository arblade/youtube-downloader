import re
import os
class Model():
    def __init__(self):
        self.path_music=None
        self.path_video=None
        self.dir = None
        self.config=None

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
                    if param=='default_path_music':
                        self.path_music=re.sub("\r|\n|\s","",elems[1]) # on enlève les espaces potentiels
                        if self.path_music[-1]=="/": # au cas où l'utilisateur mette un /
                            self.path_music=self.path_music[:-1]
                    elif param=='default_path_video':
                        self.path_video=re.sub("\r|\n|\s","",elems[1]) # on enlève les espaces potentiels
                        if self.path_video[-1]=="/": # au cas où l'utilisateur mette un /
                            self.path_video=self.path_video[:-1]

        return self.path_music,self.path_video


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
    

