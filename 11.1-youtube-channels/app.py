from flask import Flask, render_template

app = Flask(__name__)

# Дані про популярні YouTube-канали
channels = [
    {"id": 1, "name": "MrBeast", "subscribers": "200M+", "description": "Insane challenges & crazy giveaways!", "url": "https://www.youtube.com/c/MrBeast6000"},
    {"id": 2, "name": "Marques Brownlee", "subscribers": "17M+", "description": "High-quality tech reviews and insights.", "url": "https://www.youtube.com/c/mkbhd"},
    {"id": 3, "name": "Veritasium", "subscribers": "13M+", "description": "Science and engineering explained.", "url": "https://www.youtube.com/c/veritasium"},
    {"id": 4, "name": "Kurzgesagt", "subscribers": "21M+", "description": "Explaining the universe in a fun way.", "url": "https://www.youtube.com/c/Kurzgesagt"},
    {"id": 5, "name": "TEDx Talks", "subscribers": "38M+", "description": "Inspiring talks from around the world.", "url": "https://www.youtube.com/c/TEDxTalks"}
]

@app.route("/")
def home():
    return render_template("index.html", channels=channels)

@app.route("/channel/<int:id>")
def channel_detail(id):
    channel = next((c for c in channels if c["id"] == id), None)
    if channel:
        return render_template("channel.html", channel=channel)
    return "<h1>Channel not found</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)