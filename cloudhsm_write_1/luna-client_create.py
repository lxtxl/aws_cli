#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-luna-client.html
if __name__ == '__main__':
    """
	delete-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-luna-client.html
	describe-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-luna-client.html
	list-luna-clients : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-luna-clients.html
	modify-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/modify-luna-client.html
    """

    parameter_display_string = """
    # certificate : The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudhsm", "create-luna-client", "certificate", add_option_dict)





