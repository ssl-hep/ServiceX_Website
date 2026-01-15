# ServiceX Website

This repository contains the ServiceX website, which is hosted at [tryservicex.org](https://tryservicex.org).  
The website provides a landing page for new users and a convenient way for existing users to access references, documentation, and resources.

---

## 15-Minute Histogram Challenge

As part of onboarding, ServiceX includes the 15-Minute Histogram Challenge.  
The goal of this challenge is to guide users from installing ServiceX to producing a full histogram in under 15 minutes.

The challenge is implemented as Sphinx documentation stored in this repository.  
Documentation is automatically built when the GitHub Action for updating the website is run.  

Markdown is used for the docs to simplify editing. If you need to add sections you are unsure about, feel free to reach out or open an issue.

---

## Repository Structure

- `15minhist/` — Sphinx documentation for the 15-Minute Histogram Challenge.
- `docs/` — HTML pages that contain iframes linking to the different ServiceX documentation.
- `img/` — Images used on the website (e.g., logo, figures).

---

## Contributing

We welcome contributions! Here’s how you can help:

1. **Update the 15-Minute Histogram Challenge**

   To edit or test the challenge locally:

   - Install the required Python packages:

     ```bash
     pip install sphinx myst_parser furo
     ```

   - Navigate to the `15minhist/` folder and build the docs:

     ```bash
     make html
     ```

     This generates a `build/` directory containing an `index.html`.

   - You can view the generated documentation by either:
     - Opening `build/index.html` directly in your browser, or  
     - Using a VSCode Live Server extension.

   For more information on editing or building Sphinx documentation, see the [Sphinx Quickstart Guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

2. **Update the Website**

   Modify HTML, CSS, or JS in `website/` for styling, layout, or functionality improvements.  
   The documentation pages are linked through iframes. For more information on iframes, see the [W3Schools iframe guide](https://www.w3schools.com/tags/tag_iframe.ASP).

3. **Report Issues**

   Use GitHub Issues to report bugs, broken links, or unclear instructions.

---

## Deployment

The website is automatically built and deployed via GitHub Actions. When changes are pushed to the main branch:

1. Sphinx documentation in `15minhist/` is built.
2. The static website in `website/` is updated with the latest docs and assets.
3. The site is deployed to [tryservicex.org](https://tryservicex.org).

---
