# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import json

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'YTOIHWEFHGSI'


@app.route('/')
def main():
    output = render_template("index.html")
    return output


@app.route('/goals/<goal>/')
def show_goals(goal):
    output = render_template("goal.html")
    return output


@app.route('/profiles/<int:teacher_id>/')
def show_profiles(teacher_id):
    with open("teachers.json", "r") as teachers_file:
        teachers = json.loads(teachers_file.read())
        teachers_file.close()

    with open("goals.json", "r+") as goals_file:
        goals = json.loads(goals_file.read())
        goals_file.close()

    # Getting the goal list from the teachers.json
    user_goals_list = []
    time_available_list = []
    for teacher in teachers["teachers"]:
        if teacher_id == teacher["id"]:
            name = teacher["name"]
            picture = teacher["picture"]
            user_goals_list.append(teacher['goals'])
            rating = teacher["rating"]
            price = teacher["price"]
            about = teacher["about"]
            # Getting the available time for the teacher and add it to the list
            for key in teacher.get("free").values():
                print(key)





    # Compare if one list has the values in other list then save them to the new list
    total_goals = []
    for user_goal in user_goals_list:
        for each_goal in user_goal:
            if each_goal in goals.keys():
                total_goals.append(each_goal)

    output = render_template("profile.html",
                             teacher_id=teacher_id,
                             name=name,
                             picture=picture,
                             total_goals=total_goals,
                             rating=rating,
                             price=price,
                             about=about)
    return output


@app.route('/request/')
def get_request():
    output = render_template("request.html")
    return output


@app.route('/request_done/')
def request_sent():
    output = render_template("request_done.html")
    return output


@app.route('/booking/<teacher_id>/<week_day>/<booking_time>/')
def teacher_booking_form(teacher_id, week_day, booking_time):
    output = render_template("booking.html")
    return output


@app.route('/booking_done/')
def teacher_form_sent():
    output = render_template("booking_done.html")
    return output


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что то не так, но мы все починим"


if __name__ == '__main__':
    app.run()
toolbar = DebugToolbarExtension
