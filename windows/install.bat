@echo [info] Download of youtube-dl...
powershell -Command "Invoke-WebRequest https://youtube-dl.org/downloads/latest/youtube-dl.exe -OutFile C:\Windows\youtube-dl.exe"
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
powershell -Command "& 'C:\Program Files\7-Zip\7z.exe' x -oC:\Windows\ C:\Windows\Temp\ffmpeg.7z"
@echo [info] Copy file ffmpeg
xcopy C:\Windows\ffmpeg-2020-10-17-git-62073cfa97-full_build\bin\ffmpeg.exe C:\Windows\
@echo [info] Copy of Youtube-Downloader files
cd /d %~dp0
robocopy ./youtube-downloader/ "C:\Program Files\youtube-downloader" /E
xcopy youtube-downloader\Youtube-Downloader.lnk %UserProfile%\Desktop\
@echo [info] Close the terminal ...
pause
