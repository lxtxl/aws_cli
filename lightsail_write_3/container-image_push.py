#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/push-container-image.html
if __name__ == '__main__':
    """
	delete-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-image.html
	get-container-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-images.html
	register-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/register-container-image.html
    """

    parameter_display_string = """
    # service-name : The name of the container service to which the container image will be pushed.
    # image : The name of the container image to push from the local machine to the container service.
    # label : The label to apply to the registered container image on the container service.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "push-container-image", "service-name", "image", "label", add_option_dict)
