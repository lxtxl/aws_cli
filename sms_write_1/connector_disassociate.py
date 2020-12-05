#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/disassociate-connector.html
if __name__ == '__main__':
    """
	get-connectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-connectors.html
    """

    parameter_display_string = """
    # connector-id : The ID of the connector.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sms", "disassociate-connector", "connector-id", add_option_dict)





