#!/usr/bin/env python3
"""
Sample script for GET /data/data-table endpoint
Gets specific table data with pagination
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.api_client import APIClient
from config import API_TOKEN

def main():
    # Initialize API client
    client = APIClient(token=API_TOKEN)
    
    # Configuration - Update these values
    TABLE_NAME = "your_table_name"  # Replace with actual table name
    STARTING_ROW = 0
    NUM_ROWS = 50
    
    try:
        # Get table data
        print(f"Fetching data from table: {TABLE_NAME}")
        params = {
            'tableName': TABLE_NAME,
            'startingRow': STARTING_ROW,
            'numRows': NUM_ROWS
        }
        
        response = client.get('/data/data-table', params=params)
        
        if response.get('success', True):
            data = response.get('data', {})
            rows = data.get('rows', [])
            
            print(f"Retrieved {len(rows)} rows (starting from row {STARTING_ROW})")
            
            # Display first few rows
            for i, row in enumerate(rows[:5]):  # Show first 5 rows
                print(f"Row {STARTING_ROW + i}: {row}")
            
            if len(rows) > 5:
                print(f"... and {len(rows) - 5} more rows")
                
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch table data: {e}")

if __name__ == "__main__":
    main()