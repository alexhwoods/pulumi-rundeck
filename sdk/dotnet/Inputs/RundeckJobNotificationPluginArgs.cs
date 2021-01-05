// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Rundeck.Inputs
{

    public sealed class RundeckJobNotificationPluginArgs : Pulumi.ResourceArgs
    {
        [Input("config")]
        private InputMap<object>? _config;

        /// <summary>
        /// Map of arbitrary configuration properties for the selected plugin.
        /// </summary>
        public InputMap<object> Config
        {
            get => _config ?? (_config = new InputMap<object>());
            set => _config = value;
        }

        /// <summary>
        /// The name of the plugin to use.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public RundeckJobNotificationPluginArgs()
        {
        }
    }
}
