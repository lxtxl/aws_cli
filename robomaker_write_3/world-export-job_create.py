#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-export-job.html
if __name__ == '__main__':
    """
	cancel-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-world-export-job.html
	describe-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-export-job.html
	list-world-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-export-jobs.html
    """

    parameter_display_string = """
    # worlds : A list of Amazon Resource Names (arns) that correspond to worlds to export.
(string)
    # output-location : 
    # iam-role : The IAM role that the world export process uses to access the Amazon S3 bucket and put the export.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("robomaker", "create-world-export-job", "worlds", "output-location", "iam-role", add_option_dict)
