import flask
import json
import os
import requests

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as config:
            return json.load(config)
    else:
        print("ERROR: config.json file in / not found! Using web formular.")
        return {"API_KEY": "", "CONFIG_ID": ""}

def save_config(config):
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)




app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    config = load_config()

    if config["API_KEY"] == "" or config["CONFIG_ID"] == "":

        if flask.request.method == "POST":
            config["API_KEY"] = flask.request.form["api_key"]
            config["CONFIG_ID"] = flask.request.form["config_id"]
            save_config(config)
            return flask.redirect("/")
   
        return flask.render_template("configuration.html")
    
    return flask.render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)