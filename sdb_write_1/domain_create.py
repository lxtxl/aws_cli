#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/create-domain.html
if __name__ == '__main__':
    """
	delete-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/list-domains.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, â_â, â-â, and â.â.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sdb", "create-domain", "domain-name", add_option_dict)





