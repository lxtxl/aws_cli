#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-service-action-execution-parameters.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # provisioned-product-id : The identifier of the provisioned product.
    # service-action-id : The self-service action identifier.
    """

    execute_two_parameter("servicecatalog", "describe-service-action-execution-parameters", "provisioned-product-id", "service-action-id", parameter_display_string)