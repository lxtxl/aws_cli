#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/test-repository-triggers.html
if __name__ == '__main__':
    """
	get-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository-triggers.html
	put-repository-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-repository-triggers.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository in which to test the triggers.
    # triggers : The list of triggers to test.
(structure)

Information about a trigger for a repository.
name -> (string)

The name of the trigger.

destinationArn -> (string)

The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).

customData -> (string)

Any custom data associated with the trigger to be included in the information sent to the target of the trigger.

branches -> (list)

The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.

Note
Although no content is required in the array, you must include the array itself.

(string)

events -> (list)

The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.

Note
The valid value âallâ cannot be used with any other values.

(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "test-repository-triggers", "repository-name", "triggers", add_option_dict)
