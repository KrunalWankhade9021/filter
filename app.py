from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    subject = request.form['subject']  # Get the subject from the form
    criteria = float(request.form['criteria'])  # Get the criteria

    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Read the uploaded CSV file
    df = pd.read_csv(file)

    # Filter the DataFrame based on the criteria
    toppers = df[df['PercentCorrect'] >= criteria]

    # Pass the toppers and subject to the template
    return render_template('toppers.html', toppers=toppers, subject=subject)

# The app is automatically started by Vercel serverless environment.
# If you were running this locally, you would still use app.run(), but Vercel handles this.

