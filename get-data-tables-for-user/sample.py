#!/usr/bin/env python3
"""
Sample script for GET /data/data-tables-for-user endpoint
Gets data tables available to the authenticated user
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
        # Get data tables for user
        print("Fetching data tables for user...")
        response = client.get('/data/data-tables-for-user')
        
        if response.get('success', True):
            tables = response.get('data', [])
            print(f"Found {len(tables)} accessible data tables:")
            
            for table in tables:
                print(f"- {table}")
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch user data tables: {e}")

if __name__ == "__main__":
    main()