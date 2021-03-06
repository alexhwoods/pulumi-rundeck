# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'RundeckJobCommandArgs',
    'RundeckJobCommandJobArgs',
    'RundeckJobCommandJobNodefiltersArgs',
    'RundeckJobCommandNodeStepPluginArgs',
    'RundeckJobCommandStepPluginArgs',
    'RundeckJobNotificationArgs',
    'RundeckJobNotificationEmailArgs',
    'RundeckJobNotificationPluginArgs',
    'RundeckJobOptionArgs',
    'RundeckProjectResourceModelSourceArgs',
]

@pulumi.input_type
class RundeckJobCommandArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 inline_script: Optional[pulumi.Input[str]] = None,
                 jobs: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandJobArgs']]]] = None,
                 node_step_plugins: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandNodeStepPluginArgs']]]] = None,
                 script_file: Optional[pulumi.Input[str]] = None,
                 script_file_args: Optional[pulumi.Input[str]] = None,
                 shell_command: Optional[pulumi.Input[str]] = None,
                 step_plugins: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandStepPluginArgs']]]] = None):
        """
        :param pulumi.Input[str] description: A longer description of the job, describing the job in the Rundeck UI.
        :param pulumi.Input[str] inline_script: gives a whole shell script, inline in the configuration, to execute on the nodes.
        :param pulumi.Input[str] script_file: and `script_file_args` together describe a script that is already pre-installed
               on the nodes which is to be executed.
        :param pulumi.Input[str] shell_command: gives a single shell command to execute on the nodes.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if inline_script is not None:
            pulumi.set(__self__, "inline_script", inline_script)
        if jobs is not None:
            pulumi.set(__self__, "jobs", jobs)
        if node_step_plugins is not None:
            pulumi.set(__self__, "node_step_plugins", node_step_plugins)
        if script_file is not None:
            pulumi.set(__self__, "script_file", script_file)
        if script_file_args is not None:
            pulumi.set(__self__, "script_file_args", script_file_args)
        if shell_command is not None:
            pulumi.set(__self__, "shell_command", shell_command)
        if step_plugins is not None:
            pulumi.set(__self__, "step_plugins", step_plugins)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A longer description of the job, describing the job in the Rundeck UI.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="inlineScript")
    def inline_script(self) -> Optional[pulumi.Input[str]]:
        """
        gives a whole shell script, inline in the configuration, to execute on the nodes.
        """
        return pulumi.get(self, "inline_script")

    @inline_script.setter
    def inline_script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inline_script", value)

    @property
    @pulumi.getter
    def jobs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandJobArgs']]]]:
        return pulumi.get(self, "jobs")

    @jobs.setter
    def jobs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandJobArgs']]]]):
        pulumi.set(self, "jobs", value)

    @property
    @pulumi.getter(name="nodeStepPlugins")
    def node_step_plugins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandNodeStepPluginArgs']]]]:
        return pulumi.get(self, "node_step_plugins")

    @node_step_plugins.setter
    def node_step_plugins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandNodeStepPluginArgs']]]]):
        pulumi.set(self, "node_step_plugins", value)

    @property
    @pulumi.getter(name="scriptFile")
    def script_file(self) -> Optional[pulumi.Input[str]]:
        """
        and `script_file_args` together describe a script that is already pre-installed
        on the nodes which is to be executed.
        """
        return pulumi.get(self, "script_file")

    @script_file.setter
    def script_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_file", value)

    @property
    @pulumi.getter(name="scriptFileArgs")
    def script_file_args(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "script_file_args")

    @script_file_args.setter
    def script_file_args(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_file_args", value)

    @property
    @pulumi.getter(name="shellCommand")
    def shell_command(self) -> Optional[pulumi.Input[str]]:
        """
        gives a single shell command to execute on the nodes.
        """
        return pulumi.get(self, "shell_command")

    @shell_command.setter
    def shell_command(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shell_command", value)

    @property
    @pulumi.getter(name="stepPlugins")
    def step_plugins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandStepPluginArgs']]]]:
        return pulumi.get(self, "step_plugins")

    @step_plugins.setter
    def step_plugins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobCommandStepPluginArgs']]]]):
        pulumi.set(self, "step_plugins", value)


@pulumi.input_type
class RundeckJobCommandJobArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 args: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 nodefilters: Optional[pulumi.Input['RundeckJobCommandJobNodefiltersArgs']] = None,
                 run_for_each_node: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] name: The name of the job, used to describe the job in the Rundeck UI.
        :param pulumi.Input[str] group_name: The name of a group within the project in which to place the job.
               Setting this creates collapsable subcategories within the Rundeck UI's project job index.
        """
        pulumi.set(__self__, "name", name)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if nodefilters is not None:
            pulumi.set(__self__, "nodefilters", nodefilters)
        if run_for_each_node is not None:
            pulumi.set(__self__, "run_for_each_node", run_for_each_node)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the job, used to describe the job in the Rundeck UI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of a group within the project in which to place the job.
        Setting this creates collapsable subcategories within the Rundeck UI's project job index.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter
    def nodefilters(self) -> Optional[pulumi.Input['RundeckJobCommandJobNodefiltersArgs']]:
        return pulumi.get(self, "nodefilters")

    @nodefilters.setter
    def nodefilters(self, value: Optional[pulumi.Input['RundeckJobCommandJobNodefiltersArgs']]):
        pulumi.set(self, "nodefilters", value)

    @property
    @pulumi.getter(name="runForEachNode")
    def run_for_each_node(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "run_for_each_node")

    @run_for_each_node.setter
    def run_for_each_node(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_for_each_node", value)


@pulumi.input_type
class RundeckJobCommandJobNodefiltersArgs:
    def __init__(__self__, *,
                 excludeprecedence: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None):
        if excludeprecedence is not None:
            pulumi.set(__self__, "excludeprecedence", excludeprecedence)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter
    def excludeprecedence(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "excludeprecedence")

    @excludeprecedence.setter
    def excludeprecedence(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "excludeprecedence", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)


@pulumi.input_type
class RundeckJobCommandNodeStepPluginArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        :param pulumi.Input[str] type: The name of the plugin to use.
        :param pulumi.Input[Mapping[str, Any]] config: Map of arbitrary configuration properties for the selected plugin.
        """
        pulumi.set(__self__, "type", type)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the plugin to use.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of arbitrary configuration properties for the selected plugin.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class RundeckJobCommandStepPluginArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        :param pulumi.Input[str] type: The name of the plugin to use.
        :param pulumi.Input[Mapping[str, Any]] config: Map of arbitrary configuration properties for the selected plugin.
        """
        pulumi.set(__self__, "type", type)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the plugin to use.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of arbitrary configuration properties for the selected plugin.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class RundeckJobNotificationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 emails: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationEmailArgs']]]] = None,
                 plugins: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationPluginArgs']]]] = None,
                 webhook_urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] type: The name of the plugin to use.
        """
        pulumi.set(__self__, "type", type)
        if emails is not None:
            pulumi.set(__self__, "emails", emails)
        if plugins is not None:
            pulumi.set(__self__, "plugins", plugins)
        if webhook_urls is not None:
            pulumi.set(__self__, "webhook_urls", webhook_urls)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the plugin to use.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationEmailArgs']]]]:
        return pulumi.get(self, "emails")

    @emails.setter
    def emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationEmailArgs']]]]):
        pulumi.set(self, "emails", value)

    @property
    @pulumi.getter
    def plugins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationPluginArgs']]]]:
        return pulumi.get(self, "plugins")

    @plugins.setter
    def plugins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RundeckJobNotificationPluginArgs']]]]):
        pulumi.set(self, "plugins", value)

    @property
    @pulumi.getter(name="webhookUrls")
    def webhook_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "webhook_urls")

    @webhook_urls.setter
    def webhook_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "webhook_urls", value)


@pulumi.input_type
class RundeckJobNotificationEmailArgs:
    def __init__(__self__, *,
                 recipients: pulumi.Input[Sequence[pulumi.Input[str]]],
                 attach_log: Optional[pulumi.Input[bool]] = None,
                 subject: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "recipients", recipients)
        if attach_log is not None:
            pulumi.set(__self__, "attach_log", attach_log)
        if subject is not None:
            pulumi.set(__self__, "subject", subject)

    @property
    @pulumi.getter
    def recipients(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "recipients")

    @recipients.setter
    def recipients(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "recipients", value)

    @property
    @pulumi.getter(name="attachLog")
    def attach_log(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "attach_log")

    @attach_log.setter
    def attach_log(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "attach_log", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject", value)


@pulumi.input_type
class RundeckJobNotificationPluginArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        :param pulumi.Input[str] type: The name of the plugin to use.
        :param pulumi.Input[Mapping[str, Any]] config: Map of arbitrary configuration properties for the selected plugin.
        """
        pulumi.set(__self__, "type", type)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the plugin to use.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of arbitrary configuration properties for the selected plugin.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class RundeckJobOptionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 allow_multiple_values: Optional[pulumi.Input[bool]] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exposed_to_scripts: Optional[pulumi.Input[bool]] = None,
                 multi_value_delimiter: Optional[pulumi.Input[str]] = None,
                 obscure_input: Optional[pulumi.Input[bool]] = None,
                 require_predefined_choice: Optional[pulumi.Input[bool]] = None,
                 required: Optional[pulumi.Input[bool]] = None,
                 validation_regex: Optional[pulumi.Input[str]] = None,
                 value_choices: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value_choices_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of the job, used to describe the job in the Rundeck UI.
        :param pulumi.Input[str] description: A longer description of the job, describing the job in the Rundeck UI.
        """
        pulumi.set(__self__, "name", name)
        if allow_multiple_values is not None:
            pulumi.set(__self__, "allow_multiple_values", allow_multiple_values)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if exposed_to_scripts is not None:
            pulumi.set(__self__, "exposed_to_scripts", exposed_to_scripts)
        if multi_value_delimiter is not None:
            pulumi.set(__self__, "multi_value_delimiter", multi_value_delimiter)
        if obscure_input is not None:
            pulumi.set(__self__, "obscure_input", obscure_input)
        if require_predefined_choice is not None:
            pulumi.set(__self__, "require_predefined_choice", require_predefined_choice)
        if required is not None:
            pulumi.set(__self__, "required", required)
        if validation_regex is not None:
            pulumi.set(__self__, "validation_regex", validation_regex)
        if value_choices is not None:
            pulumi.set(__self__, "value_choices", value_choices)
        if value_choices_url is not None:
            pulumi.set(__self__, "value_choices_url", value_choices_url)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the job, used to describe the job in the Rundeck UI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="allowMultipleValues")
    def allow_multiple_values(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_multiple_values")

    @allow_multiple_values.setter
    def allow_multiple_values(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_multiple_values", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A longer description of the job, describing the job in the Rundeck UI.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="exposedToScripts")
    def exposed_to_scripts(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "exposed_to_scripts")

    @exposed_to_scripts.setter
    def exposed_to_scripts(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exposed_to_scripts", value)

    @property
    @pulumi.getter(name="multiValueDelimiter")
    def multi_value_delimiter(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "multi_value_delimiter")

    @multi_value_delimiter.setter
    def multi_value_delimiter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "multi_value_delimiter", value)

    @property
    @pulumi.getter(name="obscureInput")
    def obscure_input(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "obscure_input")

    @obscure_input.setter
    def obscure_input(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "obscure_input", value)

    @property
    @pulumi.getter(name="requirePredefinedChoice")
    def require_predefined_choice(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "require_predefined_choice")

    @require_predefined_choice.setter
    def require_predefined_choice(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_predefined_choice", value)

    @property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "required")

    @required.setter
    def required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "required", value)

    @property
    @pulumi.getter(name="validationRegex")
    def validation_regex(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "validation_regex")

    @validation_regex.setter
    def validation_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_regex", value)

    @property
    @pulumi.getter(name="valueChoices")
    def value_choices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "value_choices")

    @value_choices.setter
    def value_choices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "value_choices", value)

    @property
    @pulumi.getter(name="valueChoicesUrl")
    def value_choices_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value_choices_url")

    @value_choices_url.setter
    def value_choices_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_choices_url", value)


@pulumi.input_type
class RundeckProjectResourceModelSourceArgs:
    def __init__(__self__, *,
                 config: pulumi.Input[Mapping[str, Any]],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[Mapping[str, Any]] config: Map of arbitrary configuration properties for the selected resource model
               plugin.
        :param pulumi.Input[str] type: The name of the resource model plugin to use.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input[Mapping[str, Any]]:
        """
        Map of arbitrary configuration properties for the selected resource model
        plugin.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input[Mapping[str, Any]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the resource model plugin to use.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


