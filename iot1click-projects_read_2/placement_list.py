#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/describe-placement.html
if __name__ == '__main__':
    """
	create-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/create-placement.html
	delete-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/delete-placement.html
	list-placements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/list-placements.html
	update-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/update-placement.html
    """

    parameter_display_string = """
    # placement-name : The name of the placement within a project.
    # project-name : The project containing the placement to be described.
    """

    execute_two_parameter("iot1click-projects", "describe-placement", "placement-name", "project-name", parameter_display_string)