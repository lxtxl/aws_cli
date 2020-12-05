#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution.html
if __name__ == '__main__':
    """
	create-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution.html
	delete-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html
	get-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html
	list-distributions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions.html
    """

    parameter_display_string = """
    # id : The distributionâs id.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "update-distribution", "id", add_option_dict)




