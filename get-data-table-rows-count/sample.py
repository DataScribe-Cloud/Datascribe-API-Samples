#!/usr/bin/env python3
"""
Sample script for GET /data/data-table-rows-count endpoint
Gets count of table rows with optional filtering
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
    
    # Configuration - Update these values
    TABLE_NAME = "your_table_name"  # Replace with actual table name
    
    # Example filters (optional)
    FILTERS = [
        {
            "column": "status",
            "operator": "=",
            "value": "active"
        }
        # Add more filters as needed
    ]
    
    try:
        # Prepare parameters
        params = {'tableName': TABLE_NAME}
        
        # Add filters if specified
        if FILTERS:
            params['filters'] = json.dumps(FILTERS)
        
        print(f"Getting row count for table: {TABLE_NAME}")
        if FILTERS:
            print(f"With filters: {json.dumps(FILTERS, indent=2)}")
        
        response = client.get('/data/data-table-rows-count', params=params)
        
        if response.get('success', True):
            count = response.get('data', {}).get('count', 0)
            
            if FILTERS:
                print(f"Table '{TABLE_NAME}' has {count} rows matching the filters")
            else:
                print(f"Table '{TABLE_NAME}' has {count} total rows")
                
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to get table row count: {e}")

if __name__ == "__main__":
    main()