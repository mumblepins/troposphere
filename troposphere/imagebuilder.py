# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.imagebuilder import (
    component_platforms,
    ebsinstanceblockdevicespecification_volume_type,
    imagepipeline_status,
    schedule_pipelineexecutionstartcondition,
)


class Component(AWSObject):
    """
    `Component <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html>`__
    """

    resource_type = "AWS::ImageBuilder::Component"

    props: PropsDictType = {
        "ChangeDescription": (str, False),
        "Data": (str, False),
        "Description": (str, False),
        "KmsKeyId": (str, False),
        "Name": (str, True),
        "Platform": (component_platforms, True),
        "SupportedOsVersions": ([str], False),
        "Tags": (dict, False),
        "Uri": (str, False),
        "Version": (str, True),
    }


class ComponentParameter(AWSProperty):
    """
    `ComponentParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": ([str], True),
    }


class ContainerComponentConfiguration(AWSProperty):
    """
    `ContainerComponentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html>`__
    """

    props: PropsDictType = {
        "ComponentArn": (str, False),
        "Parameters": ([ComponentParameter], False),
    }


class EbsInstanceBlockDeviceSpecification(AWSProperty):
    """
    `EbsInstanceBlockDeviceSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html>`__
    """

    props: PropsDictType = {
        "DeleteOnTermination": (boolean, False),
        "Encrypted": (boolean, False),
        "Iops": (integer, False),
        "KmsKeyId": (str, False),
        "SnapshotId": (str, False),
        "Throughput": (integer, False),
        "VolumeSize": (integer, False),
        "VolumeType": (ebsinstanceblockdevicespecification_volume_type, False),
    }


class InstanceBlockDeviceMapping(AWSProperty):
    """
    `InstanceBlockDeviceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html>`__
    """

    props: PropsDictType = {
        "DeviceName": (str, False),
        "Ebs": (EbsInstanceBlockDeviceSpecification, False),
        "NoDevice": (str, False),
        "VirtualName": (str, False),
    }


class InstanceConfiguration(AWSProperty):
    """
    `InstanceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html>`__
    """

    props: PropsDictType = {
        "BlockDeviceMappings": ([InstanceBlockDeviceMapping], False),
        "Image": (str, False),
    }


class TargetContainerRepository(AWSProperty):
    """
    `TargetContainerRepository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html>`__
    """

    props: PropsDictType = {
        "RepositoryName": (str, False),
        "Service": (str, False),
    }


class ContainerRecipe(AWSObject):
    """
    `ContainerRecipe <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html>`__
    """

    resource_type = "AWS::ImageBuilder::ContainerRecipe"

    props: PropsDictType = {
        "Components": ([ContainerComponentConfiguration], True),
        "ContainerType": (str, True),
        "Description": (str, False),
        "DockerfileTemplateData": (str, False),
        "DockerfileTemplateUri": (str, False),
        "ImageOsVersionOverride": (str, False),
        "InstanceConfiguration": (InstanceConfiguration, False),
        "KmsKeyId": (str, False),
        "Name": (str, True),
        "ParentImage": (str, True),
        "PlatformOverride": (str, False),
        "Tags": (dict, False),
        "TargetRepository": (TargetContainerRepository, True),
        "Version": (str, True),
        "WorkingDirectory": (str, False),
    }


class LaunchPermissionConfiguration(AWSProperty):
    """
    `LaunchPermissionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html>`__
    """

    props: PropsDictType = {
        "OrganizationArns": ([str], False),
        "OrganizationalUnitArns": ([str], False),
        "UserGroups": ([str], False),
        "UserIds": ([str], False),
    }


class AmiDistributionConfiguration(AWSProperty):
    """
    `AmiDistributionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html>`__
    """

    props: PropsDictType = {
        "AmiTags": (dict, False),
        "Description": (str, False),
        "KmsKeyId": (str, False),
        "LaunchPermissionConfiguration": (LaunchPermissionConfiguration, False),
        "Name": (str, False),
        "TargetAccountIds": ([str], False),
    }


class ContainerDistributionConfiguration(AWSProperty):
    """
    `ContainerDistributionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html>`__
    """

    props: PropsDictType = {
        "ContainerTags": ([str], False),
        "Description": (str, False),
        "TargetRepository": (TargetContainerRepository, False),
    }


class FastLaunchLaunchTemplateSpecification(AWSProperty):
    """
    `FastLaunchLaunchTemplateSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html>`__
    """

    props: PropsDictType = {
        "LaunchTemplateId": (str, False),
        "LaunchTemplateName": (str, False),
        "LaunchTemplateVersion": (str, False),
    }


class FastLaunchSnapshotConfiguration(AWSProperty):
    """
    `FastLaunchSnapshotConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html>`__
    """

    props: PropsDictType = {
        "TargetResourceCount": (integer, False),
    }


class FastLaunchConfiguration(AWSProperty):
    """
    `FastLaunchConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, False),
        "Enabled": (boolean, False),
        "LaunchTemplate": (FastLaunchLaunchTemplateSpecification, False),
        "MaxParallelLaunches": (integer, False),
        "SnapshotConfiguration": (FastLaunchSnapshotConfiguration, False),
    }


class LaunchTemplateConfiguration(AWSProperty):
    """
    `LaunchTemplateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, False),
        "LaunchTemplateId": (str, False),
        "SetDefaultVersion": (boolean, False),
    }


class Distribution(AWSProperty):
    """
    `Distribution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html>`__
    """

    props: PropsDictType = {
        "AmiDistributionConfiguration": (AmiDistributionConfiguration, False),
        "ContainerDistributionConfiguration": (
            ContainerDistributionConfiguration,
            False,
        ),
        "FastLaunchConfigurations": ([FastLaunchConfiguration], False),
        "LaunchTemplateConfigurations": ([LaunchTemplateConfiguration], False),
        "LicenseConfigurationArns": ([str], False),
        "Region": (str, True),
    }


class DistributionConfiguration(AWSObject):
    """
    `DistributionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html>`__
    """

    resource_type = "AWS::ImageBuilder::DistributionConfiguration"

    props: PropsDictType = {
        "Description": (str, False),
        "Distributions": ([Distribution], True),
        "Name": (str, True),
        "Tags": (dict, False),
    }


class ImageTestsConfiguration(AWSProperty):
    """
    `ImageTestsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html>`__
    """

    props: PropsDictType = {
        "ImageTestsEnabled": (boolean, False),
        "TimeoutMinutes": (integer, False),
    }


class Image(AWSObject):
    """
    `Image <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html>`__
    """

    resource_type = "AWS::ImageBuilder::Image"

    props: PropsDictType = {
        "ContainerRecipeArn": (str, False),
        "DistributionConfigurationArn": (str, False),
        "EnhancedImageMetadataEnabled": (boolean, False),
        "ImageRecipeArn": (str, False),
        "ImageTestsConfiguration": (ImageTestsConfiguration, False),
        "InfrastructureConfigurationArn": (str, True),
        "Tags": (dict, False),
    }


class Schedule(AWSProperty):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html>`__
    """

    props: PropsDictType = {
        "PipelineExecutionStartCondition": (
            schedule_pipelineexecutionstartcondition,
            False,
        ),
        "ScheduleExpression": (str, False),
    }


class ImagePipeline(AWSObject):
    """
    `ImagePipeline <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html>`__
    """

    resource_type = "AWS::ImageBuilder::ImagePipeline"

    props: PropsDictType = {
        "ContainerRecipeArn": (str, False),
        "Description": (str, False),
        "DistributionConfigurationArn": (str, False),
        "EnhancedImageMetadataEnabled": (boolean, False),
        "ImageRecipeArn": (str, False),
        "ImageTestsConfiguration": (ImageTestsConfiguration, False),
        "InfrastructureConfigurationArn": (str, True),
        "Name": (str, True),
        "Schedule": (Schedule, False),
        "Status": (imagepipeline_status, False),
        "Tags": (dict, False),
    }


class SystemsManagerAgent(AWSProperty):
    """
    `SystemsManagerAgent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html>`__
    """

    props: PropsDictType = {
        "UninstallAfterBuild": (boolean, False),
    }


class AdditionalInstanceConfiguration(AWSProperty):
    """
    `AdditionalInstanceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html>`__
    """

    props: PropsDictType = {
        "SystemsManagerAgent": (SystemsManagerAgent, False),
        "UserDataOverride": (str, False),
    }


class ComponentConfiguration(AWSProperty):
    """
    `ComponentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html>`__
    """

    props: PropsDictType = {
        "ComponentArn": (str, False),
        "Parameters": ([ComponentParameter], False),
    }


class ImageRecipe(AWSObject):
    """
    `ImageRecipe <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html>`__
    """

    resource_type = "AWS::ImageBuilder::ImageRecipe"

    props: PropsDictType = {
        "AdditionalInstanceConfiguration": (AdditionalInstanceConfiguration, False),
        "BlockDeviceMappings": ([InstanceBlockDeviceMapping], False),
        "Components": ([ComponentConfiguration], True),
        "Description": (str, False),
        "Name": (str, True),
        "ParentImage": (str, True),
        "Tags": (dict, False),
        "Version": (str, True),
        "WorkingDirectory": (str, False),
    }


class InstanceMetadataOptions(AWSProperty):
    """
    `InstanceMetadataOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html>`__
    """

    props: PropsDictType = {
        "HttpPutResponseHopLimit": (integer, False),
        "HttpTokens": (str, False),
    }


class S3Logs(AWSProperty):
    """
    `S3Logs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html>`__
    """

    props: PropsDictType = {
        "S3BucketName": (str, False),
        "S3KeyPrefix": (str, False),
    }


class Logging(AWSProperty):
    """
    `Logging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html>`__
    """

    props: PropsDictType = {
        "S3Logs": (S3Logs, False),
    }


class InfrastructureConfiguration(AWSObject):
    """
    `InfrastructureConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html>`__
    """

    resource_type = "AWS::ImageBuilder::InfrastructureConfiguration"

    props: PropsDictType = {
        "Description": (str, False),
        "InstanceMetadataOptions": (InstanceMetadataOptions, False),
        "InstanceProfileName": (str, True),
        "InstanceTypes": ([str], False),
        "KeyPair": (str, False),
        "Logging": (Logging, False),
        "Name": (str, True),
        "ResourceTags": (dict, False),
        "SecurityGroupIds": ([str], False),
        "SnsTopicArn": (str, False),
        "SubnetId": (str, False),
        "Tags": (dict, False),
        "TerminateInstanceOnFailure": (boolean, False),
    }
