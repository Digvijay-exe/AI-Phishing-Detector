# AI-Phishing-Detector
Your personal AI guardian for a safer inbox.


#AI Phishing Detector

A simple and powerful web application designed to protect users from malicious emails by using an AI model to detect phishing attempts.

About The Project
This tool allows a user to paste the text of any suspicious email into a text box. With a single click, our AI model instantly analyzes the content and predicts whether the email is safe or a potential phishing attack. The result is displayed clearly, giving the user an immediate and easy-to-understand verdict.

Backend: Python, Flask, Scikit-learn

Frontend: HTML, CSS, JavaScript

How to Set Up and Run This Project
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
You will need to have the following software installed on your computer:

Python (Version 3.8 or higher recommended)

Git for cloning the repository

Step 1: Clone the Repository
First, clone the repository from GitHub to your local machine.

git clone [https://github.com/YOUR_USERNAME/AI-Phishing-Detector.git](https://github.com/YOUR_USERNAME/AI-Phishing-Detector.git)
cd AI-Phishing-Detector

(Remember to replace YOUR_USERNAME with your actual GitHub username!)

Step 2: Set Up a Virtual Environment
It's a best practice to create a virtual environment to manage project dependencies.

Create the virtual environment
python -m venv venv

Activate it (Windows)
.\venv\Scripts\activate

Activate it (macOS/Linux)
source venv/bin/activate

Step 3: Install Required Packages
Install all the necessary Python libraries using pip.

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file first. See the note below.)

Step 4: Run the Application
The project has two parts that need to be running.

1. Start the Backend Server:
In your terminal, run the following command. This will start the Flask server.

python app.py

Keep this terminal window open. You should see a message indicating the server is running on http://127.0.0.1:5000.

2. Open the Frontend:
Navigate to the project folder on your computer and double-click the index.html file. This will open the user interface in your default web browser.

How to Use the Detector
Once the application is running, using it is simple:

Find an email you want to check.

Copy the full text of the email.

Paste the text into the text box on the web page.

Click the "Check Email" button.

The AI's prediction (Safe Email or Phishing Email) will appear below the button.
