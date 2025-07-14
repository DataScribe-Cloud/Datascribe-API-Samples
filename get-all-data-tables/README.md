# Get All Data Tables

Retrieves a list of all data tables in the system. This endpoint requires administrative privileges.

## Endpoint
**GET** `/data/data-tables`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: Datascribe Administrator

## Parameters
None

## Response Format
```json
{
  "success": true,
  "data": [
    "table_name_1",
    "table_name_2",
    "table_name_3"
  ]
}
```
## Response Fields
 - ```success``` (boolean): Indicates if the request was successful
 - ```data``` (array): Array of table names (strings)

## Error Responses
```json
{
  "success": false,
  "data": "Error message describing the issue"
}
```

## Status Codes
- ```200```: Success
- ```401```: Unauthorized (invalid or missing token)
- ```403```: Forbidden (insufficient privileges)
- ```500```: Internal Server Error

## Notes
- This endpoint is restricted to administrators only
- Returns all tables in the system regardless of user permissions
- Use ```/data/data-tables-for-user``` for user-specific table access