#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-data-sets.html
if __name__ == '__main__':
    """
	create-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-data-set.html
	delete-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-data-set.html
	describe-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-data-set.html
	update-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("quicksight", "list-data-sets", "aws-account-id", add_option_dict)