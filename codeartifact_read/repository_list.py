#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories.html
if __name__ == '__main__':
    """
	create-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-repository.html
	delete-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository.html
	describe-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-repository.html
	update-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-repository.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("codeartifact", "list-repositories", add_option_dict)