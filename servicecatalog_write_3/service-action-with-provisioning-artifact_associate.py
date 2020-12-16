#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-service-action-with-provisioning-artifact.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # product-id : The product identifier. For example, prod-abcdzk7xy33qa .
    # provisioning-artifact-id : The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .
    # service-action-id : The self-service action identifier. For example, act-fs7abcd89wxyz .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicecatalog", "associate-service-action-with-provisioning-artifact", "product-id", "provisioning-artifact-id", "service-action-id", add_option_dict)
