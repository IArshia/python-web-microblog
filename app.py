import datetime
from flask import Flask, render_template,request
from pymongo import MongoClient
def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://IArshia:arshiap13811381@microblogarshia.e6isflt.mongodb.net/test")
    app.db = client.microblog
    @app.route("/", methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            print([e for e in  app.db.entries.find({})])
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_many([{"content": entry_content, "date": formatted_date}])
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b-%d")      
            )
            for entry in app.db.entries.find({})
        ]    
        return render_template("Home.html", entries=entries_with_date)
    return app    
