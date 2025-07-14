# Get Data Table

Retrieves data from a specific table with pagination support.

## Endpoint
**GET** `/data/data-table`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User

## Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `tableName` | string | Yes | - | Name of the table to retrieve data from |
| `startingRow` | integer | No | 0 | Starting row index (0-based) |
| `numRows` | integer | No | 100 | Number of rows to return |

## Response Format
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "column1": "value1",
        "column2": "value2",
        "column3": "value3"
      }
    ],
    "totalRows": 1000,
    "startingRow": 0,
    "numRows": 100
  }
}
```

# Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data``` (object): Contains the table data and metadata
- ```rows``` (array): Array of row objects
- ```totalRows``` (integer): Total number of rows in the table
- ```startingRow``` (integer): Starting row index used
- ```numRows``` (integer): Number of rows returned


## Error Responses
```json
{
  "success": false,
  "data": "Missing required parameter: tableName"
}
```

## Status Codes

- ```200```: Success
- ```400```: Bad Request (missing parameters, invalid table access)
- ```401```: Unauthorized (invalid or missing token)
- ```403```: Forbidden (insufficient privileges)
- ```500```: Internal Server Error

Notes

User must have access to the specified table
Public tables don't require organization membership
Pagination is 0-based (first row is index 0)
Returns all columns for each row