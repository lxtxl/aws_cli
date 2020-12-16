#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-domain.html
if __name__ == '__main__':
    """
	create-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-domain.html
	get-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-domains.html
	update-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-domain.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("customer-profiles", "delete-domain", "domain-name", add_option_dict)





