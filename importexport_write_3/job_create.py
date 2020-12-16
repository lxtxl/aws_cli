#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/create-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/cancel-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/list-jobs.html
	update-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/update-job.html
    """

    parameter_display_string = """
    # job-type : Possible values:

Import
Export
    # manifest : The UTF-8 encoded text of the manifest file.
    # validate-only | --no-validate-only : Validate the manifest and parameter values in the request but do not actually create a job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("importexport", "create-job", "job-type", "manifest", "validate-only | --no-validate-only", add_option_dict)
