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