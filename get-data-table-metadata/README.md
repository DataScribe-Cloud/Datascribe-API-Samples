# Get Data Table Metadata

Retrieves metadata information for a specific data table.

## Endpoint
**GET** `/data/data-table-metadata`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User

## Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tableName` | string | Yes | Name of the table to get metadata for |

## Response Format
```json
{
  "success": true,
  "data": {
    "tableName": "users",
    "rowCount": 1000,
    "columnCount": 15,
    "createdDate": "2024-01-15T10:30:00Z",
    "lastUpdated": "2024-01-20T14:45:00Z",
    "description": "User data table",
    "isPublic": false,
    "owner": "organization_name"
  }
}
```

## Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data ``` (object): Contains table metadata
- ```tableName``` (string): Name of the table
- ```rowCount``` (integer): Total number of rows
- ```columnCount``` (integer): Total number of columns
- ```createdDate``` (string): ISO date when table was created
- ```lastUpdated``` (string): ISO date when table was last updated
- ```description``` (string): Table description
- ```isPublic``` (boolean): Whether table is publicly accessible
- ```owner``` (string): Organization that owns the table



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
- ```401```: Unauthorized (invalid or missing token).
- ```403```: Forbidden (insufficient privileges)
- ```500```: Internal Server Error

## Notes

- User must have access to the specified table
- Metadata includes both structural and ownership information
- Useful for understanding table structure before querying data