# Get Data Table Rows

Retrieves specific rows from a data table with column selection, filtering, and pagination.

## Endpoint
**GET** `/data/data-table-rows`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User (`datascribeApiEndpointUserPrivilege`)

## Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `tableName` | string | Yes | - | Name of the table to query |
| `columns` | string | Yes | - | Comma-separated list of column names |
| `startingRow` | integer | No | 0 | Starting row index (0-based) |
| `numRows` | integer | No | 100 | Number of rows to return (max 1000) |
| `filters` | string | No | - | JSON array of filter objects |

## Filter Format
The `filters` parameter accepts a JSON array of filter objects:

```json
[
  {
    "column": "status",
    "operator": "=",
    "value": "active"
  },
  {
    "column": "created_date",
    "operator": ">=",
    "value": "2024-01-01"
  }
]
```

## Supported Operators

- ```=``` - Equals
- ```!=``` - Not equals
- ```>``` - Greater than
- ```>=``` - Greater than or equal
- ```<``` - Less than
- ```<=``` - Less than or equal
- ```LIKE``` - Pattern matching
- ```IN``` - Value in list
- ```NOT IN``` - Value not in list

## Response Format
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com"
    },
    {
      "id": 2,
      "username": "jane_smith",
      "email": "jane@example.com"
    }
  ]
}
```

## Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data``` (array): Array of row objects containing only requested columns

## Error Responses
```json
{
  "success": false,
  "data": "Missing required parameter: tableName"
}
```

## Status Codes

- ```200```: Success
- ```400```: Bad Request (missing parameters, invalid filters, invalid table access)
- ```401```: Unauthorized (invalid or missing token)
- ```403```: Forbidden (insufficient privileges)
- ```500```: Internal Server Error

## Notes

- User must have access to the specified table
- All specified columns must exist in the table
- Filters are applied with AND logic (all conditions must be true)
- Maximum 1000 rows per request
- Column names are case-sensitive
- Invalid filter operators will return a 400 error