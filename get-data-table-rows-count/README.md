# Get Data Table Rows Count

Retrieves the count of rows in a data table with optional filtering.

## Endpoint
**GET** `/data/data-table-rows-count`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User (`datascribeApiEndpointUserPrivilege`)

## Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tableName` | string | Yes | Name of the table to count rows for |
| `filters` | string | No | JSON array of filter objects |

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
  "data": {
    "count": 1250,
    "tableName": "users",
    "filtersApplied": true
  }
}
```

## Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data``` (object): Contains count information
- ```count``` (integer): Number of rows matching the criteria
- ```tableName``` (string): Name of the table queried
- ```filtersApplied``` (boolean): Whether filters were applied


## Error Responses
```json
{
  "success": false,
  "data": "Missing required parameter: tableName"
}
```
```json
{
  "success": false,
  "data": "filters must be a valid JSON array of where clause objects"
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
- Filters use the same format as /data/data-table-rows endpoint
- Filters are applied with AND logic (all conditions must be true)
- Useful for pagination planning and data analysis
- More efficient than fetching all rows just to count them
- Returns 0 if no rows match the criteria