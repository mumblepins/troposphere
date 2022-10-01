# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.fms import validate_json_checker


class NotificationChannel(AWSObject):
    """
    `NotificationChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html>`__
    """

    resource_type = "AWS::FMS::NotificationChannel"

    props: PropsDictType = {
        "SnsRoleName": (str, True),
        "SnsTopicArn": (str, True),
    }


class IEMap(AWSProperty):
    """
    `IEMap <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html>`__
    """

    props: PropsDictType = {
        "ACCOUNT": ([str], False),
        "ORGUNIT": ([str], False),
    }


class NetworkFirewallPolicy(AWSProperty):
    """
    `NetworkFirewallPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`__
    """

    props: PropsDictType = {
        "FirewallDeploymentModel": (str, True),
    }


class ThirdPartyFirewallPolicy(AWSProperty):
    """
    `ThirdPartyFirewallPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`__
    """

    props: PropsDictType = {
        "FirewallDeploymentModel": (str, True),
    }


class PolicyOption(AWSProperty):
    """
    `PolicyOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html>`__
    """

    props: PropsDictType = {
        "NetworkFirewallPolicy": (NetworkFirewallPolicy, False),
        "ThirdPartyFirewallPolicy": (ThirdPartyFirewallPolicy, False),
    }


class SecurityServicePolicyData(AWSProperty):
    """
    `SecurityServicePolicyData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html>`__
    """

    props: PropsDictType = {
        "ManagedServiceData": (str, False),
        "PolicyOption": (PolicyOption, False),
        "Type": (str, True),
    }


class Policy(AWSObject):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html>`__
    """

    resource_type = "AWS::FMS::Policy"

    props: PropsDictType = {
        "DeleteAllPolicyResources": (boolean, False),
        "ExcludeMap": (IEMap, False),
        "ExcludeResourceTags": (boolean, True),
        "IncludeMap": (IEMap, False),
        "PolicyName": (str, True),
        "RemediationEnabled": (boolean, True),
        "ResourceTags": (Tags, False),
        "ResourceType": (str, True),
        "ResourceTypeList": ([str], False),
        "ResourcesCleanUp": (boolean, False),
        "SecurityServicePolicyData": (validate_json_checker, True),
        "Tags": (Tags, False),
    }
