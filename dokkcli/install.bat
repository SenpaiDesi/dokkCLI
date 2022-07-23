:: Get admin if not enabled yet.
@ECHO OFF
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)
TITLE DOKKCLI is Installing dependencies....
:: Install packages where needed!
pip install --upgrade pip --quiet
pip install mechanize --quiet --exists-action i
pip install tkinter --quiet --exists-action i
pip install colorama --quiet --exists-action i
pip install pygeoip --quiet --exists-action i
pip install opencv-python --quiet --exists-action i
pip install qrcode --quiet --exists-action i
pip install pillow --quiet --exists-action i
TITLE DOKKCLI is adding itself to your enviroment....
:: Add cli to system Enviroment.
setx path "%PATH%;C:\dokkcli\" /M
TITLE DOKKCLI    is done installing!
:: Done
ECHO DONE! Run cli.py in any terminal or the windows Run center and it will launch dokkcli.
pause

