#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/disassociate-repository.html
if __name__ == '__main__':
    """
	associate-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/associate-repository.html
    """

    parameter_display_string = """
    # association-arn : The Amazon Resource Name (ARN) of the ` RepositoryAssociation https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html`__ object. You can retrieve this ARN by calling ListRepositories .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codeguru-reviewer", "disassociate-repository", "association-arn", add_option_dict)





