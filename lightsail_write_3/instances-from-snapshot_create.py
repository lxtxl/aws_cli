#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances-from-snapshot.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-names : The names for your new instances.
(string)
    # availability-zone : The Availability Zone where you want to create your instances. Use the following formatting: us-east-2a (case sensitive). You can get a list of Availability Zones by using the get regions operation. Be sure to add the include Availability Zones parameter to your request.
    # bundle-id : The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "create-instances-from-snapshot", "instance-names", "availability-zone", "bundle-id", add_option_dict)
