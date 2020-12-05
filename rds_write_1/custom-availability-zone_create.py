#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-custom-availability-zone.html
if __name__ == '__main__':
    """
	delete-custom-availability-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-custom-availability-zone.html
	describe-custom-availability-zones : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-custom-availability-zones.html
    """

    parameter_display_string = """
    # custom-availability-zone-name : The name of the custom Availability Zone (AZ).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "create-custom-availability-zone", "custom-availability-zone-name", add_option_dict)





