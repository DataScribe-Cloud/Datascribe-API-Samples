#!/usr/bin/env python3
"""
Sample script for GET /data/data-table-rows endpoint
Gets table rows with specific columns, filtering, and pagination
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
    COLUMNS = ["column1", "column2", "column3"]  # Replace with actual column names
    STARTING_ROW = 0
    NUM_ROWS = 25
    
    # Example filters (optional)
    FILTERS = [
        {
            "column": "status",
            "operator": "=",
            "value": "active"
        }
        # Add more filters as needed
        # {
        #     "column": "created_date",
        #     "operator": ">=",
        #     "value": "2024-01-01"
        # }
    ]
    
    try:
        # Prepare parameters
        params = {
            'tableName': TABLE_NAME,
            'columns': ','.join(COLUMNS),
            'startingRow': STARTING_ROW,
            'numRows': NUM_ROWS
        }
        
        # Add filters if specified
        if FILTERS:
            params['filters'] = json.dumps(FILTERS)
        
        print(f"Fetching rows from table: {TABLE_NAME}")
        print(f"Columns: {', '.join(COLUMNS)}")
        print(f"Rows: {STARTING_ROW} to {STARTING_ROW + NUM_ROWS}")
        
        if FILTERS:
            print(f"Filters: {json.dumps(FILTERS, indent=2)}")
        
        response = client.get('/data/data-table-rows', params=params)
        
        if response.get('success'):
            rows = response.get('data', [])
            
            print(f"\nRetrieved {len(rows)} rows:")
            
            # Display rows
            for i, row in enumerate(rows):
                print(f"Row {STARTING_ROW + i + 1}:")
                for col in COLUMNS:
                    value = row.get(col, 'N/A')
                    print(f"  {col}: {value}")
                print()
                
        else:
            print(f"Error: {response.get('data', 'Unknown error')}")
            
    except Exception as e:
        print(f"Failed to fetch table rows: {e}")

if __name__ == "__main__":
    main()