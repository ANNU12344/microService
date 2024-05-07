from src.flask_server import app

# def run_grpc_server():
#     print("Running gRPC server")
#     with app.app_context():
#         serve()

def run_flask_server():
    print("Running Flask server")
    # Create all tables
    app.run(host='0.0.0.0', port=5000 , debug = True)

if __name__ == "__main__":
    run_flask_server()
