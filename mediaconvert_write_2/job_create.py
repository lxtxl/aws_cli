#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html
    """

    parameter_display_string = """
    # role : Required. The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html.
    # settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconvert", "create-job", "role", "settings", add_option_dict)
