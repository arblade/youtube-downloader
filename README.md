# youtube-downloader

[![Generic badge](https://img.shields.io/badge/OS-Linux-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/OS-Windows-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Deployment-done-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/License-MIT-green.svg)](https://shields.io/)

## News
Youtube-dl is now working on our files for windows.
Windows is now integrated.
Video download is now integrated.
Future improvements : 
- correct bugs of the progress bar : Done
- correct bugs of first launch : Done
- intelligent download with geo parameters
- list of link to download

## Windows
### Installation 


### 2 ways

1. Simple :

**Note** : *Your antivirus / or Windows defender may alert you on this file, i tried to fix this, but i did not success. It seems that if you are not an official developper you are note alllowed to write app that requires particular features, thank you Windows :( !...
If you you want to check what is run by this `.exe`, [click there](#explanation_exe)*
Here is the [Setup.exe](https://github.com/Arblade/youtube-downloader/releases/download/v3.1.2/Setup.exe). If you installed this app before and you want the last version try : [Setup_special.exe](https://github.com/Arblade/youtube-downloader/releases/download/v3.1.2/Setup.exe)

2. If you want to understand what is going on / or if you dont trust the `Setup.exe` :

- Donwload the `.zip`
- Extract it where you want in your computer.
- Execute the `Setup.bat` as admin. You can before read all instructions, to check that this file is safe.
- To understand what is done go through this file : [click there](#explanation)
- Finally you can delete extracted files

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

## Use 

1. Choose your folder where to download your music / videos files
2. Paste your link.
3. Under gnome, a notification will pop up to inform you that the download is complete



![alt text](assets/yt_downloader_capv3.0.1.PNG)
## <a id="explanation_exe"></a>Explanation of commands passed through the `install.bat` file :

This `.exe` file display you a license, and then download the archive of this project. This archive is copied to `Windows\Temp`. Then the `install.bat` (on this project in  `windows/install.bat` is run (precisions below).

## <a id="explanation"></a>Explanation of commands passed through the `Setup.bat` file :

```batch

@echo [info] Download of youtube-dl...
powershell -Command "Invoke-WebRequest https://youtube-dl.org/downloads/latest/youtube-dl.exe -OutFile C:\Windows\youtube-dl.exe"
@echo [info] Download of youtube-dlc...
powershell -Command "Invoke-WebRequest https://github.com/blackjack4494/yt-dlc/releases/latest/download/youtube-dlc.exe -OutFile C:\Windows\youtube-dlc.exe"
@echo [info] Download of add-ons for youtube-dl...
powershell -Command "Invoke-WebRequest https://download.microsoft.com/download/5/B/C/5BC5DBB3-652D-4DCE-B14A-475AB85EEF6E/vcredist_x86.exe -OutFile C:\Windows\Temp\add_on_yt-dl.exe"
@echo [info] Launch of add-on installation
powershell -Command "C:\Windows\Temp\add_on_yt-dl.exe"
@echo [info] Download 7zip...
powershell -Command "Invoke-WebRequest https://www.7-zip.org/a/7z1900-x64.exe -OutFile C:\Windows\Temp\7z.exe"
@echo [info] Installation of 7zip...
powershell -Command "C:\Windows\Temp\7z.exe"
@echo [info] Download of ffmpeg...
powershell -Command "Invoke-WebRequest https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z -OutFile C:\Windows\Temp\ffmpeg.7z"
@echo [info] Extraction of ffmpeg
powershell -Command "& 'C:\Program Files\7-Zip\7z.exe' e C:\Windows\Temp\ffmpeg.7z -oC:\Windows\ ffmpeg.exe -r "
@echo [info] Copy of Youtube-Downloader files
cd /d %~dp0
robocopy ./youtube-downloader/ "C:\Program Files\youtube-downloader" /E
icacls "C:\Program Files\youtube-downloader\config.txt" /grant "*S-1-5-32-545:(W)"
xcopy youtube-downloader\Youtube-Downloader.lnk %UserProfile%\Desktop\
@echo [info] Deleting archive...
@echo [info] Deleting temp files...
del "C:\Windows\Temp\add_on_yt-dl.exe"
del "C:\Windows\Temp\7z.exe"
del "C:\Windows\Temp\ffmpeg.7z"
@echo [info] Closing the terminalby pressing "Enter"
pause
```
1. Download of youtube-dl
2. Donwload of youtube-dlc (an other version of youtube-dl)
3. Then this is download of add-ons to get all components working
4. 7zip is downloaded to extract ffmpeg archive
5. Ffmpeg is downloaded then extracted.
6. Files are copied to `Program Files` directory on your computer
7. Rights are given to a file named config.txt, to allow our program to read and write this file for your custom parameters.
8. An link to our app is copied to your Desktop
9. Then we clean all archives and exe used for this installation.

