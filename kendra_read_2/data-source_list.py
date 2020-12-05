#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-data-source.html
if __name__ == '__main__':
    """
	create-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-data-source.html
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html
    """

    parameter_display_string = """
    # id : The unique identifier of the data source to describe.
    # index-id : The identifier of the index that contains the data source.
    """

    execute_two_parameter("kendra", "describe-data-source", "id", "index-id", parameter_display_string)