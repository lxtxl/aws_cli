#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-service-actions-for-provisioning-artifact.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # product-id : The product identifier. For example, prod-abcdzk7xy33qa .
    # provisioning-artifact-id : The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .
    """

    execute_two_parameter("servicecatalog", "list-service-actions-for-provisioning-artifact", "product-id", "provisioning-artifact-id", parameter_display_string)