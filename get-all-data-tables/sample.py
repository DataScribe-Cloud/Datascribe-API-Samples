#!/usr/bin/env python3
"""
Sample script for GET /data/data-tables endpoint
Gets all data tables (requires admin privileges)
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient
from config import API_TOKEN

def main():
    # Initialize API client
    client = APIClient(token=API_TOKEN)
    
    try:
        # Get all data tables
        print("Fetching all data tables...")
        response = client.get('/data/data-tables')
        
        if response.get('success', True):
            tables = response.get('data', [])
            print(f"Found {len(tables)} data tables:")
            
            for table in tables:
                print(f"- {table}")
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch data tables: {e}")

if __name__ == "__main__":
    main()