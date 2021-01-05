// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class RundeckJob extends pulumi.CustomResource {
    /**
     * Get an existing RundeckJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RundeckJobState, opts?: pulumi.CustomResourceOptions): RundeckJob {
        return new RundeckJob(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'rundeck:index/rundeckJob:RundeckJob';

    /**
     * Returns true if the given object is an instance of RundeckJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RundeckJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RundeckJob.__pulumiType;
    }

    /**
     * Boolean defining whether two or more executions of
     * this job can run concurrently. The default is `false`, meaning that jobs will only run
     * sequentially.
     */
    public readonly allowConcurrentExecutions!: pulumi.Output<boolean | undefined>;
    public readonly commandOrderingStrategy!: pulumi.Output<string | undefined>;
    public readonly commands!: pulumi.Output<outputs.RundeckJobCommand[]>;
    /**
     * Boolean defining whether Rundeck will continue to run
     * subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
     * will stop and the execution will be considered to have failed.
     */
    public readonly continueOnError!: pulumi.Output<boolean | undefined>;
    /**
     * A longer description of the job, describing the job in the Rundeck UI.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * If you want job execution to be enabled or disabled. Defaults to `true`.
     */
    public readonly executionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name of a group within the project in which to place the job.
     * Setting this creates collapsable subcategories within the Rundeck UI's project job index.
     */
    public readonly groupName!: pulumi.Output<string | undefined>;
    /**
     * The log level that Rundeck should use for this job. Defaults to "INFO".
     */
    public readonly logLevel!: pulumi.Output<string | undefined>;
    /**
     * The maximum number of threads to use to execute this job, which
     * controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
     * the nodes will be visited sequentially.
     */
    public readonly maxThreadCount!: pulumi.Output<number | undefined>;
    /**
     * The name of the job, used to describe the job in the Rundeck UI.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly nodeFilterExcludePrecedence!: pulumi.Output<boolean | undefined>;
    /**
     * A query string using
     * [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
     * that defines which subset of the project's nodes will be used to execute this job.
     */
    public readonly nodeFilterQuery!: pulumi.Output<string | undefined>;
    public readonly notifications!: pulumi.Output<outputs.RundeckJobNotification[] | undefined>;
    public readonly options!: pulumi.Output<outputs.RundeckJobOption[] | undefined>;
    public readonly preserveOptionsOrder!: pulumi.Output<boolean>;
    /**
     * The name of the project that this job should belong to.
     */
    public readonly projectName!: pulumi.Output<string>;
    /**
     * The name of the attribute that will be used to decide in which
     * order the nodes will be visited while executing the job across multiple nodes.
     */
    public readonly rankAttribute!: pulumi.Output<string | undefined>;
    /**
     * Keyword deciding which direction the nodes are sorted in terms of
     * the chosen `rankAttribute`. May be either "ascending" (the default) or "descending".
     */
    public readonly rankOrder!: pulumi.Output<string | undefined>;
    /**
     * The jobs schedule in Unix crontab format
     */
    public readonly schedule!: pulumi.Output<string | undefined>;
    /**
     * Sets the job schedule to be enabled or disabled. Defaults to `true`.
     */
    public readonly scheduleEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Boolean determining if an empty node filter yields
     * a successful result.
     */
    public readonly successOnEmptyNodeFilter!: pulumi.Output<boolean | undefined>;

    /**
     * Create a RundeckJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RundeckJobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RundeckJobArgs | RundeckJobState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RundeckJobState | undefined;
            inputs["allowConcurrentExecutions"] = state ? state.allowConcurrentExecutions : undefined;
            inputs["commandOrderingStrategy"] = state ? state.commandOrderingStrategy : undefined;
            inputs["commands"] = state ? state.commands : undefined;
            inputs["continueOnError"] = state ? state.continueOnError : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["executionEnabled"] = state ? state.executionEnabled : undefined;
            inputs["groupName"] = state ? state.groupName : undefined;
            inputs["logLevel"] = state ? state.logLevel : undefined;
            inputs["maxThreadCount"] = state ? state.maxThreadCount : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nodeFilterExcludePrecedence"] = state ? state.nodeFilterExcludePrecedence : undefined;
            inputs["nodeFilterQuery"] = state ? state.nodeFilterQuery : undefined;
            inputs["notifications"] = state ? state.notifications : undefined;
            inputs["options"] = state ? state.options : undefined;
            inputs["preserveOptionsOrder"] = state ? state.preserveOptionsOrder : undefined;
            inputs["projectName"] = state ? state.projectName : undefined;
            inputs["rankAttribute"] = state ? state.rankAttribute : undefined;
            inputs["rankOrder"] = state ? state.rankOrder : undefined;
            inputs["schedule"] = state ? state.schedule : undefined;
            inputs["scheduleEnabled"] = state ? state.scheduleEnabled : undefined;
            inputs["successOnEmptyNodeFilter"] = state ? state.successOnEmptyNodeFilter : undefined;
        } else {
            const args = argsOrState as RundeckJobArgs | undefined;
            if (!args || args.commands === undefined) {
                throw new Error("Missing required property 'commands'");
            }
            if (!args || args.description === undefined) {
                throw new Error("Missing required property 'description'");
            }
            if (!args || args.projectName === undefined) {
                throw new Error("Missing required property 'projectName'");
            }
            inputs["allowConcurrentExecutions"] = args ? args.allowConcurrentExecutions : undefined;
            inputs["commandOrderingStrategy"] = args ? args.commandOrderingStrategy : undefined;
            inputs["commands"] = args ? args.commands : undefined;
            inputs["continueOnError"] = args ? args.continueOnError : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["executionEnabled"] = args ? args.executionEnabled : undefined;
            inputs["groupName"] = args ? args.groupName : undefined;
            inputs["logLevel"] = args ? args.logLevel : undefined;
            inputs["maxThreadCount"] = args ? args.maxThreadCount : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nodeFilterExcludePrecedence"] = args ? args.nodeFilterExcludePrecedence : undefined;
            inputs["nodeFilterQuery"] = args ? args.nodeFilterQuery : undefined;
            inputs["notifications"] = args ? args.notifications : undefined;
            inputs["options"] = args ? args.options : undefined;
            inputs["preserveOptionsOrder"] = args ? args.preserveOptionsOrder : undefined;
            inputs["projectName"] = args ? args.projectName : undefined;
            inputs["rankAttribute"] = args ? args.rankAttribute : undefined;
            inputs["rankOrder"] = args ? args.rankOrder : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["scheduleEnabled"] = args ? args.scheduleEnabled : undefined;
            inputs["successOnEmptyNodeFilter"] = args ? args.successOnEmptyNodeFilter : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RundeckJob.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RundeckJob resources.
 */
export interface RundeckJobState {
    /**
     * Boolean defining whether two or more executions of
     * this job can run concurrently. The default is `false`, meaning that jobs will only run
     * sequentially.
     */
    readonly allowConcurrentExecutions?: pulumi.Input<boolean>;
    readonly commandOrderingStrategy?: pulumi.Input<string>;
    readonly commands?: pulumi.Input<pulumi.Input<inputs.RundeckJobCommand>[]>;
    /**
     * Boolean defining whether Rundeck will continue to run
     * subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
     * will stop and the execution will be considered to have failed.
     */
    readonly continueOnError?: pulumi.Input<boolean>;
    /**
     * A longer description of the job, describing the job in the Rundeck UI.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * If you want job execution to be enabled or disabled. Defaults to `true`.
     */
    readonly executionEnabled?: pulumi.Input<boolean>;
    /**
     * The name of a group within the project in which to place the job.
     * Setting this creates collapsable subcategories within the Rundeck UI's project job index.
     */
    readonly groupName?: pulumi.Input<string>;
    /**
     * The log level that Rundeck should use for this job. Defaults to "INFO".
     */
    readonly logLevel?: pulumi.Input<string>;
    /**
     * The maximum number of threads to use to execute this job, which
     * controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
     * the nodes will be visited sequentially.
     */
    readonly maxThreadCount?: pulumi.Input<number>;
    /**
     * The name of the job, used to describe the job in the Rundeck UI.
     */
    readonly name?: pulumi.Input<string>;
    readonly nodeFilterExcludePrecedence?: pulumi.Input<boolean>;
    /**
     * A query string using
     * [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
     * that defines which subset of the project's nodes will be used to execute this job.
     */
    readonly nodeFilterQuery?: pulumi.Input<string>;
    readonly notifications?: pulumi.Input<pulumi.Input<inputs.RundeckJobNotification>[]>;
    readonly options?: pulumi.Input<pulumi.Input<inputs.RundeckJobOption>[]>;
    readonly preserveOptionsOrder?: pulumi.Input<boolean>;
    /**
     * The name of the project that this job should belong to.
     */
    readonly projectName?: pulumi.Input<string>;
    /**
     * The name of the attribute that will be used to decide in which
     * order the nodes will be visited while executing the job across multiple nodes.
     */
    readonly rankAttribute?: pulumi.Input<string>;
    /**
     * Keyword deciding which direction the nodes are sorted in terms of
     * the chosen `rankAttribute`. May be either "ascending" (the default) or "descending".
     */
    readonly rankOrder?: pulumi.Input<string>;
    /**
     * The jobs schedule in Unix crontab format
     */
    readonly schedule?: pulumi.Input<string>;
    /**
     * Sets the job schedule to be enabled or disabled. Defaults to `true`.
     */
    readonly scheduleEnabled?: pulumi.Input<boolean>;
    /**
     * Boolean determining if an empty node filter yields
     * a successful result.
     */
    readonly successOnEmptyNodeFilter?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a RundeckJob resource.
 */
export interface RundeckJobArgs {
    /**
     * Boolean defining whether two or more executions of
     * this job can run concurrently. The default is `false`, meaning that jobs will only run
     * sequentially.
     */
    readonly allowConcurrentExecutions?: pulumi.Input<boolean>;
    readonly commandOrderingStrategy?: pulumi.Input<string>;
    readonly commands: pulumi.Input<pulumi.Input<inputs.RundeckJobCommand>[]>;
    /**
     * Boolean defining whether Rundeck will continue to run
     * subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
     * will stop and the execution will be considered to have failed.
     */
    readonly continueOnError?: pulumi.Input<boolean>;
    /**
     * A longer description of the job, describing the job in the Rundeck UI.
     */
    readonly description: pulumi.Input<string>;
    /**
     * If you want job execution to be enabled or disabled. Defaults to `true`.
     */
    readonly executionEnabled?: pulumi.Input<boolean>;
    /**
     * The name of a group within the project in which to place the job.
     * Setting this creates collapsable subcategories within the Rundeck UI's project job index.
     */
    readonly groupName?: pulumi.Input<string>;
    /**
     * The log level that Rundeck should use for this job. Defaults to "INFO".
     */
    readonly logLevel?: pulumi.Input<string>;
    /**
     * The maximum number of threads to use to execute this job, which
     * controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
     * the nodes will be visited sequentially.
     */
    readonly maxThreadCount?: pulumi.Input<number>;
    /**
     * The name of the job, used to describe the job in the Rundeck UI.
     */
    readonly name?: pulumi.Input<string>;
    readonly nodeFilterExcludePrecedence?: pulumi.Input<boolean>;
    /**
     * A query string using
     * [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
     * that defines which subset of the project's nodes will be used to execute this job.
     */
    readonly nodeFilterQuery?: pulumi.Input<string>;
    readonly notifications?: pulumi.Input<pulumi.Input<inputs.RundeckJobNotification>[]>;
    readonly options?: pulumi.Input<pulumi.Input<inputs.RundeckJobOption>[]>;
    readonly preserveOptionsOrder?: pulumi.Input<boolean>;
    /**
     * The name of the project that this job should belong to.
     */
    readonly projectName: pulumi.Input<string>;
    /**
     * The name of the attribute that will be used to decide in which
     * order the nodes will be visited while executing the job across multiple nodes.
     */
    readonly rankAttribute?: pulumi.Input<string>;
    /**
     * Keyword deciding which direction the nodes are sorted in terms of
     * the chosen `rankAttribute`. May be either "ascending" (the default) or "descending".
     */
    readonly rankOrder?: pulumi.Input<string>;
    /**
     * The jobs schedule in Unix crontab format
     */
    readonly schedule?: pulumi.Input<string>;
    /**
     * Sets the job schedule to be enabled or disabled. Defaults to `true`.
     */
    readonly scheduleEnabled?: pulumi.Input<boolean>;
    /**
     * Boolean determining if an empty node filter yields
     * a successful result.
     */
    readonly successOnEmptyNodeFilter?: pulumi.Input<boolean>;
}