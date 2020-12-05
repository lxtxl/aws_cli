#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-thing.html
if __name__ == '__main__':
    """
	create-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing.html
	delete-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing.html
	describe-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing.html
	list-things : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things.html
	update-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing.html
    """

    parameter_display_string = """
    # template-body : The provisioning template. See Provisioning Devices That Have Device Certificates for more information.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "register-thing", "template-body", add_option_dict)





