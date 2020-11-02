@echo [info] Copy of Youtube-Downloader files
cd /d %~dp0
robocopy ./youtube-downloader/ "C:\Program Files\youtube-downloader" /E
xcopy youtube-downloader\Youtube-Downloader.lnk %UserProfile%\Desktop\
@echo [info] Close the terminal ...
pause
