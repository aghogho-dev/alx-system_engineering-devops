#!/usr/bin/python3
"""Export to JSON."""
import json
import sys
import urllib.request

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    url_req = url + "users/{}".format(user_id)
    user_request = urllib.request.urlopen(url_req)
    user = json.loads(user_request.read().decode())
    username = user.get("username")
    url_todos = url + "todos?userId={}".format(user_id)
    todos_request = urllib.request.urlopen(url_todos)
    todos = json.loads(todos_request.read().decode())

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}, jsonfile)
