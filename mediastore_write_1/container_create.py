#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/create-container.html
if __name__ == '__main__':
    """
	delete-container : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container.html
	describe-container : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-container.html
	list-containers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-containers.html
    """

    parameter_display_string = """
    # container-name : The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named movies in every region, as long as you donât have an existing container with that name.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediastore", "create-container", "container-name", add_option_dict)





