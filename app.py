from flask import Flask,render_template,request
import SozcukKonu as konumodul
from flask_bootstrap import Bootstrap

#import SesSozcuk as recognizer


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
   return render_template("index.html")
   


@app.route("/yorum",methods = ["GET","POST"])
def deneme():
   if request.method == "POST":
      
      sozcukler = request.form.get("htmlgonderi")
      konu = konumodul.konubul(sozcukler)
      return render_template("yorum.html",sozcukler = konu)
   
   else:
      return render_template("yorum.html")  




@app.route("/sesanaliz")
def sesial():
   import speech_recognition as sr
   sr.Microphone(device_index=1)

   r=sr.Recognizer()

   r.energy_threshold=5000

   with sr.Microphone() as source:
        print("Dinleme Aktif")
        audio=r.listen(source)
   try:
        text=r.recognize_google(audio,language="tr-TR")                
        print("You said: "+format(text))
   except:
        print("Cant recognized")

   return render_template("postalan.html",message = text)


if __name__=="__main__":
    app.run(debug = True)
