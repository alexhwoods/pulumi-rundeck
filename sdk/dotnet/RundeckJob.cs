// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Rundeck
{
    public partial class RundeckJob : Pulumi.CustomResource
    {
        /// <summary>
        /// Boolean defining whether two or more executions of
        /// this job can run concurrently. The default is `false`, meaning that jobs will only run
        /// sequentially.
        /// </summary>
        [Output("allowConcurrentExecutions")]
        public Output<bool?> AllowConcurrentExecutions { get; private set; } = null!;

        [Output("commandOrderingStrategy")]
        public Output<string?> CommandOrderingStrategy { get; private set; } = null!;

        [Output("commands")]
        public Output<ImmutableArray<Outputs.RundeckJobCommand>> Commands { get; private set; } = null!;

        /// <summary>
        /// Boolean defining whether Rundeck will continue to run
        /// subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
        /// will stop and the execution will be considered to have failed.
        /// </summary>
        [Output("continueOnError")]
        public Output<bool?> ContinueOnError { get; private set; } = null!;

        /// <summary>
        /// A longer description of the job, describing the job in the Rundeck UI.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// If you want job execution to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Output("executionEnabled")]
        public Output<bool?> ExecutionEnabled { get; private set; } = null!;

        /// <summary>
        /// The name of a group within the project in which to place the job.
        /// Setting this creates collapsable subcategories within the Rundeck UI's project job index.
        /// </summary>
        [Output("groupName")]
        public Output<string?> GroupName { get; private set; } = null!;

        /// <summary>
        /// The log level that Rundeck should use for this job. Defaults to "INFO".
        /// </summary>
        [Output("logLevel")]
        public Output<string?> LogLevel { get; private set; } = null!;

        /// <summary>
        /// The maximum number of threads to use to execute this job, which
        /// controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
        /// the nodes will be visited sequentially.
        /// </summary>
        [Output("maxThreadCount")]
        public Output<int?> MaxThreadCount { get; private set; } = null!;

        /// <summary>
        /// The name of the job, used to describe the job in the Rundeck UI.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nodeFilterExcludePrecedence")]
        public Output<bool?> NodeFilterExcludePrecedence { get; private set; } = null!;

        /// <summary>
        /// A query string using
        /// [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
        /// that defines which subset of the project's nodes will be used to execute this job.
        /// </summary>
        [Output("nodeFilterQuery")]
        public Output<string?> NodeFilterQuery { get; private set; } = null!;

        [Output("notifications")]
        public Output<ImmutableArray<Outputs.RundeckJobNotification>> Notifications { get; private set; } = null!;

        [Output("options")]
        public Output<ImmutableArray<Outputs.RundeckJobOption>> Options { get; private set; } = null!;

        [Output("preserveOptionsOrder")]
        public Output<bool> PreserveOptionsOrder { get; private set; } = null!;

        /// <summary>
        /// The name of the project that this job should belong to.
        /// </summary>
        [Output("projectName")]
        public Output<string> ProjectName { get; private set; } = null!;

        /// <summary>
        /// The name of the attribute that will be used to decide in which
        /// order the nodes will be visited while executing the job across multiple nodes.
        /// </summary>
        [Output("rankAttribute")]
        public Output<string?> RankAttribute { get; private set; } = null!;

        /// <summary>
        /// Keyword deciding which direction the nodes are sorted in terms of
        /// the chosen `rank_attribute`. May be either "ascending" (the default) or "descending".
        /// </summary>
        [Output("rankOrder")]
        public Output<string?> RankOrder { get; private set; } = null!;

        /// <summary>
        /// The jobs schedule in Unix crontab format
        /// </summary>
        [Output("schedule")]
        public Output<string?> Schedule { get; private set; } = null!;

        /// <summary>
        /// Sets the job schedule to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Output("scheduleEnabled")]
        public Output<bool?> ScheduleEnabled { get; private set; } = null!;

        /// <summary>
        /// Boolean determining if an empty node filter yields
        /// a successful result.
        /// </summary>
        [Output("successOnEmptyNodeFilter")]
        public Output<bool?> SuccessOnEmptyNodeFilter { get; private set; } = null!;


        /// <summary>
        /// Create a RundeckJob resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RundeckJob(string name, RundeckJobArgs args, CustomResourceOptions? options = null)
            : base("rundeck:index/rundeckJob:RundeckJob", name, args ?? new RundeckJobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RundeckJob(string name, Input<string> id, RundeckJobState? state = null, CustomResourceOptions? options = null)
            : base("rundeck:index/rundeckJob:RundeckJob", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RundeckJob resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RundeckJob Get(string name, Input<string> id, RundeckJobState? state = null, CustomResourceOptions? options = null)
        {
            return new RundeckJob(name, id, state, options);
        }
    }

    public sealed class RundeckJobArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean defining whether two or more executions of
        /// this job can run concurrently. The default is `false`, meaning that jobs will only run
        /// sequentially.
        /// </summary>
        [Input("allowConcurrentExecutions")]
        public Input<bool>? AllowConcurrentExecutions { get; set; }

        [Input("commandOrderingStrategy")]
        public Input<string>? CommandOrderingStrategy { get; set; }

        [Input("commands", required: true)]
        private InputList<Inputs.RundeckJobCommandArgs>? _commands;
        public InputList<Inputs.RundeckJobCommandArgs> Commands
        {
            get => _commands ?? (_commands = new InputList<Inputs.RundeckJobCommandArgs>());
            set => _commands = value;
        }

        /// <summary>
        /// Boolean defining whether Rundeck will continue to run
        /// subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
        /// will stop and the execution will be considered to have failed.
        /// </summary>
        [Input("continueOnError")]
        public Input<bool>? ContinueOnError { get; set; }

        /// <summary>
        /// A longer description of the job, describing the job in the Rundeck UI.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// If you want job execution to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("executionEnabled")]
        public Input<bool>? ExecutionEnabled { get; set; }

        /// <summary>
        /// The name of a group within the project in which to place the job.
        /// Setting this creates collapsable subcategories within the Rundeck UI's project job index.
        /// </summary>
        [Input("groupName")]
        public Input<string>? GroupName { get; set; }

        /// <summary>
        /// The log level that Rundeck should use for this job. Defaults to "INFO".
        /// </summary>
        [Input("logLevel")]
        public Input<string>? LogLevel { get; set; }

        /// <summary>
        /// The maximum number of threads to use to execute this job, which
        /// controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
        /// the nodes will be visited sequentially.
        /// </summary>
        [Input("maxThreadCount")]
        public Input<int>? MaxThreadCount { get; set; }

        /// <summary>
        /// The name of the job, used to describe the job in the Rundeck UI.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nodeFilterExcludePrecedence")]
        public Input<bool>? NodeFilterExcludePrecedence { get; set; }

        /// <summary>
        /// A query string using
        /// [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
        /// that defines which subset of the project's nodes will be used to execute this job.
        /// </summary>
        [Input("nodeFilterQuery")]
        public Input<string>? NodeFilterQuery { get; set; }

        [Input("notifications")]
        private InputList<Inputs.RundeckJobNotificationArgs>? _notifications;
        public InputList<Inputs.RundeckJobNotificationArgs> Notifications
        {
            get => _notifications ?? (_notifications = new InputList<Inputs.RundeckJobNotificationArgs>());
            set => _notifications = value;
        }

        [Input("options")]
        private InputList<Inputs.RundeckJobOptionArgs>? _options;
        public InputList<Inputs.RundeckJobOptionArgs> Options
        {
            get => _options ?? (_options = new InputList<Inputs.RundeckJobOptionArgs>());
            set => _options = value;
        }

        [Input("preserveOptionsOrder")]
        public Input<bool>? PreserveOptionsOrder { get; set; }

        /// <summary>
        /// The name of the project that this job should belong to.
        /// </summary>
        [Input("projectName", required: true)]
        public Input<string> ProjectName { get; set; } = null!;

        /// <summary>
        /// The name of the attribute that will be used to decide in which
        /// order the nodes will be visited while executing the job across multiple nodes.
        /// </summary>
        [Input("rankAttribute")]
        public Input<string>? RankAttribute { get; set; }

        /// <summary>
        /// Keyword deciding which direction the nodes are sorted in terms of
        /// the chosen `rank_attribute`. May be either "ascending" (the default) or "descending".
        /// </summary>
        [Input("rankOrder")]
        public Input<string>? RankOrder { get; set; }

        /// <summary>
        /// The jobs schedule in Unix crontab format
        /// </summary>
        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        /// <summary>
        /// Sets the job schedule to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("scheduleEnabled")]
        public Input<bool>? ScheduleEnabled { get; set; }

        /// <summary>
        /// Boolean determining if an empty node filter yields
        /// a successful result.
        /// </summary>
        [Input("successOnEmptyNodeFilter")]
        public Input<bool>? SuccessOnEmptyNodeFilter { get; set; }

        public RundeckJobArgs()
        {
        }
    }

    public sealed class RundeckJobState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean defining whether two or more executions of
        /// this job can run concurrently. The default is `false`, meaning that jobs will only run
        /// sequentially.
        /// </summary>
        [Input("allowConcurrentExecutions")]
        public Input<bool>? AllowConcurrentExecutions { get; set; }

        [Input("commandOrderingStrategy")]
        public Input<string>? CommandOrderingStrategy { get; set; }

        [Input("commands")]
        private InputList<Inputs.RundeckJobCommandGetArgs>? _commands;
        public InputList<Inputs.RundeckJobCommandGetArgs> Commands
        {
            get => _commands ?? (_commands = new InputList<Inputs.RundeckJobCommandGetArgs>());
            set => _commands = value;
        }

        /// <summary>
        /// Boolean defining whether Rundeck will continue to run
        /// subsequent steps if any intermediate step fails. Defaults to `false`, meaning that execution
        /// will stop and the execution will be considered to have failed.
        /// </summary>
        [Input("continueOnError")]
        public Input<bool>? ContinueOnError { get; set; }

        /// <summary>
        /// A longer description of the job, describing the job in the Rundeck UI.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// If you want job execution to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("executionEnabled")]
        public Input<bool>? ExecutionEnabled { get; set; }

        /// <summary>
        /// The name of a group within the project in which to place the job.
        /// Setting this creates collapsable subcategories within the Rundeck UI's project job index.
        /// </summary>
        [Input("groupName")]
        public Input<string>? GroupName { get; set; }

        /// <summary>
        /// The log level that Rundeck should use for this job. Defaults to "INFO".
        /// </summary>
        [Input("logLevel")]
        public Input<string>? LogLevel { get; set; }

        /// <summary>
        /// The maximum number of threads to use to execute this job, which
        /// controls on how many nodes the commands can be run simulateneously. Defaults to 1, meaning that
        /// the nodes will be visited sequentially.
        /// </summary>
        [Input("maxThreadCount")]
        public Input<int>? MaxThreadCount { get; set; }

        /// <summary>
        /// The name of the job, used to describe the job in the Rundeck UI.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nodeFilterExcludePrecedence")]
        public Input<bool>? NodeFilterExcludePrecedence { get; set; }

        /// <summary>
        /// A query string using
        /// [Rundeck's node filter language](http://rundeck.org/docs/manual/node-filters.html#node-filter-syntax)
        /// that defines which subset of the project's nodes will be used to execute this job.
        /// </summary>
        [Input("nodeFilterQuery")]
        public Input<string>? NodeFilterQuery { get; set; }

        [Input("notifications")]
        private InputList<Inputs.RundeckJobNotificationGetArgs>? _notifications;
        public InputList<Inputs.RundeckJobNotificationGetArgs> Notifications
        {
            get => _notifications ?? (_notifications = new InputList<Inputs.RundeckJobNotificationGetArgs>());
            set => _notifications = value;
        }

        [Input("options")]
        private InputList<Inputs.RundeckJobOptionGetArgs>? _options;
        public InputList<Inputs.RundeckJobOptionGetArgs> Options
        {
            get => _options ?? (_options = new InputList<Inputs.RundeckJobOptionGetArgs>());
            set => _options = value;
        }

        [Input("preserveOptionsOrder")]
        public Input<bool>? PreserveOptionsOrder { get; set; }

        /// <summary>
        /// The name of the project that this job should belong to.
        /// </summary>
        [Input("projectName")]
        public Input<string>? ProjectName { get; set; }

        /// <summary>
        /// The name of the attribute that will be used to decide in which
        /// order the nodes will be visited while executing the job across multiple nodes.
        /// </summary>
        [Input("rankAttribute")]
        public Input<string>? RankAttribute { get; set; }

        /// <summary>
        /// Keyword deciding which direction the nodes are sorted in terms of
        /// the chosen `rank_attribute`. May be either "ascending" (the default) or "descending".
        /// </summary>
        [Input("rankOrder")]
        public Input<string>? RankOrder { get; set; }

        /// <summary>
        /// The jobs schedule in Unix crontab format
        /// </summary>
        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        /// <summary>
        /// Sets the job schedule to be enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("scheduleEnabled")]
        public Input<bool>? ScheduleEnabled { get; set; }

        /// <summary>
        /// Boolean determining if an empty node filter yields
        /// a successful result.
        /// </summary>
        [Input("successOnEmptyNodeFilter")]
        public Input<bool>? SuccessOnEmptyNodeFilter { get; set; }

        public RundeckJobState()
        {
        }
    }
}