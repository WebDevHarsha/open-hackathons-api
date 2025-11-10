#!/usr/bin/env python3
"""
Fetch hackathon data from MongoDB and save to data.json
"""
import json
import os
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

def convert_mongodb_to_json(doc):
    """Convert MongoDB document to JSON-serializable format"""
    if isinstance(doc, dict):
        return {key: convert_mongodb_to_json(value) for key, value in doc.items()}
    elif isinstance(doc, list):
        return [convert_mongodb_to_json(item) for item in doc]
    elif isinstance(doc, ObjectId):
        return str(doc)
    elif isinstance(doc, datetime):
        return doc.isoformat()
    else:
        return doc

def main():
    # Get MongoDB URI from environment variable
    mongodb_uri = os.environ.get('MONGODB_URI')
    
    if not mongodb_uri:
        raise ValueError("MONGODB_URI environment variable is not set")
    
    print("Connecting to MongoDB...")
    client = MongoClient(mongodb_uri)
    
    try:
        # Connect to the 'dumpy' database and 'hackathons' collection
        db = client['dumpy']
        collection = db['hackathons']
        
        print(f"Fetching data from database: dumpy, collection: hackathons")
        
        # Fetch all hackathons, sorted by date (newest first)
        # Filter for open hackathons if needed
        hackathons = list(collection.find({}))
        
        print(f"Found {len(hackathons)} hackathons")
        
        # Convert MongoDB documents to JSON-serializable format
        data = {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "count": len(hackathons),
            "hackathons": [convert_mongodb_to_json(doc) for doc in hackathons]
        }
        
        # Save to data.json
        output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Data successfully saved to {output_path}")
        print(f"Total hackathons: {len(hackathons)}")
        
    finally:
        client.close()

if __name__ == "__main__":
    main()
