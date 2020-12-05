#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/export-snapshot.html
if __name__ == '__main__':
    """
	copy-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/copy-snapshot.html
    """

    parameter_display_string = """
    # source-snapshot-name : The name of the instance or disk snapshot to be exported to Amazon EC2.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "export-snapshot", "source-snapshot-name", add_option_dict)





