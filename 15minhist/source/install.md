Install and Initialize ServiceX
=================================

## Setup Python Virtual Environment

Using a Python virtual environment is recommended to avoid conflicts with existing packages and to keep your ServiceX setup isolated.

If you are unfamiliar with virtual environments, you can learn more in the [Python documentation](https://docs.python.org/3/library/venv.html).

You can also create and manage virtual environments directly in VSCode. Instructions for this can be found in the [VSCode documentation](https://code.visualstudio.com/docs/python/environments).


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

We will also want to install some packages use for the analysis:

```
pip install awkward matplotlib
```

## Initialize ServiceX

Now that everything is installed, you need to connect your client to an Analysis Facility. This step authenticates your environment and sets up the required access. To begin, run the following command:

```
servicex init
```

Running this command will launch a setup wizard that guides you through configuring your ServiceX client. After selecting your analysis facility, the wizard will provide a link to a sign-in page. On that page, click the Sign in with ATLAS option.

```{image} imgs/setup-login.png
:width: 300px
:alt: Sign-in screen
```

After completing the ATLAS sign-in, open the second link provided by the wizard. On this page, click the button to copy your authentication token:

```{image} imgs/setup-token.png
:width: 300px
:alt: Token copy button example
```

Paste this token into the command line when prompted. The wizard will verify that your client is successfully configured. Once verification is complete, you will be asked to choose a downloads directory. For this tutorial, simply press Enter to accept the default location.

If the setup completes successfully, you will see a message stating Configuration Complete. Once you see this message, you may proceed to the next step.