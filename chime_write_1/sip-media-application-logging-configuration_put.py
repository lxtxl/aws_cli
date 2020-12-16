#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-sip-media-application-logging-configuration.html
if __name__ == '__main__':
    """
	get-sip-media-application-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-media-application-logging-configuration.html
    """

    parameter_display_string = """
    # sip-media-application-id : The ID of the specified SIP media application
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "put-sip-media-application-logging-configuration", "sip-media-application-id", add_option_dict)





