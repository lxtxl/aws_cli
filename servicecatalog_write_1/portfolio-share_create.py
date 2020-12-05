#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio-share.html
if __name__ == '__main__':
    """
	accept-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/accept-portfolio-share.html
	delete-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio-share.html
	reject-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/reject-portfolio-share.html
    """

    parameter_display_string = """
    # portfolio-id : The portfolio identifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "create-portfolio-share", "portfolio-id", add_option_dict)





