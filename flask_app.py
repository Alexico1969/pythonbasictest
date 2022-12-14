from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session

challenges = [
    [1, "Send the following message to the screen: 'Hello, World!'", ["print('Hello, World!')", 'print("Hello, World!")']],
    [2, "Create a variable called 'name' and assign it the value 'Bruce Wayne'", ["name = 'Bruce Wayne'", 'name = "Bruce Wayne"',"name='Bruce Wayne'", 'name="Bruce Wayne"',]],
    [3, "Create a variable called 'age' and assign it the value 35", ["age = 35","age=35"]],
    [4, "Prompt a user, asking 'Please provide name: ', saved in a variable called 'n'", ["n = input('Please provide name: ')", 'n = input("Please provide name: ")', 'n=input("Please provide name: ")', 'n=input("Please provide name: ")']],
    [5, "Prompt a user, asking 'Please provide age: ', convert to int and saved in a variable called 'a'", ["a = int(input('Please provide age: '))", 'a = int(input("Please provide age: "))', 'a=int(input("Please provide age: "))', 'a=int(input("Please provide age: "))']],
    [6, "Create a for loop, using variable 'i' that will start at 0 and end before 10", ["for i in range(10):", "for i in range(0, 10):", "for i in range(0,10):"]],
    [7, "Create a while loop that will run until the variable 'i' is equal to 10", ["while i != 10:", "while i == 10:", "while i < 10:", "while i > 10:"]],
    [8, "Create a function called 'hello'", ["def hello():", "def hello():", "def hello():"]],
    [9, "Create a function called 'hello' that takes a parameter called 'name'", ["def hello(name):", "def hello(name):", "def hello(name):"]],

]


app = Flask(__name__)
app.secret_key = 'Bruce Wayne is Batman'

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    
    if 'nr' not in session:
        session['nr'] = 1
        nr = 1
    else:
        nr = session['nr']

    if request.method == 'POST':
        print("POST")
        code = request.form.get('code')
        print(code)

        if code in challenges[nr-1][2]:
            nr += 1
            session['nr'] = nr
            if nr > len(challenges):
                return render_template('message.html', message="AWESOME ! You've completed the challenge !", goto=url_for('winner'))
            return render_template('message.html', message="AWESOME ! Please continue with the next challenge !", goto=url_for('home'))
        else:
            print(f"code: {code} not in {challenges[nr-1][2]}")
            return render_template('message.html', message="That is not the correct code", goto=url_for('home'))


    challenge = challenges[nr-1][1]

    return render_template('home.html', nr=nr, challenge=challenge)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        print("POST")

        name = request.form.get('name')
        print(name)
        group = request.form.get('group')

        if not name:
            return render_template('message.html', message="Did you provide a name?", goto=url_for('login'))
        if " " not in name:
            return render_template('message.html', message="Did you provide a FIRST and LAST name?", goto=url_for('login'))
        if not group:
            return render_template('message.html', message="Did you choose a group?", goto=url_for('login'))

        session['name'] = name
        session['group'] = group

        return redirect(url_for('home'))



    return render_template('login.html')

@app.route('/winner')
def winner():
    name = session['name']
    group = session['group']
    return render_template('winner.html', name=name, group=group)

if __name__ == '__main__':
    app.run()