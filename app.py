# Save this file as app.py
#
# REQUIRED LIBRARIES:
# pip install Flask pandas
#
# This script will start a local web server that serves the index.html
# file and provides the project data from your CSV.

import pandas as pd
from flask import Flask, jsonify, render_template, send_from_directory

# Initialize the Flask application
# We tell Flask to look for the HTML file in the current directory.
app = Flask(__name__, template_folder='.')

# --- API Endpoint ---
@app.route('/api/projects')
def get_projects():
    """
    Reads the Projects.csv file, converts it to JSON, and returns it.
    """
    try:
        # Read the CSV file using the pandas library.
        df = pd.read_csv('Projects.csv')

        # Replace any empty cells (NaN) with empty strings.
        df = df.fillna('')

        # IMPORTANT: Convert all column headers to lowercase.
        # This ensures the frontend gets data in a consistent format
        # regardless of the capitalization in the CSV file.
        df.columns = df.columns.str.lower()

        # Convert the cleaned data to a list of dictionaries (JSON format).
        projects = df.to_dict('records')

        # Return the data as a JSON response.
        return jsonify(projects)

    except FileNotFoundError:
        # Return a clear error if the CSV file is missing.
        return jsonify({"error": "Projects.csv not found. Make sure it's in the same directory as app.py."}), 404
    except Exception as e:
        # Return a general error for any other issues.
        return jsonify({"error": f"An error occurred while reading the CSV file: {e}"}), 500

# --- Frontend Route ---
@app.route('/')
def index():
    """
    Serves the main index.html page.
    """
    return render_template('index.html')

# --- Main execution block ---
if __name__ == '__main__':
    # This code runs when you execute "python app.py"
    print("======================================================")
    print("  Starting the Project Viewer server...")
    print("  Open your browser and navigate to: http://127.0.0.1:5000")
    print("  Press CTRL+C to stop the server.")
    print("======================================================")
    
    # Run the Flask app. debug=True allows for easier development.
    app.run(debug=True, port=5000)

