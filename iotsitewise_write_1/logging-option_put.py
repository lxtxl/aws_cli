#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/put-logging-options.html
if __name__ == '__main__':
    """
	describe-logging-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-logging-options.html
    """

    parameter_display_string = """
    # logging-options : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "put-logging-options", "logging-options", add_option_dict)





