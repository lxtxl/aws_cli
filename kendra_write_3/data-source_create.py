#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-data-source.html
if __name__ == '__main__':
    """
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-data-source.html
	describe-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html
    """

    parameter_display_string = """
    # name : A unique name for the data source. A data source name canât be changed without deleting and recreating the data source.
    # index-id : The identifier of the index that should be associated with this data source.
    # type : The type of repository that contains the data source.
Possible values:

S3
SHAREPOINT
DATABASE
SALESFORCE
ONEDRIVE
SERVICENOW
CUSTOM
CONFLUENCE
GOOGLEDRIVE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kendra", "create-data-source", "name", "index-id", "type", add_option_dict)
