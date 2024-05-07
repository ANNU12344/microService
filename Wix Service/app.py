from src.wix_server import app
def run_flask_server():
    print("Running Wix server")
    app.run(debug = True)

if __name__ == "__main__":
    run_flask_server()
