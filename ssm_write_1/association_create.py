#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html
if __name__ == '__main__':
    """
	delete-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html
	describe-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association.html
	list-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-associations.html
	update-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association.html
    """

    parameter_display_string = """
    # name : The name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.
You can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.
For SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:

``arn:partition :ssm:region :account-id :document/document-name ``

For example:

arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document

For AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "create-association", "name", add_option_dict)





