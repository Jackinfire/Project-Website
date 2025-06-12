# Local Project Viewer

A simple, powerful, and entirely local web application for browsing, searching, and saving projects from a CSV file. Built with a Python (Flask) backend and a clean, responsive HTML/JavaScript frontend.

## 🚀 Features

This application provides a rich user interface to manage a list of projects with the following features:

- **Load from CSV**: Automatically loads all project data from a `Projects.csv` file in the project directory.
- **Powerful Search**: A single search bar to instantly filter projects by any keyword across all fields (title, supervisor, description, etc.).
- **Save Favorites**: Star your favorite projects and have them saved locally in your browser.
- **Filter by Saved**: Toggle a view to see only your saved projects.
- **Sorting**: Sort the project list by default order, title (A-Z), or supervisor name (A-Z).
- **Private Notes**: Add and save personal notes for any project. Your notes are stored locally and are private to your browser.
- **Recently Viewed**: A handy panel that keeps track of the last 5 projects you've viewed for quick navigation.
- **Clickable Supervisor**: Click a supervisor's name in the details view to instantly see all of their projects.
- **Random Project Discovery**: A "Random Project" button to help you discover projects you might have otherwise missed.
- **Data Export**: Export your list of saved projects to a new CSV file.
- **Clear Saved**: Easily clear all of your saved projects with a confirmation step.
- **Fully Responsive**: The layout adapts to all screen sizes, from mobile phones to desktop monitors.

## 🛠️ Setup and Installation

To get this project running on your local machine, follow these simple steps.

### Prerequisites

- **Python 3**: Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org).
- **pip**: The Python package installer, which usually comes with Python.

### 1. Set Up the Project Folder

Create a folder on your computer and place the following three files inside it:

- `app.py` (The Python backend server)
- `index.html` (The frontend user interface)
- `Projects.csv` (Your project data file)

Your folder structure must look like this:

```
/your-project-folder/
|-- app.py
|-- index.html
|-- Projects.csv
```

### 2. Install Required Libraries

Open your terminal or command prompt, navigate to your project folder, and run the following command to install the necessary Python libraries:

```
pip install Flask pandas
```

### 3. Run the Application

In the same terminal window (still inside your project folder), run the Python server:

```
python app.py
```
Or just run the file however you want

You will see a message indicating that the server is running and listening on [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 4. View the App

Open your favorite web browser and go to the following address:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

Your project dashboard should now be live!

## 📄 File Descriptions

- `app.py`: The backend of the application. This is a Flask server that reads the `Projects.csv` file, serves the `index.html` file, and provides the project data via a simple API.
- `index.html`: The frontend of the application. This file contains all the HTML structure, styling (via Tailwind CSS), and JavaScript logic for the user interface, interactivity, and communication with the backend.
- `Projects.csv`: The data source for the application. It must be in a standard CSV format with a header row. The column names can be capitalized as the Python backend will automatically handle them.