// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface RundeckJobCommand {
    /**
     * A longer description of the job, describing the job in the Rundeck UI.
     */
    description?: string;
    /**
     * gives a whole shell script, inline in the configuration, to execute on the nodes.
     */
    inlineScript?: string;
    jobs?: outputs.RundeckJobCommandJob[];
    nodeStepPlugins?: outputs.RundeckJobCommandNodeStepPlugin[];
    /**
     * and `scriptFileArgs` together describe a script that is already pre-installed
     * on the nodes which is to be executed.
     */
    scriptFile?: string;
    scriptFileArgs?: string;
    /**
     * gives a single shell command to execute on the nodes.
     */
    shellCommand?: string;
    stepPlugins?: outputs.RundeckJobCommandStepPlugin[];
}

export interface RundeckJobCommandJob {
    args?: string;
    /**
     * The name of a group within the project in which to place the job.
     * Setting this creates collapsable subcategories within the Rundeck UI's project job index.
     */
    groupName?: string;
    /**
     * The name of the job, used to describe the job in the Rundeck UI.
     */
    name: string;
    nodefilters?: outputs.RundeckJobCommandJobNodefilters;
    runForEachNode?: boolean;
}

export interface RundeckJobCommandJobNodefilters {
    excludeprecedence?: string;
    filter?: string;
}

export interface RundeckJobCommandNodeStepPlugin {
    /**
     * Map of arbitrary configuration properties for the selected plugin.
     */
    config?: {[key: string]: any};
    /**
     * The name of the plugin to use.
     */
    type: string;
}

export interface RundeckJobCommandStepPlugin {
    /**
     * Map of arbitrary configuration properties for the selected plugin.
     */
    config?: {[key: string]: any};
    /**
     * The name of the plugin to use.
     */
    type: string;
}

export interface RundeckJobNotification {
    emails?: outputs.RundeckJobNotificationEmail[];
    plugins?: outputs.RundeckJobNotificationPlugin[];
    /**
     * The name of the plugin to use.
     */
    type: string;
    webhookUrls?: string[];
}

export interface RundeckJobNotificationEmail {
    attachLog?: boolean;
    recipients: string[];
    subject?: string;
}

export interface RundeckJobNotificationPlugin {
    /**
     * Map of arbitrary configuration properties for the selected plugin.
     */
    config?: {[key: string]: any};
    /**
     * The name of the plugin to use.
     */
    type: string;
}

export interface RundeckJobOption {
    allowMultipleValues?: boolean;
    defaultValue?: string;
    /**
     * A longer description of the job, describing the job in the Rundeck UI.
     */
    description?: string;
    exposedToScripts?: boolean;
    multiValueDelimiter?: string;
    /**
     * The name of the job, used to describe the job in the Rundeck UI.
     */
    name: string;
    obscureInput?: boolean;
    requirePredefinedChoice?: boolean;
    required?: boolean;
    validationRegex?: string;
    valueChoices?: string[];
    valueChoicesUrl?: string;
}

export interface RundeckProjectResourceModelSource {
    /**
     * Map of arbitrary configuration properties for the selected resource model
     * plugin.
     */
    config: {[key: string]: any};
    /**
     * The name of the resource model plugin to use.
     */
    type: string;
}
