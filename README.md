# Computer-vision-based-object-recognition-for-the-visually-impaired-in-an-outdoor-environment

Check out the google drive link for the entire dataset and exported-models

https://drive.google.com/drive/folders/1wDqLb4nBpeusDvtjqV6GJejKEAgE9vtN?usp=sharing

1. download the entire folder
2. go to the folder where requirements.txt is present through termnal
3. write - 'python3 -m venv venv' - to create virtual environment
4. activate the venv by (linux) 'source ./venv/bin/activate';
for windows, go to venv/Scripts and run the command - 'activate'
5. you should see (venv) in the terminal or cmd which means it is activated
6. come to the same folder where requirements.txt is present. install dependecies by -
'pip3 install -r requirements.txt'
7. wait till everything is installed in your venv
8. run the command - 'jupyter-notebook'
to start the jupyter notebook

OR

if requirements.txt throws error
pip3 install jupyter ibm-watson tensorflow-gpu==2.5.0 tf-models-official matplotlib Cython gtts playsound
cd ./models/research && python setup.py build && python setup.py install
