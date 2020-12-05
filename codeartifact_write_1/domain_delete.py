#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain.html
if __name__ == '__main__':
    """
	create-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-domain.html
	describe-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-domains.html
    """

    parameter_display_string = """
    # domain : The name of the domain to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codeartifact", "delete-domain", "domain", add_option_dict)





