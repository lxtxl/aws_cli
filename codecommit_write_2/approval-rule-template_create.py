#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-approval-rule-template.html
if __name__ == '__main__':
    """
	delete-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-approval-rule-template.html
	get-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-approval-rule-template.html
	list-approval-rule-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-approval-rule-templates.html
    """

    parameter_display_string = """
    # approval-rule-template-name : The name of the approval rule template. Provide descriptive names, because this name is applied to the approval rules created automatically in associated repositories.
    # approval-rule-template-content : The content of the approval rule that is created on pull requests in associated repositories. If you specify one or more destination references (branches), approval rules are created in an associated repository only if their destination references (branches) match those specified in the template.

Note
When you create the content of the approval rule template, you can specify approvers in an approval pool in one of two ways:

CodeCommitApprovers : This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account 123456789012 and Mary_Major , all of the following are counted as approvals coming from that user:

An IAM user in the account (arn:aws:iam::123456789012 :user/Mary_Major )
A federated user identified in IAM as Mary_Major (arn:aws:sts::123456789012 :federated-user/Mary_Major )



This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of Mary_Major (arn:aws:sts::123456789012 :assumed-role/CodeCommitReview/Mary_Major ) unless you include a wildcard (*Mary_Major).

Fully qualified ARN : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.

For more information about IAM ARNs, wildcards, and formats, see IAM Identifiers in the IAM User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "create-approval-rule-template", "approval-rule-template-name", "approval-rule-template-content", add_option_dict)
