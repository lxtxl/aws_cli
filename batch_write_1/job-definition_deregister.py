#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/deregister-job-definition.html
if __name__ == '__main__':
    """
	describe-job-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-definitions.html
	register-job-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html
    """

    parameter_display_string = """
    # job-definition : The name and revision (name:revision ) or full Amazon Resource Name (ARN) of the job definition to deregister.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("batch", "deregister-job-definition", "job-definition", add_option_dict)





