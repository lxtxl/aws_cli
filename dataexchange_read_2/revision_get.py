#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-revision.html
if __name__ == '__main__':
    """
	create-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-revision.html
	delete-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-revision.html
	update-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-revision.html
    """

    parameter_display_string = """
    # data-set-id : The unique identifier for a data set.
    # revision-id : The unique identifier for a revision.
    """

    execute_two_parameter("dataexchange", "get-revision", "data-set-id", "revision-id", parameter_display_string)