#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-crawler.html
if __name__ == '__main__':
    """
	delete-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-crawler.html
	get-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawler.html
	get-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawlers.html
	list-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-crawlers.html
	start-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-crawler.html
	stop-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-crawler.html
	update-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-crawler.html
    """

    parameter_display_string = """
    # name : Name of the new crawler.
    # role : The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access customer resources.
    # targets : The targets to update or add to the rule.
(structure)

Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see  PutTargets .
If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a RoleArn with proper permissions in the Target structure. For more information, see Sending and Receiving Events Between AWS Accounts in the Amazon EventBridge User Guide .
Id -> (string)

The ID of the target.

Arn -> (string)

The Amazon Resource Name (ARN) of the target.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.

Input -> (string)

Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see The JavaScript Object Notation (JSON) Data Interchange Format .

InputPath -> (string)

The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see JSONPath .

InputTransformer -> (structure)

Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.
InputPathsMap -> (map)

Map of JSON paths to be extracted from the event. You can then insert these in the template in InputTemplate to produce the output you want to be sent to the target.

InputPathsMap is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation.

The keys cannot start with âAWS.â
key -> (string)
value -> (string)

InputTemplate -> (string)

Input template where you specify placeholders that will be filled with the values of the keys from InputPathsMap to customize the data sent to the target. Enclose each InputPathsMaps value in brackets: <value > The InputTemplate must be valid JSON.
If InputTemplate is a JSON object (surrounded by curly braces), the following restrictions apply:

The placeholder cannot be used as an object key.
Object values cannot include quote marks.

The following example shows the syntax for using InputPathsMap and InputTemplate .

"InputTransformer":
{
"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},
"InputTemplate": "<instance> is in state <status>"
}

To have the InputTemplate include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:

"InputTransformer":
{
"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},
"InputTemplate": "<instance> is in state \"<status>\""
}



KinesisParameters -> (structure)

The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the eventId as the partition key.
PartitionKeyPath -> (string)

The JSON path to be extracted from the event and used as the partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide .


RunCommandParameters -> (structure)

Parameters used when you are using the rule to invoke Amazon EC2 Run Command.
RunCommandTargets -> (list)

Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.
(structure)

Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each RunCommandTarget block can include only one key, but this key may specify multiple values.
Key -> (string)

Can be either tag: tag-key or InstanceIds .

Values -> (list)

If Key is tag: tag-key , Values is a list of tag values. If Key is InstanceIds , Values is a list of Amazon EC2 instance IDs.
(string)




EcsParameters -> (structure)

Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see Task Definitions in the Amazon EC2 Container Service Developer Guide .
TaskDefinitionArn -> (string)

The ARN of the task definition to use if the event target is an Amazon ECS task.

TaskCount -> (integer)

The number of tasks to create based on TaskDefinition . The default is 1.

LaunchType -> (string)

Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The FARGATE value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see AWS Fargate on Amazon ECS in the Amazon Elastic Container Service Developer Guide .

NetworkConfiguration -> (structure)

Use this structure if the ECS task uses the awsvpc network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if LaunchType is FARGATE because the awsvpc mode is required for Fargate tasks.
If you specify NetworkConfiguration when the target ECS task does not use the awsvpc network mode, the task fails.
awsvpcConfiguration -> (structure)

Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.
Subnets -> (list)

Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
(string)

SecurityGroups -> (list)

Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
(string)

AssignPublicIp -> (string)

Specifies whether the taskâs elastic network interface receives a public IP address. You can specify ENABLED only when LaunchType in EcsParameters is set to FARGATE .



PlatformVersion -> (string)

Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0 .
This structure is used only if LaunchType is FARGATE . For more information about valid platform versions, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .

Group -> (string)

Specifies an ECS task group for the task. The maximum length is 255 characters.


BatchParameters -> (structure)

If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see Jobs in the AWS Batch User Guide .
JobDefinition -> (string)

The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.

JobName -> (string)

The name to use for this execution of the job, if the target is an AWS Batch job.

ArrayProperties -> (structure)

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
Size -> (integer)

The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.


RetryStrategy -> (structure)

The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1â10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.
Attempts -> (integer)

The number of times to attempt to retry, if the job fails. Valid values are 1â10.



SqsParameters -> (structure)

Contains the message group ID to use when the target is a FIFO queue.
If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.
MessageGroupId -> (string)

The FIFO message group ID to use as the target.


HttpParameters -> (structure)

Contains the HTTP parameters to use when the target is a API Gateway REST endpoint.
If you specify an API Gateway REST API as a target, you can use this parameter to specify headers, path parameter, query string keys/values as part of your target invoking request.
PathParameterValues -> (list)

The path parameter values to be used to populate API Gateway REST API path wildcards (â*â).
(string)

HeaderParameters -> (map)

The headers that need to be sent as part of request invoking the API Gateway REST API.
key -> (string)
value -> (string)

QueryStringParameters -> (map)

The query string keys/values that need to be sent as part of request invoking the API Gateway REST API.
key -> (string)
value -> (string)


RedshiftDataParameters -> (structure)

Contains the Redshift Data API parameters to use when the target is a Redshift cluster.
If you specify a Redshift Cluster as a Target, you can use this to specify parameters to invoke the Redshift Data API ExecuteStatement based on EventBridge events.
SecretManagerArn -> (string)

The name or ARN of the secret that enables access to the database. Required when authenticating using AWS Secrets Manager.

Database -> (string)

The name of the database. Required when authenticating using temporary credentials.

DbUser -> (string)

The database user name. Required when authenticating using temporary credentials.

Sql -> (string)

The SQL statement text to run.

StatementName -> (string)

The name of the SQL statement. You can name the SQL statement when you create it to identify the query.

WithEvent -> (boolean)

Indicates whether to send an event back to EventBridge after the SQL statement runs.


DeadLetterConfig -> (structure)

The DeadLetterConfig that defines the target queue to send dead-letter queue events to.
Arn -> (string)

The ARN of the SQS queue specified as the target for the dead-letter queue.


RetryPolicy -> (structure)

The RetryPolicy object that contains the retry policy configuration to use for the dead-letter queue.
MaximumRetryAttempts -> (integer)

The maximum number of retry attempts to make before the request fails. Retry attempts continue until either the maximum number of attempts is made or until the duration of the MaximumEventAgeInSeconds is met.

MaximumEventAgeInSeconds -> (integer)

The maximum amount of time, in seconds, to continue to make retry attempts.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "create-crawler", "name", "role", "targets", add_option_dict)
