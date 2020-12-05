#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-name : The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot . ElastiCache resources are cluster and snapshot .
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    # tags : A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
(structure)

A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
Key -> (string)

The key for the tag. May not be null.

Value -> (string)

The tagâs value. May be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "add-tags-to-resource", "resource-name", "tags", add_option_dict)
