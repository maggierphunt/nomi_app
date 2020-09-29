from flask import Flask, render_template, request, Response
from jinja2 import Template

app = Flask("nomi_app") #making an app

#Input page
@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def input_page():
        return render_template("user_input_page.html") #runs the landing page

#Results
@app.route("/results", methods=['GET', 'POST'])    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def results_page(firstName):
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


#About page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def about_page():
        return render_template("about_page.html") #runs the landing page

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
