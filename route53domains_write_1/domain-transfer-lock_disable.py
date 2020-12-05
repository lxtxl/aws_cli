#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/disable-domain-transfer-lock.html
if __name__ == '__main__':
    """
	enable-domain-transfer-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/enable-domain-transfer-lock.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain that you want to remove the transfer lock for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53domains", "disable-domain-transfer-lock", "domain-name", add_option_dict)





