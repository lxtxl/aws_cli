#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-listener.html
if __name__ == '__main__':
    """
	create-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-listener.html
	describe-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-listener.html
	list-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-listeners.html
	update-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-listener.html
    """

    parameter_display_string = """
    # listener-arn : The Amazon Resource Name (ARN) of the listener.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("globalaccelerator", "delete-listener", "listener-arn", add_option_dict)





