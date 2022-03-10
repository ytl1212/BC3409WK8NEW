#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


app = Flask(__name__)


# In[5]:


from werkzeug.utils import secure_filename #3rd
import speech_recognition as sr #5th

@app.route("/",methods =["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["file"] #2nd step
        print("file received") #2nd then run and check if "file received" appear in jupyter(below pink running area)
        filename = secure_filename(file.filename) #3rd
        print(filename) #3rd then run and go website upload file and check if "Welcome.wav" appear downstair
        file.save("static/"+filename) #4th step : b4 this,create a folder in Speech named "static"
        a = sr.AudioFile("static/"+filename) #5th
        with a as source:
            a = sr.Recognizer().record(a)
        s = sr.Recognizer().recognize_google(a) #5th 
        return(render_template("index.html",result=s)) #5th change "1" to s variable!!then after uploading the transcript of the recording will come out on the chrome side at {result} de weizi
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




