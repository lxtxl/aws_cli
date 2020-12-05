#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/batch-associate-service-action-with-provisioning-artifact.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-action-associations : One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
(structure)

A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.
ServiceActionId -> (string)

The self-service action identifier. For example, act-fs7abcd89wxyz .

ProductId -> (string)

The product identifier. For example, prod-abcdzk7xy33qa .

ProvisioningArtifactId -> (string)

The identifier of the provisioning artifact. For example, pa-4abcdjnxjj6ne .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "batch-associate-service-action-with-provisioning-artifact", "service-action-associations", add_option_dict)





