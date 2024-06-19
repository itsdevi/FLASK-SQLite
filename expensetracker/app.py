from flask import Flask, render_template, request,redirect ,url_for
import expense_tracker

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods =['GET','POST'])
def add_expense():
    if request.method == 'POST':
        amount= request.form['amount']
        category= request.form['category']
        date = request.form['date']
        expense_tracker.add_one(amount,category,date)
        return redirect(url_for('index'))
    return render_template('add_expenses.html')

@app.route('/view')
def view_expenses():
    expenses = expense_tracker.show_all()
    return render_template('view_expenses.html', expenses=expenses)

@app.route('/filter')
def filter_expenses():
    if request.method=='GET':
        category = request.args.get(category)
        filtered = expense_tracker.filter_by_category(category)
        return render_template('filter_expenses.html' , expenses = filtered)
    return render_template('filter_expenses.html', expenses = [])


@app.route('/report')
def generate_report():
    report= expense_tracker.generate_report_by_category()
    return render_template('report.html',report=report)


if __name__ == '__main__':
    app.run(debug = True)