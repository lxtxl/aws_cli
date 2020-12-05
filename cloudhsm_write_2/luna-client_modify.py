#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/modify-luna-client.html
if __name__ == '__main__':
    """
	create-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-luna-client.html
	delete-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-luna-client.html
	describe-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-luna-client.html
	list-luna-clients : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-luna-clients.html
    """

    parameter_display_string = """
    # client-arn : The ARN of the client.
    # certificate : The new certificate for the client.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsm", "modify-luna-client", "client-arn", "certificate", add_option_dict)
