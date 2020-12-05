#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-application-revisions.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-name : The name of an AWS CodeDeploy application about which to get revision information.
    # revisions : An array of RevisionLocation objects that specify information to get about the application revisions, including type and location. The maximum number of RevisionLocation objects you can specify is 25.
(structure)

Information about the location of an application revision.
revisionType -> (string)

The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location -> (structure)

Information about the location of a revision stored in Amazon S3.
bucket -> (string)

The name of the Amazon S3 bucket where the application revision is stored.

key -> (string)

The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType -> (string)

The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version -> (string)

A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag -> (string)

The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.


gitHubLocation -> (structure)

Information about the location of application artifacts stored in GitHub.
repository -> (string)

The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId -> (string)

The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.


string -> (structure)

Information about the location of an AWS Lambda deployment revision stored as a RawString.
content -> (string)

The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 -> (string)

The SHA256 hash value of the revision content.


appSpecContent -> (structure)

The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.
content -> (string)

The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 -> (string)

The SHA256 hash value of the revision content.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("deploy", "batch-get-application-revisions", "application-name", "revisions", add_option_dict)
