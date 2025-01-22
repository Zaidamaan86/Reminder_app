from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///E:/zaid amaan/python zaid/Flask/Pushup_logger/reminder.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class reminder(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    reminder = db.Column(db.String(200), nullable=True)
    desc = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.reminder} - {self.desc}"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def Hello_world():
    if request.method == 'POST':
        rem=reminder(reminder=request.form['reminder'], desc= request.form['desc'])
        db.session.add(rem)
        db.session.commit()
        return redirect(url_for('Hello_world'))
    
    allrem=reminder.query.all()
    return render_template('index.html', allrem=allrem)


# Route for deleting a single reminder
@app.route('/delete/<int:sno>', methods=['POST'])
def delete(sno):
    reminder_to_delete = reminder.query.filter_by(sno=sno).first()
    if reminder_to_delete:
        db.session.delete(reminder_to_delete)
        db.session.commit()  # Commit the deletion
    return redirect(url_for('Hello_world'))  # Redirect to home after deletion

# Route for deleting all reminders
@app.route('/delete_all', methods=['POST'])
def delete_all():
    db.session.query(reminder).delete()
    db.session.commit()  # Commit the deletion
    return redirect(url_for('Hello_world'))  # Redirect to home after deletion

# Route for update a reminder

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    update = reminder.query.filter_by(sno=sno).first()  # Fetch the reminder to update
    print(update)

    if request.method == 'POST':
        # Debugging: print all form keys to check if 'reminder' and 'desc' exist
        print(request.form)  # This will print all form data
        
        if 'reminder' in request.form and 'desc' in request.form:
            update.reminder = request.form['reminder']
            update.desc = request.form['desc']
            db.session.commit()
            return redirect(url_for('Hello_world'))
        else:
            print("Form data is missing some fields.")
            # You can also handle this case by returning an error message or redirecting
            
    return render_template('update.html', update=update)  # Render the update form for GET requests

@app.route('/about')
def about():
     return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)