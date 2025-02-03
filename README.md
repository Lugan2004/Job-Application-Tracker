# Job Application Tracker

## Overview
A web application built with Flask that helps you track and manage your job applications efficiently. Easily record, update, and monitor your job search progress.

## Features
- **Add Job Applications**: 
  - Record company name, salary, date applied, and decision status
  - Required fields marked with 🔴
  - Automatic ZAR currency formatting for salary

- **Job Application Management**:
  - View all submitted job applications in a clean, organized table
  - Edit decision status for each application
  - Delete individual job applications
  - Clear all job applications with a single click

- **Data Export**:
  - Download job applications as an Excel (.xlsx) file
  - Persistent storage using Excel spreadsheet

- **User Interface**:
  - Responsive design with Tailwind CSS
  - Animated heading
  - Color-coded status indicators
  - Clean, modern layout

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/job-application-tracker.git
   cd job-application-tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install flask openpyxl
   ```

## Running the Application
```bash
python app.py
```
Open a web browser and navigate to `http://localhost:5000`

## Technologies Used
- Flask (Python web framework)
- Tailwind CSS
- Openpyxl (Excel file manipulation)
- JavaScript (AJAX for dynamic updates)



