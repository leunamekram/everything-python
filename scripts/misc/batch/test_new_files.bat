:: This script simply copies and renames files with appended "_new"
:: Disable echo of each line to the terminal output
echo off
echo Testing new files for %1

:: Set folder to work on
set folder=%1
:: Set python interpreter
set python="C:\Python35-32\python"

:: Iterate through each file in the file folder
for /f %%A in ('dir %folder% /b /a-d') do ( call :runFiles %%A )
GOTO :eof

:: Run each file
:runFiles
    set filename=%1
    set filename_new=%filename:~0,-3%_new.py
    if not %filename% == __init__.py (
        if not %filename:~-7% == _new.py (
            %python% %folder%/%filename%
            %python% %folder%/%filename_new%
        )
    )
    GOTO :eof

:: Aborting script. Guess ill have to do this in python