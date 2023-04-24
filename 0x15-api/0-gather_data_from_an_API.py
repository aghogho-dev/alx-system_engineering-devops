#!/usr/bin/python3
"""TODO REST API."""
import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_request = urllib.request.urlopen(url + "users/{}".format(sys.argv[1]))
    user = json.loads(user_request.read().decode())
    url_todos = url + "todos?userId={}"
    todos_request = urllib.request.urlopen(url_todos.format(sys.argv[1]))
    todos = json.loads(todos_request.read().decode())

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}:".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
