#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-import-job.html
if __name__ == '__main__':
    """
	delete-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-import-job.html
	describe-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html
	list-dataset-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-import-jobs.html
    """

    parameter_display_string = """
    # dataset-import-job-name : The name for the dataset import job. We recommend including the current timestamp in the name, for example, 20190721DatasetImport . This can help you avoid getting a ResourceAlreadyExistsException exception.
    # dataset-arn : The Amazon Resource Name (ARN) of the Amazon Forecast dataset that you want to import data to.
    # data-source : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("forecast", "create-dataset-import-job", "dataset-import-job-name", "dataset-arn", "data-source", add_option_dict)
