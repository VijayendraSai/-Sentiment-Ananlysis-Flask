from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Initialize PyMongo object
mongo = PyMongo()

def init_db(app):
    # Mongo URI from environment variable or default local
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/sentiment_analysis")
    mongo.init_app(app)
    print("MongoDB Atlas Connected!")
