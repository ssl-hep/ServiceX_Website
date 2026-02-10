# ServiceX Documentation Guidelines (V1)

As per the nature of the project ServiceX has a lot of different documentations. In order to improve the user experience as well as the developer experience this document outlines some guidelines that should be followed when working on the documentation. The first part of these guidelines will be technical, these will cover the actual development of the docs and how to setup the projects in the correct way to match the rest. The second part of the guidelines will editorial, these will cover how to structure and write the actual documentation content.

## Technical Guidelines

### Sphinx/Furo and Using Markdown

For all ServiceX projects the Sphinx framework should be used to build the documentation. The Furo theme should be used on top of the Sphinx frame work. Both `sphinx` and `furo` can be installed with pip. To install the Furo theme into Sphinx put this line in the conf.py:

```
html_theme = "furo"
```

By default Sphinx uses .rst files. For ease of the developers `myst_parser` can be used in order to allow for .md files to be use. This is required for all ServiceX documentation. 'myst_parser' can be install using pip and setup in the conf.py:

```
extensions = [
    "myst_parser",
]
```

### Documentation Location and Structure

The docs for each project should be located in the repo of the code for that project. They should be located in a docs directory in the root of the repo.

Within that directory there should be a source directory where the markdown files and configurations are stored. This is the standard for sphinx documentation. The make files should be in the root of docs/.

### pyproject.toml

Each pyproject.toml should have a docs dependency list to allow for easy development. Because DocTest will be setup for all docs it is important that this list includes everything that is required to build the docs, but doesn't need the doc test libraries because a test area should be made for that. This list could look like this:

```
docs = [
    "sphinx",
    "furo",
    "myst_parser",
]
```

### .gitignore

Likely for development you will be using a local version. To prevent grossness in the main repo please add this to the .gitignore:

```
docs/source/build/
```

### Add tryservicex.org Navigation Bar

In order to add the tryservicex.org navigation bar to the documentation a template has to be added to the docs. Here are the steps for adding this:

Start by adding the required css and js files to the config. We will also add the templates directory:

```
templates_path = ['_templates']

html_css_files = [
    ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css', {'crossorigin': 'anonymous'}),
    ('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css', {'crossorigin': 'anonymous'}),
    ('https://tryservicex.org/css/navbar.css', {'crossorigin': 'anonymous'}),
    ('https://tryservicex.org/css/sphinx.css', {'crossorigin': 'anonymous'}),
]

html_js_files = [
    ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js', 
        {'integrity': 'sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI', 'crossorigin': 'anonymous'}
    ),
]

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/scroll-start.html",
        "sidebar/scroll-end.html",
    ]
}

```

Next create a _templates folder in the source directory and then create a page.html file inside the _templates dir. The last bit of code removes the search bar from the docs. This is because there is a search bar for the entire website and the small ones confuse the user. Inside the page.html file add the following code:

```
{% extends "!page.html" %}
{% block body %}
<script>

    fetch('https://raw.githubusercontent.com/ssl-hep/ServiceX_Website/main/site/navbar.html')
        .then(res => res.text())
        .then(html => {
            document.getElementById('navbar').innerHTML = html;

            // Initialize dropdown hover behavior after navbar is loaded
            const dropdowns = document.querySelectorAll('.navbar .dropdown');

            dropdowns.forEach(dropdown => {
                dropdown.addEventListener('mouseenter', function() {
                    const toggle = this.querySelector('.dropdown-toggle');
                    const menu = this.querySelector('.dropdown-menu');

                    if (window.innerWidth > 992) { // Only on desktop (lg breakpoint)
                        menu.classList.add('show');
                        toggle.setAttribute('aria-expanded', 'true');
                    }
                });

                dropdown.addEventListener('mouseleave', function() {
                    const toggle = this.querySelector('.dropdown-toggle');
                    const menu = this.querySelector('.dropdown-menu');

                    menu.classList.remove('show');
                    toggle.setAttribute('aria-expanded', 'false');
                });
            });

            // Still initialize Bootstrap for click/mobile
            if (typeof bootstrap !== 'undefined') {
                var dropdownElementList = document.querySelectorAll('.dropdown-toggle');
                var dropdownList = Array.from(dropdownElementList).map(function (dropdownToggleEl) {
                    return new bootstrap.Dropdown(dropdownToggleEl);
                });
            }
        });
</script>

<div id="navbar"></div>

<div id="wrapper">
{{ super() }}
</div>
{% endblock %}
```

This code overrides the default template in Sphinx and Furo allowing for the navbar to be added. The navbar is hosted in the ServiceX_Website repo as well as the styles required. We then load them from the files hosted on github. This means to make changes to the navbar or styles required for this to work you need to make those changes into the ServiceX_Website repo. The file /css/sphinx.css is specifically used to make some small changes to the Sphinx/Furo css to allow the navbar to be integrated seamlessly.

### Publishing Docs

There are two ways that we expect to publish ServiceX docs. Most docs will be included in the tryservicex.org website. These docs must be published through this repo. The docs not included in the website can be published through their own GitHub pages deployment.

To publish the docs on the website you will need to update the github action in this repo. Add some code similar to this changing the important details as needed. You will need to checkout the repo and then build it:

```
  - name: Checkout FuncADL Docs
    uses: actions/checkout@v4
    with:
        repository: iris-hep/func_adl
        path: funcadl
        token: ${{ secrets.GITHUB_TOKEN }}
        sparse-checkout: docs
        sparse-checkout-cone-mode: true
  - name: Build FuncADL Sphinx documentation
    working-directory: funcadl/docs
    run: sphinx-build -b html ./ build/html
```
You will also need to add code to the two following blocks to make it so that the built files are added to the website directory:

```
  - name: Assemble site
    run: |
        mkdir -p site/challenge/
        cp -r 15minhist/build/html/* site/challenge/
        mkdir -p site/guide
        cp -r client/docs/build/html/* site/guide/
        mkdir -p site/funcadl
        cp -r funcadl/docs/build/html/* site/funcadl/
        mkdir -p site/utils
        cp -r utils/docs/build/html/* site/utils/
  - name: Local act Clean Up
    if: ${{ env.ACT }}
    run: |
        rm -rf 15minhist/build/
        rm -rf client/
        rm -rf funcadl/
        rm -rf utils/
        rm =*
```

This should allow for the code to be built and added to the website. The last step is to add links to the docs in the navbar.html file.

If you would like to deploy the docs not in connection to the website you can use this code:

```
name: Deploy Sphinx documentation to Pages

on:
  push:
    branches: [master] # branch to trigger deployment
  workflow_dispatch:

jobs:
  pages:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    permissions:
      pages: write
      id-token: write
    steps:
    - name: pip install
      run: pip install furo myst_parser
    - id: deployment
      uses: sphinx-notes/pages@v3
```