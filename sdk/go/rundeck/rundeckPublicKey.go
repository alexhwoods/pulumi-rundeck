// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rundeck

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The public key resource allows SSH public keys to be stored into Rundeck's key store.
// The key store is where Rundeck keeps credentials that are needed to access the nodes on which
// it runs commands.
//
// This resource also allows the retrieval of an existing public key from the store, so that it
// may be used in the configuration of other resources such as ``awsKeyPair``.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-rundeck/sdk/go/rundeck"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := rundeck.NewRundeckPublicKey(ctx, "anvils", &rundeck.RundeckPublicKeyArgs{
// 			KeyMaterial: pulumi.String("ssh-rsa yada-yada-yada"),
// 			Path:        pulumi.String("anvils/id_rsa.pub"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type RundeckPublicKey struct {
	pulumi.CustomResourceState

	// True if the key should be deleted when the resource is deleted.
	// Defaults to true if keyMaterial is provided in the configuration.
	Delete pulumi.BoolOutput `pulumi:"delete"`
	// The public key string to store, serialized in any way that is accepted
	// by OpenSSH. If this is not included, ``keyMaterial`` becomes an attribute that can be used
	// to read the already-existing key material in the Rundeck store.
	KeyMaterial pulumi.StringOutput `pulumi:"keyMaterial"`
	// The path within the key store where the key will be stored. By convention
	// this path name normally ends with ".pub" and otherwise has the same name as the associated
	// private key.
	Path pulumi.StringOutput `pulumi:"path"`
	// The URL at which the key material can be retrieved from the key store by other clients.
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewRundeckPublicKey registers a new resource with the given unique name, arguments, and options.
func NewRundeckPublicKey(ctx *pulumi.Context,
	name string, args *RundeckPublicKeyArgs, opts ...pulumi.ResourceOption) (*RundeckPublicKey, error) {
	if args == nil || args.Path == nil {
		return nil, errors.New("missing required argument 'Path'")
	}
	if args == nil {
		args = &RundeckPublicKeyArgs{}
	}
	var resource RundeckPublicKey
	err := ctx.RegisterResource("rundeck:index/rundeckPublicKey:RundeckPublicKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRundeckPublicKey gets an existing RundeckPublicKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRundeckPublicKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RundeckPublicKeyState, opts ...pulumi.ResourceOption) (*RundeckPublicKey, error) {
	var resource RundeckPublicKey
	err := ctx.ReadResource("rundeck:index/rundeckPublicKey:RundeckPublicKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RundeckPublicKey resources.
type rundeckPublicKeyState struct {
	// True if the key should be deleted when the resource is deleted.
	// Defaults to true if keyMaterial is provided in the configuration.
	Delete *bool `pulumi:"delete"`
	// The public key string to store, serialized in any way that is accepted
	// by OpenSSH. If this is not included, ``keyMaterial`` becomes an attribute that can be used
	// to read the already-existing key material in the Rundeck store.
	KeyMaterial *string `pulumi:"keyMaterial"`
	// The path within the key store where the key will be stored. By convention
	// this path name normally ends with ".pub" and otherwise has the same name as the associated
	// private key.
	Path *string `pulumi:"path"`
	// The URL at which the key material can be retrieved from the key store by other clients.
	Url *string `pulumi:"url"`
}

type RundeckPublicKeyState struct {
	// True if the key should be deleted when the resource is deleted.
	// Defaults to true if keyMaterial is provided in the configuration.
	Delete pulumi.BoolPtrInput
	// The public key string to store, serialized in any way that is accepted
	// by OpenSSH. If this is not included, ``keyMaterial`` becomes an attribute that can be used
	// to read the already-existing key material in the Rundeck store.
	KeyMaterial pulumi.StringPtrInput
	// The path within the key store where the key will be stored. By convention
	// this path name normally ends with ".pub" and otherwise has the same name as the associated
	// private key.
	Path pulumi.StringPtrInput
	// The URL at which the key material can be retrieved from the key store by other clients.
	Url pulumi.StringPtrInput
}

func (RundeckPublicKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*rundeckPublicKeyState)(nil)).Elem()
}

type rundeckPublicKeyArgs struct {
	// The public key string to store, serialized in any way that is accepted
	// by OpenSSH. If this is not included, ``keyMaterial`` becomes an attribute that can be used
	// to read the already-existing key material in the Rundeck store.
	KeyMaterial *string `pulumi:"keyMaterial"`
	// The path within the key store where the key will be stored. By convention
	// this path name normally ends with ".pub" and otherwise has the same name as the associated
	// private key.
	Path string `pulumi:"path"`
}

// The set of arguments for constructing a RundeckPublicKey resource.
type RundeckPublicKeyArgs struct {
	// The public key string to store, serialized in any way that is accepted
	// by OpenSSH. If this is not included, ``keyMaterial`` becomes an attribute that can be used
	// to read the already-existing key material in the Rundeck store.
	KeyMaterial pulumi.StringPtrInput
	// The path within the key store where the key will be stored. By convention
	// this path name normally ends with ".pub" and otherwise has the same name as the associated
	// private key.
	Path pulumi.StringInput
}

func (RundeckPublicKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rundeckPublicKeyArgs)(nil)).Elem()
}