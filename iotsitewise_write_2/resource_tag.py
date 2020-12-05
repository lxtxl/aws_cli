#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the resource to tag.
    # tags : A list of key-value pairs that contain metadata for the resource. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsitewise", "tag-resource", "resource-arn", "tags", add_option_dict)
