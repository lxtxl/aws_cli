#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association-batch.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # entries : One or more associations.
(structure)

Describes the association of a Systems Manager SSM document and an instance.
Name -> (string)

The name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.
You can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.
For SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:

``arn:aws:ssm:region :account-id :document/document-name ``

For example:

arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document

For AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .

InstanceId -> (string)

The ID of the instance.

Parameters -> (map)

A description of the parameters for a document.
key -> (string)
value -> (list)

(string)


AutomationTargetParameterName -> (string)

Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

DocumentVersion -> (string)

The document version.

Targets -> (list)

The instances targeted by the request.
(structure)

An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
Run Command and Maintenance window targets only : ``Key=resource-groups:Name,Values=*resource-group-name* ``
Maintenance window targets only : ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
Automation targets only : ``Key=ResourceGroup;Values=*resource-group-name* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
Run Command and Maintenance window targets only : Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
Maintenance window targets only : ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
Automation targets only : Key=ResourceGroup,Values=MyResourceGroup
State Manager association targets only : Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For more information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .
Key -> (string)

User-defined criteria for sending commands that target instances that meet the criteria.

Values -> (list)

User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .
(string)



ScheduleExpression -> (string)

A cron expression that specifies a schedule when the association runs.

OutputLocation -> (structure)

An S3 bucket where you want to store the results of this request.
S3Location -> (structure)

An S3 bucket where you want to store the results of this request.
OutputS3Region -> (string)

(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName -> (string)

The name of the S3 bucket.

OutputS3KeyPrefix -> (string)

The S3 bucket subfolder.



AssociationName -> (string)

Specify a descriptive name for the association.

MaxErrors -> (string)

The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there wonât be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency -> (string)

The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity -> (string)

The severity level to assign to the association.

SyncCompliance -> (string)

The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesnât run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.

ApplyOnlyAtCronInterval -> (boolean)

By default, when you create a new associations, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you donât want an association to run immediately after you create it.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "create-association-batch", "entries", add_option_dict)





