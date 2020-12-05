#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-user : The name of a database user. If a user name matching DbUser exists in the database, the temporary user credentials have the same permissions as the existing user. If DbUser doesnât exist in the database and Autocreate is True , a new user is created using the value for DbUser with PUBLIC permissions. If a database user matching the value for DbUser doesnât exist and Autocreate is False , then the command succeeds but the connection attempt will fail because the user doesnât exist in the database.
For more information, see CREATE USER in the Amazon Redshift Database Developer Guide.
Constraints:

Must be 1 to 64 alphanumeric characters or hyphens. The user name canât be PUBLIC .
Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
First character must be a letter.
Must not contain a colon ( : ) or slash ( / ).
Cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
    # cluster-identifier : The unique identifier of the cluster that contains the database for which your are requesting credentials. This parameter is case sensitive.
    """

    execute_two_parameter("redshift", "get-cluster-credentials", "db-user", "cluster-identifier", parameter_display_string)