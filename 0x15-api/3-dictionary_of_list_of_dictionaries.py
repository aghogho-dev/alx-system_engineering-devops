#!/usr/bin/python3
"""List of dictionaries."""
import json
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_request = urllib.request.urlopen(url + "users")
    users = json.loads(users_request.read().decode())

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
                } for t in json.loads(urllib.request.urlopen(
                    url + "todos?userId={}".format(
                        u.get("id"))).read().decode())]
                    for u in users}, jsonfile)
