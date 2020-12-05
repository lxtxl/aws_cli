#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database-snapshot.html
if __name__ == '__main__':
    """
	create-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database-snapshot.html
	get-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshot.html
	get-relational-database-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshots.html
    """

    parameter_display_string = """
    # relational-database-snapshot-name : The name of the database snapshot that you are deleting.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-relational-database-snapshot", "relational-database-snapshot-name", add_option_dict)





