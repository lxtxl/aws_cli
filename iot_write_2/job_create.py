#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job.html
	delete-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job.html
	describe-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-jobs.html
	update-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-job.html
    """

    parameter_display_string = """
    # job-id : A job identifier which must be unique for your AWS account. We recommend using a UUID. Alpha-numeric characters, â-â and â_â are valid for use here.
    # targets : A list of things and thing groups to which the job should be sent.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "create-job", "job-id", "targets", add_option_dict)
