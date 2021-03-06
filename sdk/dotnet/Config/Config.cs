// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;

namespace Pulumi.Rundeck
{
    public static class Config
    {
        private static readonly Pulumi.Config __config = new Pulumi.Config("rundeck");
        /// <summary>
        /// API Version of the target Rundeck server.
        /// </summary>
        public static string? ApiVersion { get; set; } = __config.Get("apiVersion");

        /// <summary>
        /// Auth token to use with the Rundeck API.
        /// </summary>
        public static string? AuthToken { get; set; } = __config.Get("authToken");

        /// <summary>
        /// URL of the root of the target Rundeck server.
        /// </summary>
        public static string? Url { get; set; } = __config.Get("url");

    }
}
