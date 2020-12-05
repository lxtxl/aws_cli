#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-invalidation.html
if __name__ == '__main__':
    """
	create-invalidation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-invalidation.html
	list-invalidations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-invalidations.html
    """

    parameter_display_string = """
    # distribution-id : The distributionâs ID.
    # id : The identifier for the invalidation request, for example, IDFDVBD632BHDS5 .
    """

    execute_two_parameter("cloudfront", "get-invalidation", "distribution-id", "id", parameter_display_string)