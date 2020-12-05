#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/describe-text-translation-job.html
if __name__ == '__main__':
    """
	list-text-translation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-text-translation-jobs.html
	start-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/start-text-translation-job.html
	stop-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/stop-text-translation-job.html
    """

    parameter_display_string = """
    # job-id : The identifier that Amazon Translate generated for the job. The  StartTextTranslationJob operation returns this identifier in its response.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("translate", "describe-text-translation-job", "job-id", add_option_dict)