#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-configuration.html
if __name__ == '__main__':
    """
	create-hsm-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-configuration.html
	describe-hsm-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-configurations.html
    """

    parameter_display_string = """
    # hsm-configuration-identifier : The identifier of the Amazon Redshift HSM configuration to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-hsm-configuration", "hsm-configuration-identifier", add_option_dict)





