#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/delete-dataset.html
if __name__ == '__main__':
    """
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/describe-dataset.html
	list-datasets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-datasets.html
    """

    parameter_display_string = """
    # identity-pool-id : A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    # identity-id : A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    # dataset-name : A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, â_â (underscore), â-â (dash), and â.â (dot).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-sync", "delete-dataset", "identity-pool-id", "identity-id", "dataset-name", add_option_dict)
