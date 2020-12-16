#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-media-application.html
if __name__ == '__main__':
    """
	create-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-media-application.html
	delete-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-media-application.html
	get-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-media-application.html
	list-sip-media-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-media-applications.html
    """

    parameter_display_string = """
    # sip-media-application-id : The SIP media application ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "update-sip-media-application", "sip-media-application-id", add_option_dict)





