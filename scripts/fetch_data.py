#!/usr/bin/env python3

import json
import os
import re
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

def convert_mongodb_to_json(doc):
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

def extract_prize_value(prize_text):
    """Extract numeric value from prize text for sorting"""
    if not prize_text:
        return 0
    # Remove HTML tags and extract numbers
    clean_text = re.sub(r'<[^>]*>', '', prize_text)
    # Try to find numbers
    numbers = re.findall(r'[\d,]+', clean_text)
    if numbers:
        # Take the first number found, remove commas
        return int(numbers[0].replace(',', ''))
    return 0

def save_json(filepath, data):
    """Save data to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    mongodb_uri = os.environ.get('MONGODB_URI')
    
    if not mongodb_uri:
        raise ValueError("MONGODB_URI environment variable is not set")
    
    print("Connecting to MongoDB...")
    client = MongoClient(mongodb_uri)
    
    try:
        db = client['dumpy']
        collection = db['hackathons']
        
        print(f"Fetching data from database: dumpy, collection: hackathons")
        
        hackathons = list(collection.find({}))
        
        print(f"Found {len(hackathons)} hackathons")
        
        converted_hackathons = [convert_mongodb_to_json(doc) for doc in hackathons]
        
        last_updated = datetime.utcnow().isoformat() + "Z"
        output_dir = os.path.dirname(os.path.dirname(__file__))
        
        data_all = {
            "last_updated": last_updated,
            "count": len(converted_hackathons),
            "hackathons": converted_hackathons
        }
        save_json(os.path.join(output_dir, 'data.json'), data_all)
        print(f"✓ Saved data.json - {len(converted_hackathons)} hackathons")
        
        online_hackathons = [h for h in converted_hackathons 
                            if h.get('displayed_location', '').strip().lower() == 'online']
        data_online = {
            "last_updated": last_updated,
            "count": len(online_hackathons),
            "hackathons": online_hackathons
        }
        save_json(os.path.join(output_dir, 'data-online.json'), data_online)
        print(f"✓ Saved data-online.json - {len(online_hackathons)} hackathons")
        
        offline_hackathons = [h for h in converted_hackathons 
                             if h.get('displayed_location', '').strip().lower() not in ['online', '']]
        data_offline = {
            "last_updated": last_updated,
            "count": len(offline_hackathons),
            "hackathons": offline_hackathons
        }
        save_json(os.path.join(output_dir, 'data-offline.json'), data_offline)
        print(f"✓ Saved data-offline.json - {len(offline_hackathons)} hackathons")
        
        featured_hackathons = [h for h in converted_hackathons if h.get('featured') == True]
        data_featured = {
            "last_updated": last_updated,
            "count": len(featured_hackathons),
            "hackathons": featured_hackathons
        }
        save_json(os.path.join(output_dir, 'data-featured.json'), data_featured)
        print(f"✓ Saved data-featured.json - {len(featured_hackathons)} hackathons")
        
        hackathons_with_prize = [h for h in converted_hackathons if h.get('prizeText')]
        sorted_by_prize = sorted(
            hackathons_with_prize,
            key=lambda x: extract_prize_value(x.get('prizeText', '')),
            reverse=True
        )
        data_by_prize = {
            "last_updated": last_updated,
            "count": len(sorted_by_prize),
            "hackathons": sorted_by_prize
        }
        save_json(os.path.join(output_dir, 'data-by-prize.json'), data_by_prize)
        print(f"✓ Saved data-by-prize.json - {len(sorted_by_prize)} hackathons")
        
        print(f"\n✅ All endpoints generated successfully!")
        print(f"   Total: {len(converted_hackathons)}")
        print(f"   Online: {len(online_hackathons)}")
        print(f"   Offline: {len(offline_hackathons)}")
        print(f"   Featured: {len(featured_hackathons)}")
        print(f"   With Prizes: {len(sorted_by_prize)}")
        
    finally:
        client.close()

if __name__ == "__main__":
    main()
