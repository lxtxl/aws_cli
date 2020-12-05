#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-document-analysis.html
if __name__ == '__main__':
    """
	start-document-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-analysis.html
    """

    parameter_display_string = """
    # job-id : A unique identifier for the text-detection job. The JobId is returned from StartDocumentAnalysis . A JobId value is only valid for 7 days.
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

    execute_one_parameter("textract", "get-document-analysis", "job-id", add_option_dict)