#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-comment-reaction.html
if __name__ == '__main__':
    """
	get-comment-reactions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment-reactions.html
    """

    parameter_display_string = """
    # comment-id : The ID of the comment to which you want to add or update a reaction.
    # reaction-value : The emoji reaction you want to add or update. To remove a reaction, provide a value of blank or null. You can also provide the value of none. For information about emoji reaction values supported in AWS CodeCommit, see the AWS CodeCommit User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "put-comment-reaction", "comment-id", "reaction-value", add_option_dict)
