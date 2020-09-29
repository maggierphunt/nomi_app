from flask import Flask, render_template, redirect, request, Response
import os
from jinja2 import Template

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
                        
                        message = 'The file was uploaded successfully'

                        return redirect(request.url)

        return render_template("user_input_page.html") #runs the landing page

#Results
@app.route("/results", methods=['GET', 'POST'])    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def results_page(FirstName):

        form_data = request.form

        gender = form_data["selectGender"]
        firstName = form_data["FirstName"]
        lastName = form_data["LastName"]
        FirstNameImage = form_data["FirstNameImage"]
        LastNameImageme = form_data["LastNameImage"]
        FirstNamePronounciation = form_data["FirstNamePronounciation"]
        LastNamePronounciation = form_data["LastNamePronounciation"]        
        FreeTextContentFirstName = form_data["FirstNameFreeTextContent"]        
        FreeTextContentLastName = form_data["LastNameFreeTextContent"]  

        return render_template("display_page.html", firstName=firstName.results_page())

#debug
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
