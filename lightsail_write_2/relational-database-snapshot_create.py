#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database-snapshot.html
if __name__ == '__main__':
    """
	delete-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database-snapshot.html
	get-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshot.html
	get-relational-database-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshots.html
    """

    parameter_display_string = """
    # relational-database-name : The name of the database on which to base your new snapshot.
    # relational-database-snapshot-name : The name for your new database snapshot.
Constraints:

Must contain from 2 to 255 alphanumeric characters, or hyphens.
The first and last character must be a letter or number.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "create-relational-database-snapshot", "relational-database-name", "relational-database-snapshot-name", add_option_dict)
