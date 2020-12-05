#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-image.html
if __name__ == '__main__':
    """
	get-container-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-images.html
	push-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/push-container-image.html
	register-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/register-container-image.html
    """

    parameter_display_string = """
    # service-name : The name of the container service for which to delete a registered container image.
    # image : The name of the container image to delete from the container service.
Use the GetContainerImages action to get the name of the container images that are registered to a container service.

Note
Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (: ). For example, :container-service-1.mystaticwebsite.1 . Container images sourced from a public registry like Docker Hub donât start with a colon. For example, nginx:latest or nginx .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "delete-container-image", "service-name", "image", add_option_dict)
