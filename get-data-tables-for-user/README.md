# Get Data Tables for User

Retrieves a list of data tables that the authenticated user has access to.

## Endpoint
**GET** `/data/data-tables-for-user`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User

## Parameters
None

## Response Format
```json
{
  "success": true,
  "data": [
    "accessible_table_1",
    "accessible_table_2",
    "public_table_1"
  ]
}
```

## Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data``` (array): Array of table names that the user can access

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

- Returns only tables the user has permission to access
- Includes both organization-specific tables and public tables
- Access is determined by user's organization membership