#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/disassociate-discovered-resource.html
if __name__ == '__main__':
    """
	associate-discovered-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/associate-discovered-resource.html
	list-discovered-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-discovered-resources.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : The identifier given to the MigrationTask. Do not store personal data in this field.
    # configuration-id : ConfigurationId of the Application Discovery Service resource to be disassociated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mgh", "disassociate-discovered-resource", "progress-update-stream", "migration-task-name", "configuration-id", add_option_dict)
