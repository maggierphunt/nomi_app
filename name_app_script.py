from flask import Flask, render_template, request, Response

#Home page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("landing_page.html") #runs the landing page

#Input page
@app.route("/input")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("user_input_page.html") #runs the landing page

#Results
@app.route("/results")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("user_results_page.html") #runs the landing page


#About page
@app.route("/about")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("about_page.html") #runs the landing page

app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.