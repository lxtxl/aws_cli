#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/list-datasets.html
if __name__ == '__main__':
    """
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/delete-dataset.html
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/describe-dataset.html
    """

    parameter_display_string = """
    # identity-pool-id : A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    # identity-id : A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    """

    execute_two_parameter("cognito-sync", "list-datasets", "identity-pool-id", "identity-id", parameter_display_string)