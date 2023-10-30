from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample project data
    projects = [
        {"title": "Project 1", "description": "Description of Project 1"},
        {"title": "Project 2", "description": "Description of Project 2"},
        # Add more sample projects as needed
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)