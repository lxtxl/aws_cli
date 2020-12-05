#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html
if __name__ == '__main__':
    """
	cancel-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/cancel-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html
	start-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html
    """

    parameter_display_string = """
    # catalog : Required. The catalog related to the request. Fixed value: AWSMarketplace
    # change-set-id : Required. The unique identifier for the StartChangeSet request that you want to describe the details for.
    """

    execute_two_parameter("marketplace-catalog", "describe-change-set", "catalog", "change-set-id", parameter_display_string)