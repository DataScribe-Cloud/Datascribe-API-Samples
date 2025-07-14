#!/usr/bin/env python3
"""
Sample script for GET /data/data-table-columns endpoint
Gets column information for a specific table
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient
from config import API_TOKEN

def main():
    # Initialize API client
    client = APIClient(token=API_TOKEN)
    
    # Configuration - Update this value
    TABLE_NAME = "your_table_name"  # Replace with actual table name
    
    try:
        # Get table columns
        print(f"Fetching columns for table: {TABLE_NAME}")
        params = {'tableName': TABLE_NAME}
        
        response = client.get('/data/data-table-columns', params=params)
        
        if response.get('success', True):
            columns = response.get('data', [])
            
            print(f"Table '{TABLE_NAME}' has {len(columns)} columns:")
            for i, column in enumerate(columns, 1):
                print(f"{i}. {column}")
                
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch table columns: {e}")

if __name__ == "__main__":
    main()