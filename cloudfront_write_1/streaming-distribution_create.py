#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-streaming-distribution.html
if __name__ == '__main__':
    """
	delete-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-streaming-distribution.html
	get-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-streaming-distribution.html
	list-streaming-distributions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-streaming-distributions.html
	update-streaming-distribution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-streaming-distribution.html
    """

    parameter_display_string = """
    # streaming-distribution-config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "create-streaming-distribution", "streaming-distribution-config", add_option_dict)





