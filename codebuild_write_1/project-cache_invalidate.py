#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/invalidate-project-cache.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # project-name : The name of the AWS CodeBuild build project that the cache is reset for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codebuild", "invalidate-project-cache", "project-name", add_option_dict)





