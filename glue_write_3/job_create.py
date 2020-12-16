#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-job.html
if __name__ == '__main__':
    """
	delete-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html
	get-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-jobs.html
	update-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html
    """

    parameter_display_string = """
    # name : The name you assign to this job definition. It must be unique in your account.
    # role : The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
    # command : Command to execute on Master Node
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "create-job", "name", "role", "command", add_option_dict)
