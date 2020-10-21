# youtube-downloader

[![Generic badge](https://img.shields.io/badge/OS-Linux-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/OS-Windows-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Deployment-ongoing-orange.svg)](https://shields.io/)

## News
Windows is now integrated.
Video download is now integrated.
Future improvements : 
- correct bugs of the progress bar
- correct bugs of first launch
- intelligent download with geo parameters
- list of link to download
## Linux
### Installation
1. Clone the repo
2. Create a config.txt file like bellow :
```
# Configuration file

# Put there the absolute path to the folder where you want to put by default music and video downloaded (like the example bellow :
default_path_music=/home/arblade/Musics/myfolder
default_path_video=/home/arblade/Videos/myfolder
```
3. Launch `yt-downloader.py` with Python 3.6

## Windows
### Installation 
1. Clone or download the repo.

2. Go to the windows folder and check the `install.bat` file, then execute it with administrators rights

3. It will download youtube-download and all necessary packages.

4. An icon 'Youtbe Downloader' should have appeared on your desktop : you can test the app !

5. You can create a config.txt file in `\windows\youtube-downloader\` :
```
# Configuration file

# Put there the absolute path to the folder where you want to put by default music and video downloaded (like the example bellow :
default_path_music=C:\Users\arblade\Music\
default_path_video=C:\Users\arbalde\Videos\
```

## Use 

1. Choose your folder where to download your music / videos files
2. Paste your link.
3. Under gnome, a notification will pop up to inform you that the download is complete

**Important** : Sometimes, the conversion won't work : this is a bug, you have then to do it again, but this time launching the app with admin rights.

![alt text](assets/yt_capture.png)
