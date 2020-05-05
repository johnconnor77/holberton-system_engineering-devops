#!/usr/bin/python3
"""
    Expand #0 script to export data in the CSV format
"""
import csv
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

        with open("{}.csv".format(user_id), mode="w") as file:
            csv2write = csv.writer(file, quoting=csv.QUOTE_ALL)

            for task in total_user_tasks:
                task_title = task.get('title')
                is_completed = task.get('completed')
                csv2write.writerow([user_id, user_name,
                                    is_completed, task_title])
    except KeyError:
        pass


if __name__ == "__main__":
    get_todolist_progress()
