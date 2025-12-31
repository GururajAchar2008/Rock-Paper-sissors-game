from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key="supersecretkey"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loading', methods=['POST'])
def loading():
    choice = request.form['choice']
    return render_template('loading.html', choice=choice)

@app.route('/play/<choice>')
def play(choice):
    user_choice = choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")



