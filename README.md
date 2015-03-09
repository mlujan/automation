#Prerequisite
Install Python 2.7
In windows:
set PATH=%PATH%;C:\Python27
set PATH=%PATH%;C:\Python27\scripts
#Pip install virtualenv
Install git
http://git-scm.com/download/win

#Test Automation Environment Setup
virtualenv  --python=/python27/python.exe env

cd env/Scripts/
activate

pip install sst

git clone https://github.com/mlujan/automation.git

cd automation

sst-run -r xml





