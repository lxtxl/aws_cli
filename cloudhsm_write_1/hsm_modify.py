#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/modify-hsm.html
if __name__ == '__main__':
    """
	create-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-hsm.html
	delete-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-hsm.html
	describe-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-hsm.html
	list-hsms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-hsms.html
    """

    parameter_display_string = """
    # hsm-arn : The ARN of the HSM to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudhsm", "modify-hsm", "hsm-arn", add_option_dict)





