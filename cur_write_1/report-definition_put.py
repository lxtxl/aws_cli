#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html
if __name__ == '__main__':
    """
	delete-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/delete-report-definition.html
	describe-report-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/describe-report-definitions.html
	modify-report-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/modify-report-definition.html
    """

    parameter_display_string = """
    # report-definition : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cur", "put-report-definition", "report-definition", add_option_dict)





