# hiperwalk.org

The Hiperwalk website is built with [Hugo static site generator](https://gohugo.io/) and uses the [scientific-python-hugo-theme](https://github.com/scientific-python/scientific-python-hugo-theme).

## Build

The build is automatically started every time a new commit on the `main` branch is made. After the build is complete, the site is served through GitHub Pages.

The GitHub Actions workflow that does that is described in the `.github/workflows/gh-pages-deployment.yml` file.

Instructions to create and configure the SSH key pair used by the workflow are available in the [wiki](./wiki/Configuring-the-key-pair-for-the-automatic-build).
