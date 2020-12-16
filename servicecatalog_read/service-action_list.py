#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-service-actions.html
if __name__ == '__main__':
    """
	create-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-service-action.html
	delete-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-service-action.html
	describe-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-service-action.html
	update-service-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-service-action.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("servicecatalog", "list-service-actions", add_option_dict)