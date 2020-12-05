#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-data.html
if __name__ == '__main__':
    """
	get-metric-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-data.html
    """

    parameter_display_string = """
    # namespace : The namespace for the metric data.
To avoid conflicts with AWS service namespaces, you should not specify a namespace that begins with AWS/
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudwatch", "put-metric-data", "namespace", add_option_dict)





