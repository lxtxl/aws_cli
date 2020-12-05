#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-entity.html
if __name__ == '__main__':
    """
	list-entities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-entities.html
    """

    parameter_display_string = """
    # catalog : Required. The catalog related to the request. Fixed value: AWSMarketplace
    # entity-id : Required. The unique ID of the entity to describe.
    """

    execute_two_parameter("marketplace-catalog", "describe-entity", "catalog", "entity-id", parameter_display_string)