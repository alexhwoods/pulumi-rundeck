// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Rundeck.Outputs
{

    [OutputType]
    public sealed class RundeckJobNotificationPlugin
    {
        /// <summary>
        /// Map of arbitrary configuration properties for the selected plugin.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Config;
        /// <summary>
        /// The name of the plugin to use.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private RundeckJobNotificationPlugin(
            ImmutableDictionary<string, object>? config,

            string type)
        {
            Config = config;
            Type = type;
        }
    }
}
