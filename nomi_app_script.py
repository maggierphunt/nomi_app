from flask import Flask, render_template, redirect, request, Response
import os
from jinja2 import Template
import io
import base64
from werkzeug.utils import secure_filename

app = Flask("nomi_app") #making an app
firstName = 'None'
lastName = 'None'
nickName = 'None'
gender = 'None'
audio = 'None'

#Specifies a path to save images and allows image types

#app.config['IMAGE_UPLOADS'] =  "TBC"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPEG", "JPG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 


#About page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def about_page():
        return render_template("about_page.html") #runs the about page

  

# Checks if extension is allowed
def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1] #Splits from the right on the . and takes the first element 
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:   
        return False

#Input page
@app.route("/", methods=["GET", "POST"])    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.

def landing_page():

        if request.method == "POST":

               if request.files:
##
                        FirstNameImage = request.files["FirstNameImage"]

                        if FirstNameImage.filename == "":
                                print("Image must have a filename")
                                return redirect(request.url)
                
                        if not allowed_image(FirstNameImage.filename):
                                print("That image extension is not allowed")
                                return redirect(request.url)

                        FirstNameImage.save(os.path.join(app.config['IMAGE_UPLOADS'], FirstNameImage.filename))

                        print('Image saved!')
                        
                        if request.files:

                                LastNameImage = request.files["LastNameImage"]

                        if LastNameImage.filename == "":
                                print("Image must have a filename")
                                return redirect(request.url)
                
                        if not allowed_image(LastNameImage.filename):
                               print("That image extension is not allowed")
                        return redirect(request.url)

                        LastNameImage.save(os.path.join(app.config['IMAGE_UPLOADS'], LastNameImage.filename))

                        print('Image saved!')        
        #                 html = """
        #  <html>
        #    <body>
        #    <p class="message">{HTMLmessage}</p>
        #    </body>
        #   </html>
        #         """
                        
        #                 return html.format(HTMLmessage=message)
                        def submit_message():
                                 message_submit = "The file was uploaded successfully"
                                 return render_template("user_input_page.html", message_submit=message_submit) 
                        
                                #submit_message()v
                        #message_submit = "<script>`The file was uploaded successfully`</script>"
                      # return render_template("user_input_page.html", message_submit=message_submit)
                        return redirect(request.url)
        
        return render_template("user_input_page.html") #runs the landing page

#Results
@app.route("/results", methods=['POST'])      #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
        #image processing!

def results_page():

        form_data = request.form

        global firstName, lastName, nickName, gender, audio, FirstNameImage, LastNameImage
        form_data = request.form
        firstName = form_data['FirstName']
        lastName = form_data['LastName']
        nickName = form_data['NickName']
        gender = form_data['selectGender']
        FirstNameImage = request.files['FirstNameImage']
        LastNameImage = request.files['LastNameImage']
        audio = form_data['NameRecording']
 
        

        return render_template("display_page.html",
        NickName = form_data["NickName"],
        NickNamePronunciation = form_data["NickNamePronunciation"],
        FirstName = form_data['FirstName'],
        LastName = form_data["LastName"],
        FirstNamePronunciation = form_data["FirstNamePronunciation"],
        FirstNameImage = FirstNameImage,
        NameRecording=audio,
        LastNamePronunciation = form_data["LastNamePronunciation"],
        Gender = form_data["selectGender"],
        FreeTextContentFirstName = form_data["FirstNameFreeTextContent"],
        FreeTextContentLastName = form_data["LastNameFreeTextContent"],
        LastNameImage = LastNameImage
        )

@app.route("/widget")
def widget_page():
        global firstName, lastName, nickName, gender, audio
        return render_template("widget_page.html",
                               FirstName=firstName,
                               LastName=lastName,
                               NickName=nickName,
                               Gender=gender,
                               Audio=audio)
      

#debug
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature