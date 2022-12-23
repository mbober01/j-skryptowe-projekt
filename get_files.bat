@echo off
setlocal enabledelayedexpansion
:menu
cls
echo Menu
echo 1. Uruchom program
echo 2. Backup
echo 3. Informacje o projekcie
echo 4. Wyjście
set /p select=Wybor: 
IF %select%==1 GOTO run 
IF %select%==2 GOTO backup 
IF %select%==3 goto info
IF %select%==4 goto exit 
goto exit

:run
cls
set result=
for %%i in (input/*) do (
    set result=!result!%%i,
)
python main.py %result%
echo utworzono raport
pause 
goto menu 

:backup
cls
if exist backup (
    rmdir /s /q backup > nul
)
mkdir backup
for %%f in (*.html) do (
    xcopy %%f backup 
)
echo:
echo wykonano backup raportow
pause 
goto menu 

:info
cls
echo autor projektu: Michal Bober
echo projekt na podstawie zadania 2 z Algorytmionu 2020
echo:
echo opis algorytmu
echo Ciagiem niepowtarzalnym nazywamy taki ciag (rozpatrujemy w tym zadaniu 
echo tylko ciagi skonczone, tzn. posiadajace skonczona liczbe elementow), w ktorym dowolny jego podciag skladajacy sie z dowolnej liczby jego kolejnych elementow nie powtarza sie bezposrednio po sobie. Np. ciag 1,2,3,2,3,1 nie jest ciagiem niepowtarzalnym, bo podciag 2,3 wystepuje bezposrednio po sobie. Podobnie ciag 2,3,4,3,3,2,4 
echo nie jest ciagiem niepowtarzalnym, bo podciag 3 występuje bezposrednio po sobie. Natomiast ciag 1,2,3,2,1,3 jest ciagiem niepowtarzalnym, podobnie jak ciag 3,2,4,3,2,1 
echo (podciag 3,2 wystepuje w tym ciagu dwa razy, jednak nie jest to bezposrednie sasiedztwo, bo rozdziela je element 4) 
pause 
goto menu 

:exit
echo Koniec
pause
