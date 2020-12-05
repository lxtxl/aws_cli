#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-trust.html
if __name__ == '__main__':
    """
	create-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-trust.html
	delete-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-trust.html
	describe-trusts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-trusts.html
	verify-trust : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/verify-trust.html
    """

    parameter_display_string = """
    # trust-id : Identifier of the trust relationship.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ds", "update-trust", "trust-id", add_option_dict)





