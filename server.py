from flask import Flask, render_template, url_for,request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
   return render_template('project.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/index.html')
def index():
	return render_template('index.html')

def write_to_file(data):
	with open('database.txt', mode='a')as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',newline='',mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',',quotechar=':',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
	if request.method == 'POST':
	  data = request.form.to_dict()
	  write_to_csv(data)
	  return render_template('thankyou.html')
	else:
		return "null"
   