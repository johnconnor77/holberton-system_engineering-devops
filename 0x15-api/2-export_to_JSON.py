#!/usr/bin/python3
"""
    Expand #0 script to export data in the JSON format
"""

import json
import requests
from sys import argv


def get_todolist_progress():
    """
    Get's the  to do list progress of a specified user
    """
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_info = requests.get(url + "users/{}"
                             .format(user_id)).json()
    total_user_tasks = requests.get(url + "todos?userId={}"
                                    .format(user_id)).json()

    try:

        user_name = user_info.get('username')

        json_data = []
        for task in total_user_tasks:
            todo_dict = {}

            task_title = task.get("title")
            is_completed = task.get("completed")

            todo_dict["task"] = task_title
            todo_dict["completed"] = is_completed
            todo_dict["username"] = user_name

            json_data.append(todo_dict)

        with open("{}.json".format(argv[1]), mode="w") as json_file:
            final_dict = {user_id: json_data}
            json.dump(final_dict, json_file)

    except KeyError:
        pass


if __name__ == "__main__":
    get_todolist_progress()
