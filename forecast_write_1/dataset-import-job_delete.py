#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-import-job.html
if __name__ == '__main__':
    """
	create-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-import-job.html
	describe-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html
	list-dataset-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-import-jobs.html
    """

    parameter_display_string = """
    # dataset-import-job-arn : The Amazon Resource Name (ARN) of the dataset import job to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("forecast", "delete-dataset-import-job", "dataset-import-job-arn", add_option_dict)





