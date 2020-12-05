#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-custom-data-identifier.html
if __name__ == '__main__':
    """
	create-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-custom-data-identifier.html
	delete-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-custom-data-identifier.html
	list-custom-data-identifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-custom-data-identifiers.html
	test-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/test-custom-data-identifier.html
    """

    parameter_display_string = """
    # id : The unique identifier for the Amazon Macie resource or account that the request applies to.
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

    execute_one_parameter("macie2", "get-custom-data-identifier", "id", add_option_dict)