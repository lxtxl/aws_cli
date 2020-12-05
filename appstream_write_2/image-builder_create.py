#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-image-builder.html
if __name__ == '__main__':
    """
	delete-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-builder.html
	describe-image-builders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-builders.html
	start-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html
	stop-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-image-builder.html
    """

    parameter_display_string = """
    # name : A unique name for the image builder.
    # instance-type : The instance type to use when launching the image builder. The following instance types are available:

stream.standard.medium
stream.standard.large
stream.compute.large
stream.compute.xlarge
stream.compute.2xlarge
stream.compute.4xlarge
stream.compute.8xlarge
stream.memory.large
stream.memory.xlarge
stream.memory.2xlarge
stream.memory.4xlarge
stream.memory.8xlarge
stream.memory.z1d.large
stream.memory.z1d.xlarge
stream.memory.z1d.2xlarge
stream.memory.z1d.3xlarge
stream.memory.z1d.6xlarge
stream.memory.z1d.12xlarge
stream.graphics-design.large
stream.graphics-design.xlarge
stream.graphics-design.2xlarge
stream.graphics-design.4xlarge
stream.graphics-desktop.2xlarge
stream.graphics.g4dn.xlarge
stream.graphics.g4dn.2xlarge
stream.graphics.g4dn.4xlarge
stream.graphics.g4dn.8xlarge
stream.graphics.g4dn.12xlarge
stream.graphics.g4dn.16xlarge
stream.graphics-pro.4xlarge
stream.graphics-pro.8xlarge
stream.graphics-pro.16xlarge
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appstream", "create-image-builder", "name", "instance-type", add_option_dict)
