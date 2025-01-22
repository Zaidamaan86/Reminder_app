@app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):
#     update = reminder.query.filter_by(sno=sno).first()  # Fetch the reminder to update

#     if request.method == 'POST':
#         # Debugging: print all form keys to check if 'reminder' and 'desc' exist
#         print(request.form)  # This will print all form data
        
#         if 'reminder' in request.form and 'desc' in request.form:
#             update.reminder = request.form['reminder']
#             update.desc = request.form['desc']
#             db.session.commit()
#             return redirect(url_for('Hello_world'))
#         else:
#             print("Form data is missing some fields.")
#             # You can also handle this case by returning an error message or redirecting
            
#     return render_template('update.html', update=update)  # Render the update form for GET requests
