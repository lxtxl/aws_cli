#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-classification-job.html
if __name__ == '__main__':
    """
	describe-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-classification-job.html
	list-classification-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html
	update-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-classification-job.html
    """

    parameter_display_string = """
    # job-type : The schedule for running the job. Valid values are:

ONE_TIME - Run the job only once. If you specify this value, donât specify a value for the scheduleFrequency property.
SCHEDULED - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the scheduleFrequency property to define the recurrence pattern for the job.

Possible values:

ONE_TIME
SCHEDULED
    # name : A custom name for the job. The name can contain as many as 500 characters.
    # s3-job-definition : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("macie2", "create-classification-job", "job-type", "name", "s3-job-definition", add_option_dict)
