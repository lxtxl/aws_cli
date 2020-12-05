#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio.html
if __name__ == '__main__':
    """
	create-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio.html
	describe-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio.html
	list-portfolios : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolios.html
	update-portfolio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio.html
    """

    parameter_display_string = """
    # id : The portfolio identifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "delete-portfolio", "id", add_option_dict)





