#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-job.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The unique system-generated ID of the job for which you want to confirm receipt.
    # nonce : A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the  PollForJobs request that returned this job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codepipeline", "acknowledge-job", "job-id", "nonce", add_option_dict)
