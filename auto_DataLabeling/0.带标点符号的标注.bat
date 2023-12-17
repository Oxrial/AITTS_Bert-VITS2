@echo off
chcp 65001
@title VITS数据自动标注 by 未鸟
set path=.\env\Scripts;.\env;ffmpeg\bin;.\env\bin;%path%
echo =====
echo 请确定所有的音频已经按标准处理完毕，否则必报错！
echo =====
echo.
DEL long_character_anno.txt
DEL long_character_anno.list
.\env\python.exe auto_DataLabeling_long.py
:wait
timeout /t 1/nobreak >nul 2>&1
tasklist find /i "python.exe">nul 2>&1
if %errorlevel% equ 0 (
	goto wait
)
.\env\python ./sort_file.py long_character_anno.txt \d+(?=\.wav)
pause
