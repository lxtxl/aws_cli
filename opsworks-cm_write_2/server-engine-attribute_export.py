#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/export-server-engine-attribute.html
if __name__ == '__main__':
    """
	update-server-engine-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/update-server-engine-attributes.html
    """

    parameter_display_string = """
    # export-attribute-name : The name of the export attribute. Currently, the supported export attribute is Userdata . This exports a user data script that includes parameters and values provided in the InputAttributes list.
    # server-name : The name of the server from which you are exporting the attribute.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks-cm", "export-server-engine-attribute", "export-attribute-name", "server-name", add_option_dict)
