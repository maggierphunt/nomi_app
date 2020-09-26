from flask import Flask, render_template, request, Response

app = Flask("nomi_app") #making an app

#Home page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("about_page.html") #runs the landing page

#Input page
@app.route("/input")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("user_input_page.html") #runs the landing page

#Results
@app.route("/results", methods=['POST'])    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        form_data = request.form

        FirstName = form_data["FirstName"]
        LastName = form_data["LastName"]
        NameScriptImageFirstName = form_data["NameScriptImageFirstName"]
        NameScriptImageLastName = form_data["NameScriptImageLastName"]
        FirstNamePronounciation = form_data["FirstNamePronounciation"]
        LastNamePronounciation = form_data["LastNamePronounciation"]        
        FreeTextContentFirstName = form_data["FreeTextContentFirstName"]        
        FreeTextContentLastName = form_data["FreeTextContentLastName"]  

        return render_template("display_page.html") #runs the landing page


#About page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("about_page.html") #runs the landing page

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
