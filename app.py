from flask import Flask
import os
from flask_cors import CORS
from routes.crud_route import crud_router


app = Flask(__name__)   

CORS(app)

# Register the routes blueprint
app.register_blueprint(crud_router,url_prefix="/api")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)