from bottle import request, post, get, route, template, run

tasks = []
descriptions = []

@route("/")
def main_paige():
    if len(request.query.heading) >= 1:
        tasks.append(request.query.heading)
        descriptions.append(request.query.text)
    if len(tasks) >= 1:
        return template("/Users/rylwrn/Desktop/random_things/list_to_do_template.html", tasks=tasks, des=descriptions)
    else:
        return template("/Users/rylwrn/Desktop/random_things/list_to_do_template.html", tasks=[], des=[])

@route("/add-tasks")
def hi():
    return template("/Users/rylwrn/Desktop/random_things/list_to_to_template2.html")

@route("/change/<task>")
def edit_task(task):
    t, n = task.split("-")
    n = int(n)
    template = """
        <html>
        <body>
        <form action="/">
            heading: <input type="text" name="heading" id="heading" value="{}"><br>
            description: <br><textarea name="text" id="text" style="overflow:auto;resize:none" cols="30" rows="10">{}</textarea>
            <input type="submit" value="submit">
        </form>
        </body>
        </html>
    """.format(tasks[n], descriptions[n])
    return template

@route("/remove/<task>")
def remove_task(task):
    t, n = task.split("-")
    n = int(n)
    tasks.remove(tasks[n])
    descriptions.remove(descriptions[n])
    template = """
        <html>
        <body>
        <form action="/">
            <b>task was removed successfuly</b>
            <input type="submit" value="return">
        </form>
        </body>
        </html>
    """
    return template

run(host="localhost", port=8080)