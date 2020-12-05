#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/copy-snapshot.html
if __name__ == '__main__':
    """
	export-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/export-snapshot.html
    """

    parameter_display_string = """
    # target-snapshot-name : The name of the new manual snapshot to be created as a copy.
    # source-region : The AWS Region where the source manual or automatic snapshot is located.
Possible values:

us-east-1
us-east-2
us-west-1
us-west-2
eu-west-1
eu-west-2
eu-west-3
eu-central-1
ca-central-1
ap-south-1
ap-southeast-1
ap-southeast-2
ap-northeast-1
ap-northeast-2
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "copy-snapshot", "target-snapshot-name", "source-region", add_option_dict)
