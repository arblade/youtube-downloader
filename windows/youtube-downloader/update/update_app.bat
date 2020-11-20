@echo ------------------ Update of Youtube-Downloader -------------------
@echo [info] Download...
powershell -Command "Invoke-WebRequest https://github.com/Arblade/youtube-downloader/archive/main.zip -OutFile C:\Windows\Temp\main.zip"
@echo [info] Dezip...
powershell -Command "Expand-Archive 'C:\Windows\Temp\main.zip' -DestinationPath C:\Windows\Temp\youtube-downloader\ -Force"
@echo [info] Go into directory...
cd C:\Windows\Temp\youtube-downloader\youtube-downloader-main\windows\
@echo [info] Copy of Youtube-Downloader files
robocopy ./youtube-downloader/ "C:\Program Files\youtube-downloader" /E
@echo ------------------ Done -------------------
@echo Press Enter to quit
pause