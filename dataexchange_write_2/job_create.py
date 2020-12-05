#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/cancel-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-jobs.html
	start-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/start-job.html
    """

    parameter_display_string = """
    # details : 
    # type : The type of job to be created.
Possible values:

IMPORT_ASSETS_FROM_S3
IMPORT_ASSET_FROM_SIGNED_URL
EXPORT_ASSETS_TO_S3
EXPORT_ASSET_TO_SIGNED_URL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dataexchange", "create-job", "details", "type", add_option_dict)
