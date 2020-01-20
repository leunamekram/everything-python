:: This script simply renames files with git mv command
:: Disable echo of each line to the terminal output
echo off
echo Renaming files for %1

:: Set folder to work on
set folder=%1
:: Set git client

:: Iterate through each file in the file folder
for /f %%A in ('dir %folder% /b /a-d') do ( call :renameFileWithGit %%A )
GOTO :eof

:: Forceful renaming of files in Git
:renameFileWithGit
    set filename=%1
    set dest_file=%filename:~0,-7%.py
    if %filename:~-7% == _new.py (
        echo Git rename of %filename% to %dest_file%
        git mv -f "%folder%/%filename%" "%folder%/%dest_file%"
    )
    GOTO :eof
