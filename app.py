from flask import Flask, render_template, jsonify

app = Flask(__name__)

# SGPA data for each semester
semester_data = [
    {"semester": 1, "sgpa": 8.2},
    {"semester": 2, "sgpa": 8.81},
    {"semester": 3, "sgpa": 8.2},
    {"semester": 4, "sgpa": 8.54},
    {"semester": 5, "sgpa": 8.64},
    {"semester": 6, "sgpa": 9.07},
    {"semester": 7, "sgpa": 9.04},

]

# Calculate CGPA
cgpa = round(sum(sem["sgpa"] for sem in semester_data) / len(semester_data), 2)

@app.route('/')
def index():
    """Main route - renders the Mario GPA tracker"""
    return render_template('index.html', 
                         semesters=semester_data, 
                         cgpa=cgpa)

@app.route('/api/grades')
def get_grades():
    """API endpoint to get all grades data"""
    return jsonify({
        'semesters': semester_data,
        'cgpa': cgpa
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
