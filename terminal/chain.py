from sys import platform
from textwrap import dedent
from langchain.schema import HumanMessage, SystemMessage, AIMessage

history: list = [
    SystemMessage(content = dedent(f"""\
        You are a command line assistant. Given text input from a user, help build a series of console commands
        that will achieve the goals of the prompt. 
        - We are running on {platform}. Only return commands that will function on this platform.
        - Your responses will be one at a time, where each response is the command and nothing but the command.
        - When ready for the next command the user will say "--next" and you will respond with the next command.
        - When you reached the end of the terminal commands, respond with "--done".
        - You may answer questions not related to the terminal, just don't surround them in backticks.
        """)
    ),

    HumanMessage(content = "Build a basic Flask app."),
    AIMessage(content = "`pip install flask`"),

    HumanMessage(content = "--next"),
    AIMessage(content = "`mkdir basic_flask_app`"),

    HumanMessage(content = "--next"),
    AIMessage(content = dedent('''\
        `cat << 'EOF' > basic_flask_app/app.py
        from flask import Flask, render_template

        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/about')
        def about():
            return render_template('about.html')

        if __name__ == '__main__':
            app.run(debug=True)

        EOF`''')
    ),
    
    HumanMessage(content = "--next"),
    AIMessage(content = dedent('''\
        `cat << EOF > basic_flask_app/templates/index.html
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Flask App</title>
        </head>
        <body>
            <h1>Welcome to My Flask App</h1>
            <p>This is the home page!</p>
        </body>
        </html>
        EOF`''')
    ),

    HumanMessage(content="--next"),
    AIMessage(content=dedent('''\
        `cat << 'EOF' > basic_flask_app/templates/about.html
        <!DOCTYPE html>
        <html>
        <head>
            <title>About My Flask App</title>
        </head>
        <body>
            <h1>About My Flask App</h1>
            <p>This is a simple Flask app that demonstrates the use of templates!</p>
        </body>
        </html>
        EOF`''')
    ),

    HumanMessage(content="--next"),
    AIMessage(content="`python basic_flask_app/app.py`"),

    HumanMessage(content="--next"),
    AIMessage(content="--done"),

    HumanMessage(content="List my current directory"),
    AIMessage(content="`ls`"),

    HumanMessage(content="--next"),
    AIMessage(content="--done"),
    
    HumanMessage(content="Create a basic React app"),
    AIMessage(content="`npx create-react-app basic-app`"),

    HumanMessage(content="--next"),
    AIMessage(content="--done"),
]