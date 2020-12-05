#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-thing-principal.html
if __name__ == '__main__':
    """
	attach-thing-principal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html
	list-thing-principals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principals.html
    """

    parameter_display_string = """
    # thing-name : The name of the thing.
    # principal : If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "detach-thing-principal", "thing-name", "principal", add_option_dict)
