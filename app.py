import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello!"

@app.route("/yo")
def howAreYou():
    return "Yo back to you!"

if __name__ == "__main__":
    app.run()