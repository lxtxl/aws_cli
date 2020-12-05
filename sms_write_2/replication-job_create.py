#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/create-replication-job.html
if __name__ == '__main__':
    """
	delete-replication-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/delete-replication-job.html
	get-replication-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-replication-jobs.html
	update-replication-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/update-replication-job.html
    """

    parameter_display_string = """
    # server-id : The ID of the server.
    # seed-replication-time : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sms", "create-replication-job", "server-id", "seed-replication-time", add_option_dict)
