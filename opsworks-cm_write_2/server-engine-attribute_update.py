#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/update-server-engine-attributes.html
if __name__ == '__main__':
    """
	export-server-engine-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/export-server-engine-attribute.html
    """

    parameter_display_string = """
    # server-name : The name of the server to update.
    # attribute-name : The name of the engine attribute to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks-cm", "update-server-engine-attributes", "server-name", "attribute-name", add_option_dict)
