#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-third-party-job.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The unique system-generated ID of the job.
    # nonce : A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a  GetThirdPartyJobDetails request.
    # client-token : The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codepipeline", "acknowledge-third-party-job", "job-id", "nonce", "client-token", add_option_dict)
