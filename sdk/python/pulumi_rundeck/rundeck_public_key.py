# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RundeckPublicKey']


class RundeckPublicKey(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_material: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The public key resource allows SSH public keys to be stored into Rundeck's key store.
        The key store is where Rundeck keeps credentials that are needed to access the nodes on which
        it runs commands.

        This resource also allows the retrieval of an existing public key from the store, so that it
        may be used in the configuration of other resources such as ``aws_key_pair``.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rundeck as rundeck

        anvils = rundeck.RundeckPublicKey("anvils",
            key_material="ssh-rsa yada-yada-yada",
            path="anvils/id_rsa.pub")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_material: The public key string to store, serialized in any way that is accepted
               by OpenSSH. If this is not included, ``key_material`` becomes an attribute that can be used
               to read the already-existing key material in the Rundeck store.
        :param pulumi.Input[str] path: The path within the key store where the key will be stored. By convention
               this path name normally ends with ".pub" and otherwise has the same name as the associated
               private key.
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

            __props__['key_material'] = key_material
            if path is None:
                raise TypeError("Missing required property 'path'")
            __props__['path'] = path
            __props__['delete'] = None
            __props__['url'] = None
        super(RundeckPublicKey, __self__).__init__(
            'rundeck:index/rundeckPublicKey:RundeckPublicKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delete: Optional[pulumi.Input[bool]] = None,
            key_material: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'RundeckPublicKey':
        """
        Get an existing RundeckPublicKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete: True if the key should be deleted when the resource is deleted. 
               Defaults to true if key_material is provided in the configuration.
        :param pulumi.Input[str] key_material: The public key string to store, serialized in any way that is accepted
               by OpenSSH. If this is not included, ``key_material`` becomes an attribute that can be used
               to read the already-existing key material in the Rundeck store.
        :param pulumi.Input[str] path: The path within the key store where the key will be stored. By convention
               this path name normally ends with ".pub" and otherwise has the same name as the associated
               private key.
        :param pulumi.Input[str] url: The URL at which the key material can be retrieved from the key store by other clients.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["delete"] = delete
        __props__["key_material"] = key_material
        __props__["path"] = path
        __props__["url"] = url
        return RundeckPublicKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def delete(self) -> pulumi.Output[bool]:
        """
        True if the key should be deleted when the resource is deleted. 
        Defaults to true if key_material is provided in the configuration.
        """
        return pulumi.get(self, "delete")

    @property
    @pulumi.getter(name="keyMaterial")
    def key_material(self) -> pulumi.Output[str]:
        """
        The public key string to store, serialized in any way that is accepted
        by OpenSSH. If this is not included, ``key_material`` becomes an attribute that can be used
        to read the already-existing key material in the Rundeck store.
        """
        return pulumi.get(self, "key_material")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The path within the key store where the key will be stored. By convention
        this path name normally ends with ".pub" and otherwise has the same name as the associated
        private key.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL at which the key material can be retrieved from the key store by other clients.
        """
        return pulumi.get(self, "url")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

