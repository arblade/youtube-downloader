#!/home/theophane/anaconda3/bin/python
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
import sys
from app import GUI
from app.Model import *
from gi.repository import Notify,GdkPixbuf



class MyApp(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

        # Connect a button to a function
        app_icon = QtGui.QIcon('/home/theophane/Documents/youtube-downloader/yt-downloader/icon.png')
        self.setWindowIcon(app_icon)
        self.pushButton.clicked.connect(self.run)
        self.process=None
        self.progressBar.setValue(0)

    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        options |= QtWidgets.QFileDialog.DontUseCustomDirectoryIcons
        path= QtWidgets.QFileDialog.getExistingDirectory(self, options=options)
        if path:
            self.lineEdit.setText(path)
        
  

    def create_process(self):
        # Add the process and start it
        self.process = QtCore.QProcess()
        # Set the channels
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        # Connect the signal readyReadStandardOutput to the slot of the widget
        self.process.readyReadStandardOutput.connect(self.write_to_window)

    def write_to_window(self):
        text = str(self.process.readAllStandardOutput(),'utf-8')
        print(text)
        # gestion largeur texte 
        if len(text)>100:
            text=text[0:100]+'\n'+text[100:]
        # gestion des download

        if text[1:13]=='[download]  ':
            text=re.sub("\s\s+", " ", text)
            text=text.replace("\n","")
            elems=text.split(" ")
            for elem in elems:
                elem.replace(" ", "")
            print(elems)

            self.progressBar.setValue(float(elems[1][0:-1]))

            self.state.setText('Progression : {}'.format(text))
        else :
            self.state.setText(text)

    def terminate(self):
        self.state.setText("Finished ! Ready !")
        self.progressBar.setValue(100)
        Notify.init("App Name")
        # Use GdkPixbuf to create the proper image type
        image = GdkPixbuf.Pixbuf.new_from_file(model.folder+"/icon.png")

        # Use the GdkPixbuf image
        summary = "Download Complete !"
        body = "Your download is complete !"
        notification = Notify.Notification.new(summary,body) # Optional
        notification.set_icon_from_pixbuf(image)
        notification.set_image_from_pixbuf(image)
        notification.show()
    



    def run(self):
        self.progressBar.setValue(0)
        # Write here what happens after the button press
        self.state.setText("State : Lauching Analysis")
        link = self.lineEdit_link.text()

        if self.lineEdit.text() :
            if not model.set_path(str(self.lineEdit.text())):
                self.state.setText("State : Cannot find the path")
                return
            else :
                path=model.get_path()
        else :
            if not model.set_config():
                self.state.setText("State : Cannot find the configuration file")
                return
            else :
                path=model.get_config()
        if link[0:4]=="http": #petite vérification 
            self.state.setText("State : Launching Download")
            self.create_process() # on crée le process
            if not self.checkBox.isChecked():
                #cmd = 'youtube-dl -x --embed-thumbnail --format bestaudio --output \"~/Musique/yt-download/%(title)s.%(ext)s\" {}'.format(link)
                self.process.start('youtube-dl',['-x','--embed-thumbnail','--format', 'bestaudio', '--output', path+'/%(title)s.%(ext)s\"', link])
            else :
                #cmd = 'youtube-dl -x --embed-thumbnail --format bestaudio --output \"~/Musique/yt-download/%(playlist)s/%(title)s.%(ext)s\" {}'.format(link)
                self.process.start('youtube-dl',['-x','--embed-thumbnail','--format', 'bestaudio', '--output',path+'/%(playlist)s/%(title)s.%(ext)s\"', link])
            #os.system(cmd)
            #subp.run(['youtube-dl','-x','--embed-thumbnail','--format', 'bestaudio', '--output', '\"~/Musique/yt-download/%(title)s.%(ext)s\"', link],capture_output=True, text=True)
            #process=subp.Popen(['youtube-dl','-x','--embed-thumbnail','--format', 'bestaudio', '--output', '\"~/Musique/yt-download/%(title)s.%(ext)s\"', link],stdout=subp.PIPE)

            self.process.finished.connect(self.terminate)
                    
        else :
            self.state.setText("State : Stopped : wrong link")
            return
        
if __name__ == '__main__':
    model=Model()
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.setWindowIcon(QtGui.QIcon(model.folder+'/icon.png'))
    form.setWindowTitle("Youtube-Downloader")
    form.show()
    app.exec_()
 