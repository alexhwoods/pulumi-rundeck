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
    public sealed class RundeckJobNotificationEmail
    {
        public readonly bool? AttachLog;
        public readonly ImmutableArray<string> Recipients;
        public readonly string? Subject;

        [OutputConstructor]
        private RundeckJobNotificationEmail(
            bool? attachLog,

            ImmutableArray<string> recipients,

            string? subject)
        {
            AttachLog = attachLog;
            Recipients = recipients;
            Subject = subject;
        }
    }
}
