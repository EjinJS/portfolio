from flask import Flask, render_template,flash
from forms import ContactForm
from flask import request
import pandas as pd
from forms import ContactForm 

app = Flask(__name__)
app.secret_key = '9846636399'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact',methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res_html = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        html_code = res_html.to_html(header=False)
        html_file = open('table.html','a')
        html_file.write(html_code)
        res.to_csv('./contactusMessage.csv',mode='a',header=False)
        print("The data are saved !")
        #flash('Your message sented sucessfully')
        return render_template('index.html')
    else:
        return render_template('contact.html', form=form)

@app.route('/help')
def help():
    return render_template('help.html')



if __name__ == '__main__':
    app.run(debug=True)