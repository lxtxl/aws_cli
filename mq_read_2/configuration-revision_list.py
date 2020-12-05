#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-configuration-revision.html
if __name__ == '__main__':
    """
	list-configuration-revisions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-configuration-revisions.html
    """

    parameter_display_string = """
    # configuration-id : The unique ID that Amazon MQ generates for the configuration.
    # configuration-revision : The revision of the configuration.
    """

    execute_two_parameter("mq", "describe-configuration-revision", "configuration-id", "configuration-revision", parameter_display_string)