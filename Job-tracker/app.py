from flask import Flask, render_template, request, redirect, url_for, send_file
import openpyxl
import os

app = Flask(__name__)

# Path to the Excel file
EXCEL_FILE = 'jobs.xlsx'

# Ensure the Excel file exists with headers
if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Company Name', 'Salary'])
    wb.save(EXCEL_FILE)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form['company_name']
        salary = request.form['salary']

        # Load the Excel file
        wb = openpyxl.load_workbook(EXCEL_FILE)
        ws = wb.active

        # Append the new job application
        ws.append([company_name, salary])

        # Save the Excel file
        wb.save(EXCEL_FILE)

        return redirect(url_for('index'))

    # Read the Excel file to display its contents
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
    jobs = []
    for row in ws.iter_rows(min_row=1, values_only=True):
        jobs.append(row)

    return render_template('index.html', jobs=jobs)

@app.route('/download')
def download_file():
    # Send the Excel file for download
    return send_file(EXCEL_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)