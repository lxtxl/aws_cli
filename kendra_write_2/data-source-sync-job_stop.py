#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/stop-data-source-sync-job.html
if __name__ == '__main__':
    """
	list-data-source-sync-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-source-sync-jobs.html
	start-data-source-sync-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/start-data-source-sync-job.html
    """

    parameter_display_string = """
    # id : The identifier of the data source for which to stop the synchronization jobs.
    # index-id : The identifier of the index that contains the data source.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "stop-data-source-sync-job", "id", "index-id", add_option_dict)
