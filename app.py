# app.py

from flask import Flask, render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    # Call your Tkinter quiz application here
    # For simplicity, let's assume your Tkinter app is in a file named quiz_app.py
    import subprocess
    subprocess.Popen(["python", "main.py"])  # Replace with your actual file name

    return "Quiz started!"

if __name__ == '__main__':
    app.run(debug=True)
