#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-third-party-job-failure-result.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The ID of the job that failed. This is the same ID returned from PollForThirdPartyJobs .
    # client-token : The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
    # failure-details : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codepipeline", "put-third-party-job-failure-result", "job-id", "client-token", "failure-details", add_option_dict)
