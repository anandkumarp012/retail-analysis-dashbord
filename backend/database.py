import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import certifi

load_dotenv()

# MongoDB connection string - using localhost by default
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "retail_dashboard")

# Set a shorter timeout so it doesn't hang if Mongo isn't running
mongo_options = {
    "serverSelectionTimeoutMS": 5000,
    "connectTimeoutMS": 20000,
    "socketTimeoutMS": 20000,
}

# Atlas/SRV uses TLS; certifi helps avoid platform certificate issues.
if MONGO_URL.startswith("mongodb+srv://"):
    mongo_options["tls"] = True
    mongo_options["tlsCAFile"] = certifi.where()

client = AsyncIOMotorClient(MONGO_URL, **mongo_options)
db = client[DATABASE_NAME]

async def get_database():
    # Return the db object directly. 
    # The actual connection check happens when we perform an operation.
    return db
