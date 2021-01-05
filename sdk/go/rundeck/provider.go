// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rundeck

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The provider type for the rundeck package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil || args.ApiVersion == nil {
		return nil, errors.New("missing required argument 'ApiVersion'")
	}
	if args == nil || args.AuthToken == nil {
		return nil, errors.New("missing required argument 'AuthToken'")
	}
	if args == nil || args.Url == nil {
		return nil, errors.New("missing required argument 'Url'")
	}
	if args == nil {
		args = &ProviderArgs{}
	}
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:rundeck", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// API Version of the target Rundeck server.
	ApiVersion string `pulumi:"apiVersion"`
	// Auth token to use with the Rundeck API.
	AuthToken string `pulumi:"authToken"`
	// URL of the root of the target Rundeck server.
	Url string `pulumi:"url"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// API Version of the target Rundeck server.
	ApiVersion pulumi.StringInput
	// Auth token to use with the Rundeck API.
	AuthToken pulumi.StringInput
	// URL of the root of the target Rundeck server.
	Url pulumi.StringInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}
