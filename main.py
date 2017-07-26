from flask import Flask, render_template, request, abort
from steamapi import core, user
from steamapi.errors import UserNotFoundError

app = Flask("Steamer")
core.APIConnection(api_key="YOURAWESOMEAPIKEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def hello(name=None):
    try:
        steam_user = user.SteamUser(userurl=name)
    except UserNotFoundError:
        abort(404)
    nickname = steam_user.name
    img = steam_user.avatar
    return render_template('hello.html', name=name, nickname=nickname, friends=steam_user.friends,img=img)

@app.route('/post', methods=["POST"])
def post():
    friends= {}
    group = request.form.getlist("friends")
    myname = request.form["name"].lower()
    try:
        my_games = user.SteamUser(userurl=myname).games
    except UserNotFoundError:
        abort(404)
    intersection = my_games

    friends[myname] = {"name": myname,
                       "count": len(my_games),
                       "games": my_games}

    for friend_id in group:
        friend = user.SteamUser(userid=friend_id)
        friends[friend.name] = {"id": friend.id,
                                "name": friend.name,
                                "count": len(friend.games),
                                "games": friend.games}
        intersection = list(set(intersection) & set(friend.games))

    return  render_template('group.html',amount=len(intersection), friends=friends, intersection=intersection)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
