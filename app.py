
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CodeQL Security Demo</h1>
    <p>This application is being used for an authorized penetration test.</p>
    <p>Try the /run endpoint.</p>
    """

@app.route("/run")
def run_command():
    command = request.args.get("command")

    allowed_commands = {
        "hello": "Hello!",
        "status": "System is running."
    }

    result = allowed_commands.get(command, "Invalid command.")
    return result

if __name__ == "__main__":
    app.run()
