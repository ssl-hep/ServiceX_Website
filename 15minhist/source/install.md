Install and Initialize ServiceX
=================================

## Install Required Packages

This tutorial uses two Python packages.

The first is the ServiceX client, which provides the core functionality needed to interact with ServiceX. You can install it using `pip`:


```
pip install servicex
```

The second package contains a collection of analysis utility functions that simplify common ServiceX workflows and reduce boilerplate code:


```
pip install servicex-analysis-utils
```

The `servicex-analysis-utils` package is useful well beyond this tutorial and can be integrated directly into your own analyses. It provides many helper functions that make working with ServiceX more convenient and efficient.

## Initialize ServiceX

Now that everything is installed you need to connect your client to an Analysis Facility. This step authenticates your environment and sets up access. To do this you can run this command:

```
servicex init atlas
```

You'll be promted to log in via a provided link. Once authenticated you should see a success message. You can confirm the setup by running:

```
servicex init test
```