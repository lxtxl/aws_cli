#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-domain.html
if __name__ == '__main__':
    """
	deprecate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-domain.html
	describe-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-domains.html
	register-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-domain.html
    """

    parameter_display_string = """
    # name : The name of the domain of the deprecated workflow type.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("swf", "undeprecate-domain", "name", add_option_dict)





