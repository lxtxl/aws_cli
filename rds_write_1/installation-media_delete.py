#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-installation-media.html
if __name__ == '__main__':
    """
	describe-installation-media : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-installation-media.html
	import-installation-media : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/import-installation-media.html
    """

    parameter_display_string = """
    # installation-media-id : The installation medium ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-installation-media", "installation-media-id", add_option_dict)





