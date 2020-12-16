#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-application.html
if __name__ == '__main__':
    """
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/delete-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/list-applications.html
	unshare-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/unshare-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/update-application.html
    """

    parameter_display_string = """
    # author : The name of the author publishing the app.
Minimum length=1. Maximum length=127.
Pattern â^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$â;
    # description : The description of the application.
Minimum length=1. Maximum length=256
    # name : The name of the application that you want to publish.
Minimum length=1. Maximum length=140
Pattern: â[a-zA-Z0-9-]+â;
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("serverlessrepo", "create-application", "author", "description", "name", add_option_dict)
