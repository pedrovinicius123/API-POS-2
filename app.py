from app import create_app

# Creating app
app = create_app()

# Defining main routes
@app.route("/")
def home():
    return "This is the home of an awesome API!"
