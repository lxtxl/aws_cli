#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request-approval-rule.html
if __name__ == '__main__':
    """
	delete-pull-request-approval-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-pull-request-approval-rule.html
	evaluate-pull-request-approval-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/evaluate-pull-request-approval-rules.html
	override-pull-request-approval-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/override-pull-request-approval-rules.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request for which you want to create the approval rule.
    # approval-rule-name : The name for the approval rule.
    # approval-rule-content : The content of the approval rule, including the number of approvals needed and the structure of an approval pool defined for approvals, if any. For more information about approval pools, see the AWS CodeCommit User Guide.

Note
When you create the content of the approval rule, you can specify approvers in an approval pool in one of two ways:

CodeCommitApprovers : This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account 123456789012 and Mary_Major , all of the following would be counted as approvals coming from that user:

An IAM user in the account (arn:aws:iam::123456789012 :user/Mary_Major )
A federated user identified in IAM as Mary_Major (arn:aws:sts::123456789012 :federated-user/Mary_Major )



This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of Mary_Major (arn:aws:sts::123456789012 :assumed-role/CodeCommitReview/Mary_Major ) unless you include a wildcard (*Mary_Major).

Fully qualified ARN : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.

For more information about IAM ARNs, wildcards, and formats, see IAM Identifiers in the IAM User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codecommit", "create-pull-request-approval-rule", "pull-request-id", "approval-rule-name", "approval-rule-content", add_option_dict)
