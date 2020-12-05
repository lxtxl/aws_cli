#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html
if __name__ == '__main__':
    """
	detach-thing-principal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-thing-principal.html
	list-thing-principals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principals.html
    """

    parameter_display_string = """
    # thing-name : The name of the thing.
    # principal : The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "attach-thing-principal", "thing-name", "principal", add_option_dict)
