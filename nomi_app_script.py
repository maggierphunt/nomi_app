from flask import Flask, render_template, redirect, request, Response
import os
from jinja2 import Template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

app = Flask("nomi_app") #making an app
#About page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def about_page():
        return render_template("about_page.html") #runs the about page

  
# Specifies a path to save images and allows image types

app.config["IMAGE_UPLOADS"] = "/Users/Mio/Desktop/nomi_app/static/images/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPEG", "JPG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 



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

                        image = request.files["image"]

                        if image.filename == "":
                                print("Image must have a filename")
                                return redirect(request.url)
                
                        if not allowed_image(image.filename):
                                print("That image extension is not allowed")
                                return redirect(request.url)

                        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

                        print('Image saved!')
                        
                        
        #                 html = """
        #  <html>
        #    <body>
        #    <p class="message">{HTMLmessage}</p>
        #    </body>
        #   </html>
        #         """
                        
        #                 return html.format(HTMLmessage=message)
                        # def submit_message():
                        #         message_submit = "The file was uploaded successfully"
                        #         return render_template("user_input_page.html", message_submit=message_submit) 
                        
                        # submit_message()v
                        message_submit = "<script>`The file was uploaded successfully`</script>"
                        return render_template("user_input_page.html", message_submit=message_submit)
                        return redirect(request.url)
        
        return render_template("user_input_page.html") #runs the landing page


     

#Results
@app.route("/results", methods=['POST'])    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def results_page():

        form_data = request.form
        
        return render_template("display_page.html", 
        FirstName = form_data["FirstName"],
        LastName = form_data["LastName"],
        FirstNamePronunciation = form_data["FirstNamePronunciation"],
        NameRecording=form_data["NameRecording"],
        LastNamePronunciation = form_data["LastNamePronunciation"],
        NickName = form_data["NickName"],
        NickNamePronunciation = form_data["NickNamePronunciation"],
        Gender = form_data["selectGender"],
        FreeTextContentFirstName = form_data["FirstNameFreeTextContent"],    
        FreeTextContentLastName = form_data["LastNameFreeTextContent"])

#debug
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
