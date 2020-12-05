#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html
if __name__ == '__main__':
    """
	delete-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-listener.html
	describe-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listeners.html
	modify-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html
    """

    parameter_display_string = """
    # load-balancer-arn : The Amazon Resource Name (ARN) of the load balancer.
    # default-actions : The actions for the default rule.
(structure)

Information about an action.
Each rule must include exactly one of the following types of actions: forward , fixed-response , or redirect , and it must be the last action to be performed.
Type -> (string)

The type of action.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group. Specify only when Type is forward and you want to route to a single target group. To route to one or more target groups, use ForwardConfig instead.

AuthenticateOidcConfig -> (structure)

[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when Type is authenticate-oidc .
Issuer -> (string)

The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint -> (string)

The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId -> (string)

The OAuth 2.0 client identifier.

ClientSecret -> (string)

The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set UseExistingClientSecret to true.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
key -> (string)
value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.


UseExistingClientSecret -> (boolean)

Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.


AuthenticateCognitoConfig -> (structure)

[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when Type is authenticate-cognito .
UserPoolArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId -> (string)

The ID of the Amazon Cognito user pool client.

UserPoolDomain -> (string)

The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is openid .
To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
key -> (string)
value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

deny- Return an HTTP 401 Unauthorized error.
allow- Allow the request to be forwarded to the target.
authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.



Order -> (integer)

The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.

RedirectConfig -> (structure)

[Application Load Balancer] Information for creating a redirect action. Specify only when Type is redirect .
Protocol -> (string)

The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

Port -> (string)

The port. You can specify a value from 1 to 65535 or #{port}.

Host -> (string)

The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path -> (string)

The absolute path, starting with the leading â/â. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query -> (string)

The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading â?â, as it is automatically added. You can specify any of the reserved keywords.

StatusCode -> (string)

The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).


FixedResponseConfig -> (structure)

[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when Type is fixed-response .
MessageBody -> (string)

The message.

StatusCode -> (string)

The HTTP response code (2XX, 4XX, or 5XX).

ContentType -> (string)

The content type.
Valid Values: text/plain | text/css | text/html | application/javascript | application/json


ForwardConfig -> (structure)

Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when Type is forward . If you specify both ForwardConfig and TargetGroupArn , you can specify only one target group using ForwardConfig and it must be the same target group specified in TargetGroupArn .
TargetGroups -> (list)

One or more target groups. For Network Load Balancers, you can specify a single target group.
(structure)

Information about how traffic will be distributed between multiple target groups in a forward rule.
TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group.

Weight -> (integer)

The weight. The range is 0 to 999.



TargetGroupStickinessConfig -> (structure)

The target group stickiness for the rule.
Enabled -> (boolean)

Indicates whether target group stickiness is enabled.

DurationSeconds -> (integer)

The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "create-listener", "load-balancer-arn", "default-actions", add_option_dict)
