#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-configuration-set-sending-options.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that you want to enable or disable email sending for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint-email", "put-configuration-set-sending-options", "configuration-set-name", add_option_dict)





