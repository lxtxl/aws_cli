#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job-template.html
if __name__ == '__main__':
    """
	create-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job-template.html
	delete-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-job-template.html
	list-job-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-job-templates.html
	update-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-job-template.html
    """

    parameter_display_string = """
    # name : The name of the job template.
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

    execute_one_parameter("mediaconvert", "get-job-template", "name", add_option_dict)