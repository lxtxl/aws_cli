#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-import-job.html
if __name__ == '__main__':
    """
	get-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-import-job.html
	list-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-import-jobs.html
    """

    parameter_display_string = """
    # import-destination : 
    # import-data-source : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "create-import-job", "import-destination", "import-data-source", add_option_dict)
