# Get Data Table Columns

Retrieves column information for a specific data table.

## Endpoint
**GET** `/data/data-table-columns`

## Authentication
- **Required**: Yes
- **Type**: Bearer Token
- **Privilege Level**: User

## Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tableName` | string | Yes | Name of the table to get columns for |

## Response Format
```json
{
  "success": true,
  "data": [
    {
      "columnName": "id",
      "dataType": "integer",
      "nullable": false,
      "isPrimaryKey": true,
      "defaultValue": null
    },
    {
      "columnName": "username",
      "dataType": "varchar",
      "nullable": false,
      "isPrimaryKey": false,
      "defaultValue": null
    },
    {
      "columnName": "email",
      "dataType": "varchar",
      "nullable": true,
      "isPrimaryKey": false,
      "defaultValue": null
    }
  ]
}
```

## Response Fields

- ```success``` (boolean): Indicates if the request was successful
- ```data``` (array): Array of column objects
- ```columnName``` (string): Name of the column
- ```dataType``` (string): Data type of the column
- ```nullable``` (boolean): Whether column allows null values
- ```isPrimaryKey``` (boolean): Whether column is part of primary key
- ```defaultValue``` (any): Default value for the column


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

## Notes

- User must have access to the specified table
- Column information includes data types and constraints
- Useful for building dynamic queries and validating data
- Primary key information helps identify unique identifiers