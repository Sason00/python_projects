from bottle import get, post, request, run # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username, password)
    if username == "a" and password == "b":
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080)