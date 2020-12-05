#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-packages.html
if __name__ == '__main__':
    """
	associate-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/associate-package.html
	create-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-package.html
	delete-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-package.html
	dissociate-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/dissociate-package.html
	update-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-package.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("es", "describe-packages", add_option_dict)