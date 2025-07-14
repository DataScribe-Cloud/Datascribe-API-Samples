#!/usr/bin/env python3
"""
Sample script for GET /data/data-table-metadata endpoint
Gets metadata information for a specific table
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient
from config import API_TOKEN
import json

def main():
    # Initialize API client
    client = APIClient(token=API_TOKEN)
    
    # Configuration - Update this value
    TABLE_NAME = "your_table_name"  # Replace with actual table name
    
    try:
        # Get table metadata
        print(f"Fetching metadata for table: {TABLE_NAME}")
        params = {'tableName': TABLE_NAME}
        
        response = client.get('/data/data-table-metadata', params=params)
        
        if response.get('success', True):
            metadata = response.get('data', {})
            
            print("Table Metadata:")
            print(json.dumps(metadata, indent=2))
            
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch table metadata: {e}")

if __name__ == "__main__":
    main()