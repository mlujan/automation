#Test Automation Environment Setup

virtualenv  --python=python2.7 env

. env/bin/activate

pip install sst

git clone https://github.com/mlujan/automation.git

cd automation

sst-run -r xml





