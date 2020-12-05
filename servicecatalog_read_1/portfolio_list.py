#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio.html
if __name__ == '__main__':
    """
	create-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio.html
	delete-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio.html
	list-portfolios : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolios.html
	update-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio.html
    """

    parameter_display_string = """
    # id : The portfolio identifier.
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

    execute_one_parameter("servicecatalog", "describe-portfolio", "id", add_option_dict)