#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/describe-application-snapshot.html
if __name__ == '__main__':
    """
	create-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/create-application-snapshot.html
	delete-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/delete-application-snapshot.html
	list-application-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/list-application-snapshots.html
    """

    parameter_display_string = """
    # application-name : The name of an existing application.
    # snapshot-name : The identifier of an application snapshot. You can retrieve this value using .
    """

    execute_two_parameter("kinesisanalyticsv2", "describe-application-snapshot", "application-name", "snapshot-name", parameter_display_string)