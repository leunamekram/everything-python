:: This script simply copies and renames files with appended "_new"
:: Disable echo of each line to the terminal output
echo off
echo Copying files for %1

:: Set folder to work on
set folder=%1
:: Set git client

:: Iterate through each file in the file folder
for /f %%A in ('dir %folder% /b /a-d') do ( call :copyFileNew %%A )
GOTO :eof

:: Copy each file appending "_new"
:copyFileNew
    set filename=%1
    set dest_file=%filename:~0,-3%_new.py
    if not %filename% == __init__.py (
        if not %filename:~-7% == _new.py (
            echo Copying %folder%/%filename% as %folder%/%dest_file%
            xcopy %folder%\%filename% %folder%\%dest_file%* /y /q
        )
    )
    GOTO :eof
