#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/batch-get-aggregate-resource-config.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # configuration-aggregator-name : The name of the configuration aggregator.
    # resource-identifiers : A list of aggregate ResourceIdentifiers objects.
(structure)

The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.
SourceAccountId -> (string)

The 12-digit account ID of the source account.

SourceRegion -> (string)

The source region where data is aggregated.

ResourceId -> (string)

The ID of the AWS resource.

ResourceType -> (string)

The type of the AWS resource.

ResourceName -> (string)

The name of the AWS resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "batch-get-aggregate-resource-config", "configuration-aggregator-name", "resource-identifiers", add_option_dict)
