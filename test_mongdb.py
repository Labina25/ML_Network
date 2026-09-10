from pymongo import MongoClient

# Replace <db_password> with your actual password
uri = "mongodb+srv://labinas2568_db_user:Labina123@cluster0.leyent2.mongodb.net/?appName=Cluster0"

# Create a new client
client = MongoClient(uri)

try:
    # Ping the server to confirm connection
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
finally:
    client.close()