#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/generate-db-auth-token.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # hostname : The hostname of the database to connect to.
    # port : The port number the database is listening on.
    # username : The username to log in as.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "generate-db-auth-token", "hostname", "port", "username", add_option_dict)
