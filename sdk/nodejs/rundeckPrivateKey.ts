// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The private key resource allows SSH private keys to be stored into Rundeck's key store.
 * The key store is where Rundeck keeps credentials that are needed to access the nodes on which
 * it runs commands.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as rundeck from "@pulumi/rundeck";
 *
 * const anvils = new rundeck.RundeckPrivateKey("anvils", {
 *     keyMaterial: fs.readFileSync("/id_rsa", "utf-8"),
 *     path: "anvils/id_rsa",
 * });
 * ```
 */
export class RundeckPrivateKey extends pulumi.CustomResource {
    /**
     * Get an existing RundeckPrivateKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RundeckPrivateKeyState, opts?: pulumi.CustomResourceOptions): RundeckPrivateKey {
        return new RundeckPrivateKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'rundeck:index/rundeckPrivateKey:RundeckPrivateKey';

    /**
     * Returns true if the given object is an instance of RundeckPrivateKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RundeckPrivateKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RundeckPrivateKey.__pulumiType;
    }

    /**
     * The private key material to store, serialized in any way that is
     * accepted by OpenSSH.
     */
    public readonly keyMaterial!: pulumi.Output<string>;
    /**
     * The path within the key store where the key will be stored.
     */
    public readonly path!: pulumi.Output<string>;

    /**
     * Create a RundeckPrivateKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RundeckPrivateKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RundeckPrivateKeyArgs | RundeckPrivateKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RundeckPrivateKeyState | undefined;
            inputs["keyMaterial"] = state ? state.keyMaterial : undefined;
            inputs["path"] = state ? state.path : undefined;
        } else {
            const args = argsOrState as RundeckPrivateKeyArgs | undefined;
            if (!args || args.keyMaterial === undefined) {
                throw new Error("Missing required property 'keyMaterial'");
            }
            if (!args || args.path === undefined) {
                throw new Error("Missing required property 'path'");
            }
            inputs["keyMaterial"] = args ? args.keyMaterial : undefined;
            inputs["path"] = args ? args.path : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RundeckPrivateKey.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RundeckPrivateKey resources.
 */
export interface RundeckPrivateKeyState {
    /**
     * The private key material to store, serialized in any way that is
     * accepted by OpenSSH.
     */
    readonly keyMaterial?: pulumi.Input<string>;
    /**
     * The path within the key store where the key will be stored.
     */
    readonly path?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RundeckPrivateKey resource.
 */
export interface RundeckPrivateKeyArgs {
    /**
     * The private key material to store, serialized in any way that is
     * accepted by OpenSSH.
     */
    readonly keyMaterial: pulumi.Input<string>;
    /**
     * The path within the key store where the key will be stored.
     */
    readonly path: pulumi.Input<string>;
}
