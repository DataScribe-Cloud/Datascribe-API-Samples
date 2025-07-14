# API Sample Scripts

This repository contains sample Python scripts demonstrating how to use the Data API endpoints.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   export DATASCRIBE_API_BASE_URL="https://datascribe.cloud/data"
   export DATASCRIBE_API_TOKEN="your_api_token_here"
   ```

   Or create a `.env` file:
   ```
   DATASCRIBE_API_BASE_URL=https://datascribe.cloud/data
   DATASCRIBE_API_TOKEN=your_api_token_here
   ```

## Usage

Each endpoint has its own directory with:
- `sample.py` - Working example script
- `README.md` - Endpoint-specific documentation

Run any sample script:
```bash
cd get-data-tables-for-user
python sample.py
```

## Available Endpoints

- `get-all-data-tables/` - Get all data tables (admin only)
- `get-data-tables-for-user/` - Get data tables for authenticated user
- `get-data-table/` - Get specific table data with pagination
- `get-data-table-metadata/` - Get table metadata information
- `get-data-table-columns/` - Get table column information
- `get-data-table-rows/` - Get table rows with filtering and pagination
- `get-data-table-rows-count/` - Get count of table rows with filtering

## Common Error Codes

| Code | Description | Common Causes |
|------|-------------|---------------|
| 400 | Bad Request | Missing parameters, invalid filters, no table access |
| 401 | Unauthorized | Invalid or missing authentication token |
| 403 | Forbidden | Insufficient privileges for the endpoint |
| 404 | Not Found | Table doesn't exist or endpoint not found |
| 500 | Internal Server Error | Server-side error, database issues |

## Common Error Messages
- `"Missing required parameter: tableName"` - tableName parameter not provided
- `"Bad Request. User is not part of the organization that owns this table."` - User lacks access to private table
- `"filters must be a valid JSON array of where clause objects"` - Invalid filter format
- `"numRows must be a valid positive integer (max 1000)"` - Invalid pagination parameters
