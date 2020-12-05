#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-source-sync-jobs.html
if __name__ == '__main__':
    """
	start-data-source-sync-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/start-data-source-sync-job.html
	stop-data-source-sync-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/stop-data-source-sync-job.html
    """

    parameter_display_string = """
    # id : The identifier of the data source.
    # index-id : The identifier of the index that contains the data source.
    """

    execute_two_parameter("kendra", "list-data-source-sync-jobs", "id", "index-id", parameter_display_string)