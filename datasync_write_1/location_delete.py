#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-location.html
if __name__ == '__main__':
    """
	list-locations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-locations.html
    """

    parameter_display_string = """
    # location-arn : The Amazon Resource Name (ARN) of the location to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("datasync", "delete-location", "location-arn", add_option_dict)





