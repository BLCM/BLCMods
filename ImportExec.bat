:: 'Installs' console executables to the Binaries folder by copying them and stripping the extension
:: Place this in a new folder inside Binaries
:: Inside the same folder also add Data and Buffer folders
:: Put your console executables in the Data folder and run the batch file

@echo off
SET DAT=%~dp0%Data
SET BUF=%~dp0%Buffer
cd "%~dp0"
cd ..
SET INS=%cd%
mkdir "%BUF%"
xcopy "%DAT%" "%BUF%" /y
cd %BUF%
SETLOCAL ENABLEDELAYEDEXPANSION
for /f "tokens=*" %%f in ('dir /b *.*') do (
  SET newname=%%~nf
  move "%%f" "!newname!"
)
xcopy "%BUF%" "%INS%" /y
cd %BUF%
del *.* /Q