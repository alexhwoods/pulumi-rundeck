# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['RundeckProject']


class RundeckProject(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_node_executor_plugin: Optional[pulumi.Input[str]] = None,
                 default_node_file_copier_plugin: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 extra_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_model_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RundeckProjectResourceModelSourceArgs']]]]] = None,
                 ssh_authentication_type: Optional[pulumi.Input[str]] = None,
                 ssh_key_file_path: Optional[pulumi.Input[str]] = None,
                 ssh_key_storage_path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a RundeckProject resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_node_executor_plugin: The name of a plugin to use to run commands on
               nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
               nodes.
        :param pulumi.Input[str] default_node_file_copier_plugin: The name of a plugin to use to copy files onto
               nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
               to send files over SSH.
        :param pulumi.Input[str] description: Description of the project to be shown in the Rundeck UI
        :param pulumi.Input[Mapping[str, Any]] extra_config: Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
               key names due to limitations in Terraform's config language.
        :param pulumi.Input[str] name: The name of the project, used both in the UI and to uniquely identify
               the project. Must therefore be unique across a single Rundeck installation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RundeckProjectResourceModelSourceArgs']]]] resource_model_sources: Nested block instructing Rundeck on how to determine the
               set of resources (nodes) for this project. The nested block structure is described below.
        :param pulumi.Input[str] ssh_authentication_type: When the SSH-based file copier and executor plugins are
               used, the type of SSH authentication to use. Defaults to `privateKey`.
        :param pulumi.Input[str] ssh_key_file_path: Like `ssh_key_storage_path` except that the key is read from
               the Rundeck server's local filesystem, rather than from the key store.
        :param pulumi.Input[str] ssh_key_storage_path: When the SSH-based file copier and executor plugins are
               used, the location within Rundeck's key store where the SSH private key can be found. Private
               keys can be uploaded to rundeck using the `RundeckPrivateKey` resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['default_node_executor_plugin'] = default_node_executor_plugin
            __props__['default_node_file_copier_plugin'] = default_node_file_copier_plugin
            __props__['description'] = description
            __props__['extra_config'] = extra_config
            __props__['name'] = name
            if resource_model_sources is None:
                raise TypeError("Missing required property 'resource_model_sources'")
            __props__['resource_model_sources'] = resource_model_sources
            __props__['ssh_authentication_type'] = ssh_authentication_type
            __props__['ssh_key_file_path'] = ssh_key_file_path
            __props__['ssh_key_storage_path'] = ssh_key_storage_path
            __props__['ui_url'] = None
        super(RundeckProject, __self__).__init__(
            'rundeck:index/rundeckProject:RundeckProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_node_executor_plugin: Optional[pulumi.Input[str]] = None,
            default_node_file_copier_plugin: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            extra_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_model_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RundeckProjectResourceModelSourceArgs']]]]] = None,
            ssh_authentication_type: Optional[pulumi.Input[str]] = None,
            ssh_key_file_path: Optional[pulumi.Input[str]] = None,
            ssh_key_storage_path: Optional[pulumi.Input[str]] = None,
            ui_url: Optional[pulumi.Input[str]] = None) -> 'RundeckProject':
        """
        Get an existing RundeckProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_node_executor_plugin: The name of a plugin to use to run commands on
               nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
               nodes.
        :param pulumi.Input[str] default_node_file_copier_plugin: The name of a plugin to use to copy files onto
               nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
               to send files over SSH.
        :param pulumi.Input[str] description: Description of the project to be shown in the Rundeck UI
        :param pulumi.Input[Mapping[str, Any]] extra_config: Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
               key names due to limitations in Terraform's config language.
        :param pulumi.Input[str] name: The name of the project, used both in the UI and to uniquely identify
               the project. Must therefore be unique across a single Rundeck installation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RundeckProjectResourceModelSourceArgs']]]] resource_model_sources: Nested block instructing Rundeck on how to determine the
               set of resources (nodes) for this project. The nested block structure is described below.
        :param pulumi.Input[str] ssh_authentication_type: When the SSH-based file copier and executor plugins are
               used, the type of SSH authentication to use. Defaults to `privateKey`.
        :param pulumi.Input[str] ssh_key_file_path: Like `ssh_key_storage_path` except that the key is read from
               the Rundeck server's local filesystem, rather than from the key store.
        :param pulumi.Input[str] ssh_key_storage_path: When the SSH-based file copier and executor plugins are
               used, the location within Rundeck's key store where the SSH private key can be found. Private
               keys can be uploaded to rundeck using the `RundeckPrivateKey` resource.
        :param pulumi.Input[str] ui_url: The URL of the index page for this project in the Rundeck UI.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_node_executor_plugin"] = default_node_executor_plugin
        __props__["default_node_file_copier_plugin"] = default_node_file_copier_plugin
        __props__["description"] = description
        __props__["extra_config"] = extra_config
        __props__["name"] = name
        __props__["resource_model_sources"] = resource_model_sources
        __props__["ssh_authentication_type"] = ssh_authentication_type
        __props__["ssh_key_file_path"] = ssh_key_file_path
        __props__["ssh_key_storage_path"] = ssh_key_storage_path
        __props__["ui_url"] = ui_url
        return RundeckProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultNodeExecutorPlugin")
    def default_node_executor_plugin(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a plugin to use to run commands on
        nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
        nodes.
        """
        return pulumi.get(self, "default_node_executor_plugin")

    @property
    @pulumi.getter(name="defaultNodeFileCopierPlugin")
    def default_node_file_copier_plugin(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a plugin to use to copy files onto
        nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
        to send files over SSH.
        """
        return pulumi.get(self, "default_node_file_copier_plugin")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the project to be shown in the Rundeck UI
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="extraConfig")
    def extra_config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
        key names due to limitations in Terraform's config language.
        """
        return pulumi.get(self, "extra_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the project, used both in the UI and to uniquely identify
        the project. Must therefore be unique across a single Rundeck installation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceModelSources")
    def resource_model_sources(self) -> pulumi.Output[Sequence['outputs.RundeckProjectResourceModelSource']]:
        """
        Nested block instructing Rundeck on how to determine the
        set of resources (nodes) for this project. The nested block structure is described below.
        """
        return pulumi.get(self, "resource_model_sources")

    @property
    @pulumi.getter(name="sshAuthenticationType")
    def ssh_authentication_type(self) -> pulumi.Output[Optional[str]]:
        """
        When the SSH-based file copier and executor plugins are
        used, the type of SSH authentication to use. Defaults to `privateKey`.
        """
        return pulumi.get(self, "ssh_authentication_type")

    @property
    @pulumi.getter(name="sshKeyFilePath")
    def ssh_key_file_path(self) -> pulumi.Output[Optional[str]]:
        """
        Like `ssh_key_storage_path` except that the key is read from
        the Rundeck server's local filesystem, rather than from the key store.
        """
        return pulumi.get(self, "ssh_key_file_path")

    @property
    @pulumi.getter(name="sshKeyStoragePath")
    def ssh_key_storage_path(self) -> pulumi.Output[Optional[str]]:
        """
        When the SSH-based file copier and executor plugins are
        used, the location within Rundeck's key store where the SSH private key can be found. Private
        keys can be uploaded to rundeck using the `RundeckPrivateKey` resource.
        """
        return pulumi.get(self, "ssh_key_storage_path")

    @property
    @pulumi.getter(name="uiUrl")
    def ui_url(self) -> pulumi.Output[str]:
        """
        The URL of the index page for this project in the Rundeck UI.
        """
        return pulumi.get(self, "ui_url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

