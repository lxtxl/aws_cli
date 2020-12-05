#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-third-party-job-success-result.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The ID of the job that successfully completed. This is the same ID returned from PollForThirdPartyJobs .
    # client-token : The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codepipeline", "put-third-party-job-success-result", "job-id", "client-token", add_option_dict)
