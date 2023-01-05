import os
from taskmanager import app


if __name__ == "__main__":  # Tells our app 'how' and 'where' to run our app
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
