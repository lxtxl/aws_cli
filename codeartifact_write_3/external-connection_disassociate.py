#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/disassociate-external-connection.html
if __name__ == '__main__':
    """
	associate-external-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/associate-external-connection.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository from which to remove the external repository.
    # repository : The name of the repository from which the external connection will be removed.
    # external-connection : The name of the external connection to be removed from the repository.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeartifact", "disassociate-external-connection", "domain", "repository", "external-connection", add_option_dict)
