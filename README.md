# stock-web-app
# Reproducing this app
To recreate this web app on your computer, do following.
## Create virtual enviroment
Firstly, we will creat pip enviroment called *venv*
```
python -m venv venv
```
Secondly, we will activate it 
```
venv\Scripts\activate
```
## Install prerequisite libraries
Download requirements.txt file
```
wget https://github.com/pavelzylkov/stock-web-app/blob/master/requirements.txt
```
Pip install libraries
```
pip install -r requirements.txt
```
## Download and unzip contents from GitHub repo
Link: https://github.com/pavelzylkov/stock-web-app/archive/master.zip
## Launch the app
```
streamlit run main.py
```
