#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/register-container-image.html
if __name__ == '__main__':
    """
	delete-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-image.html
	get-container-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-images.html
	push-container-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/push-container-image.html
    """

    parameter_display_string = """
    # service-name : The name of the container service for which to register a container image.
    # label : The label for the container image when itâs registered to the container service.
Use a descriptive label that you can use to track the different versions of your registered container images.
Use the GetContainerImages action to return the container images registered to a Lightsail container service. The label is the <imagelabel> portion of the following image name example:

:container-service-1.<imagelabel>.1

If the name of your container service is mycontainerservice , and the label that you specify is mystaticwebsite , then the name of the registered container image will be :mycontainerservice.mystaticwebsite.1 .
The number at the end of these image name examples represents the version of the registered container image. If you push and register another container image to the same Lightsail container service, with the same label, then the version number for the new registered container image will be 2 . If you push and register another container image, the version number will be 3 , and so on.
    # digest : The digest of the container image to be registered.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "register-container-image", "service-name", "label", "digest", add_option_dict)
