#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-import-task.html
if __name__ == '__main__':
    """
	describe-import-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-import-tasks.html
    """

    parameter_display_string = """
    # name : A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.
    # import-url : The URL for your import file that youâve uploaded to Amazon S3.

Note
If youâre using the AWS CLI, this URL is structured as follows: s3://BucketName/ImportFileName.CSV
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("discovery", "start-import-task", "name", "import-url", add_option_dict)
