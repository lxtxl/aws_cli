#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-host.html
if __name__ == '__main__':
    """
	create-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-host.html
	get-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-host.html
	list-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-hosts.html
    """

    parameter_display_string = """
    # host-arn : The Amazon Resource Name (ARN) of the host to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codestar-connections", "delete-host", "host-arn", add_option_dict)





