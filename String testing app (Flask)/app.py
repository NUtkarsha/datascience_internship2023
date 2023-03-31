from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']

        # Find all matches using regular expression
        matches = re.findall(regex_pattern, test_string)

        # Redirect to the results page
        return redirect(url_for('results', matches=matches))

    # If the request method is GET or there are no matches, render the input page
    return render_template('input.html')

@app.route('/results')
def results():
    matches = request.args.getlist('matches')

    # Render the results page with the matched strings
    return render_template('results.html', matches=matches)
if __name__ == '__main__':
    app.run(debug=True)