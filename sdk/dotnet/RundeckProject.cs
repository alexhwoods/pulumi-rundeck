// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Rundeck
{
    public partial class RundeckProject : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of a plugin to use to run commands on
        /// nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
        /// nodes.
        /// </summary>
        [Output("defaultNodeExecutorPlugin")]
        public Output<string?> DefaultNodeExecutorPlugin { get; private set; } = null!;

        /// <summary>
        /// The name of a plugin to use to copy files onto
        /// nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
        /// to send files over SSH.
        /// </summary>
        [Output("defaultNodeFileCopierPlugin")]
        public Output<string?> DefaultNodeFileCopierPlugin { get; private set; } = null!;

        /// <summary>
        /// Description of the project to be shown in the Rundeck UI
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
        /// key names due to limitations in Terraform's config language.
        /// </summary>
        [Output("extraConfig")]
        public Output<ImmutableDictionary<string, object>?> ExtraConfig { get; private set; } = null!;

        /// <summary>
        /// The name of the project, used both in the UI and to uniquely identify
        /// the project. Must therefore be unique across a single Rundeck installation.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Nested block instructing Rundeck on how to determine the
        /// set of resources (nodes) for this project. The nested block structure is described below.
        /// </summary>
        [Output("resourceModelSources")]
        public Output<ImmutableArray<Outputs.RundeckProjectResourceModelSource>> ResourceModelSources { get; private set; } = null!;

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the type of SSH authentication to use. Defaults to `privateKey`.
        /// </summary>
        [Output("sshAuthenticationType")]
        public Output<string?> SshAuthenticationType { get; private set; } = null!;

        /// <summary>
        /// Like `ssh_key_storage_path` except that the key is read from
        /// the Rundeck server's local filesystem, rather than from the key store.
        /// </summary>
        [Output("sshKeyFilePath")]
        public Output<string?> SshKeyFilePath { get; private set; } = null!;

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the location within Rundeck's key store where the SSH private key can be found. Private
        /// keys can be uploaded to rundeck using the `rundeck.RundeckPrivateKey` resource.
        /// </summary>
        [Output("sshKeyStoragePath")]
        public Output<string?> SshKeyStoragePath { get; private set; } = null!;

        /// <summary>
        /// The URL of the index page for this project in the Rundeck UI.
        /// </summary>
        [Output("uiUrl")]
        public Output<string> UiUrl { get; private set; } = null!;


        /// <summary>
        /// Create a RundeckProject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RundeckProject(string name, RundeckProjectArgs args, CustomResourceOptions? options = null)
            : base("rundeck:index/rundeckProject:RundeckProject", name, args ?? new RundeckProjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RundeckProject(string name, Input<string> id, RundeckProjectState? state = null, CustomResourceOptions? options = null)
            : base("rundeck:index/rundeckProject:RundeckProject", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RundeckProject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RundeckProject Get(string name, Input<string> id, RundeckProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new RundeckProject(name, id, state, options);
        }
    }

    public sealed class RundeckProjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of a plugin to use to run commands on
        /// nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
        /// nodes.
        /// </summary>
        [Input("defaultNodeExecutorPlugin")]
        public Input<string>? DefaultNodeExecutorPlugin { get; set; }

        /// <summary>
        /// The name of a plugin to use to copy files onto
        /// nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
        /// to send files over SSH.
        /// </summary>
        [Input("defaultNodeFileCopierPlugin")]
        public Input<string>? DefaultNodeFileCopierPlugin { get; set; }

        /// <summary>
        /// Description of the project to be shown in the Rundeck UI
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("extraConfig")]
        private InputMap<object>? _extraConfig;

        /// <summary>
        /// Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
        /// key names due to limitations in Terraform's config language.
        /// </summary>
        public InputMap<object> ExtraConfig
        {
            get => _extraConfig ?? (_extraConfig = new InputMap<object>());
            set => _extraConfig = value;
        }

        /// <summary>
        /// The name of the project, used both in the UI and to uniquely identify
        /// the project. Must therefore be unique across a single Rundeck installation.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resourceModelSources", required: true)]
        private InputList<Inputs.RundeckProjectResourceModelSourceArgs>? _resourceModelSources;

        /// <summary>
        /// Nested block instructing Rundeck on how to determine the
        /// set of resources (nodes) for this project. The nested block structure is described below.
        /// </summary>
        public InputList<Inputs.RundeckProjectResourceModelSourceArgs> ResourceModelSources
        {
            get => _resourceModelSources ?? (_resourceModelSources = new InputList<Inputs.RundeckProjectResourceModelSourceArgs>());
            set => _resourceModelSources = value;
        }

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the type of SSH authentication to use. Defaults to `privateKey`.
        /// </summary>
        [Input("sshAuthenticationType")]
        public Input<string>? SshAuthenticationType { get; set; }

        /// <summary>
        /// Like `ssh_key_storage_path` except that the key is read from
        /// the Rundeck server's local filesystem, rather than from the key store.
        /// </summary>
        [Input("sshKeyFilePath")]
        public Input<string>? SshKeyFilePath { get; set; }

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the location within Rundeck's key store where the SSH private key can be found. Private
        /// keys can be uploaded to rundeck using the `rundeck.RundeckPrivateKey` resource.
        /// </summary>
        [Input("sshKeyStoragePath")]
        public Input<string>? SshKeyStoragePath { get; set; }

        public RundeckProjectArgs()
        {
        }
    }

    public sealed class RundeckProjectState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of a plugin to use to run commands on
        /// nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
        /// nodes.
        /// </summary>
        [Input("defaultNodeExecutorPlugin")]
        public Input<string>? DefaultNodeExecutorPlugin { get; set; }

        /// <summary>
        /// The name of a plugin to use to copy files onto
        /// nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
        /// to send files over SSH.
        /// </summary>
        [Input("defaultNodeFileCopierPlugin")]
        public Input<string>? DefaultNodeFileCopierPlugin { get; set; }

        /// <summary>
        /// Description of the project to be shown in the Rundeck UI
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("extraConfig")]
        private InputMap<object>? _extraConfig;

        /// <summary>
        /// Additional raw configuration parameters to include in the project configuration, with dots replaced with slashes in the
        /// key names due to limitations in Terraform's config language.
        /// </summary>
        public InputMap<object> ExtraConfig
        {
            get => _extraConfig ?? (_extraConfig = new InputMap<object>());
            set => _extraConfig = value;
        }

        /// <summary>
        /// The name of the project, used both in the UI and to uniquely identify
        /// the project. Must therefore be unique across a single Rundeck installation.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resourceModelSources")]
        private InputList<Inputs.RundeckProjectResourceModelSourceGetArgs>? _resourceModelSources;

        /// <summary>
        /// Nested block instructing Rundeck on how to determine the
        /// set of resources (nodes) for this project. The nested block structure is described below.
        /// </summary>
        public InputList<Inputs.RundeckProjectResourceModelSourceGetArgs> ResourceModelSources
        {
            get => _resourceModelSources ?? (_resourceModelSources = new InputList<Inputs.RundeckProjectResourceModelSourceGetArgs>());
            set => _resourceModelSources = value;
        }

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the type of SSH authentication to use. Defaults to `privateKey`.
        /// </summary>
        [Input("sshAuthenticationType")]
        public Input<string>? SshAuthenticationType { get; set; }

        /// <summary>
        /// Like `ssh_key_storage_path` except that the key is read from
        /// the Rundeck server's local filesystem, rather than from the key store.
        /// </summary>
        [Input("sshKeyFilePath")]
        public Input<string>? SshKeyFilePath { get; set; }

        /// <summary>
        /// When the SSH-based file copier and executor plugins are
        /// used, the location within Rundeck's key store where the SSH private key can be found. Private
        /// keys can be uploaded to rundeck using the `rundeck.RundeckPrivateKey` resource.
        /// </summary>
        [Input("sshKeyStoragePath")]
        public Input<string>? SshKeyStoragePath { get; set; }

        /// <summary>
        /// The URL of the index page for this project in the Rundeck UI.
        /// </summary>
        [Input("uiUrl")]
        public Input<string>? UiUrl { get; set; }

        public RundeckProjectState()
        {
        }
    }
}
