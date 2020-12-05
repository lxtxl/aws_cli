#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/batch-grant-permissions.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # entries : A list of up to 20 entries for resource permissions to be granted by batch operation to the principal.
(structure)

A permission to a resource granted by batch operation to the principal.
Id -> (string)

A unique identifier for the batch permissions request entry.

Principal -> (structure)

The principal to be granted a permission.
DataLakePrincipalIdentifier -> (string)

An identifier for the AWS Lake Formation principal.


Resource -> (structure)

The resource to which the principal is to be granted a permission.
Catalog -> (structure)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

Database -> (structure)

The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

Name -> (string)

The name of the database resource. Unique to the Data Catalog.


Table -> (structure)

The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

DatabaseName -> (string)

The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name -> (string)

The name of the table.

TableWildcard -> (structure)

A wildcard object representing every table under a database.
At least one of TableResource$Name or TableResource$TableWildcard is required.


TableWithColumns -> (structure)

The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.
CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

DatabaseName -> (string)

The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name -> (string)

The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames -> (list)

The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.
(string)

ColumnWildcard -> (structure)

A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.
ExcludedColumnNames -> (list)

Excludes column names. Any column with this name will be excluded.
(string)



DataLocation -> (structure)

The location of an Amazon S3 path where permissions are granted or revoked.
CatalogId -> (string)

The identifier for the Data Catalog where the location is registered with AWS Lake Formation. By default, it is the account ID of the caller.

ResourceArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the data location resource.



Permissions -> (list)

The permissions to be granted.
(string)

PermissionsWithGrantOption -> (list)

Indicates if the option to pass permissions is granted.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lakeformation", "batch-grant-permissions", "entries", add_option_dict)





