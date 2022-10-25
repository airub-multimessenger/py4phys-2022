# Frequently (or not) Asked Questions


## How to download a file from GitHub?

[GitHub](github.com) is meant to store `git` *projects*. It is not really designed to store *files* as we know them. Since we do not know (yet) how to use `git` to properly interact with GitHub, we need to download everything manually:
- to download the entire repository as a `zip` archive, go to the [main page](https://github.com/airub-multimessenger/py4phys-2022) of the repository, and click *Code* -> *Download ZIP*
- to download a single file, navigate to the file and click on *Raw*, then save the page from your browser.

**Pro-tip (using git)**: if you already have basic experience with `git` (or you are feeling adventurous), you can just `git clone https://github.com/airub-multimessenger/py4phys-2022.git py4phys`. You can then enter the `py4phys` directory and run `git pull` whenever you want align the content with the online repository. We recommend you always make a copy before modifying a notebook, otherwise things can get messy!

## Jupyter or JupyterLab?

Depending on your installation, you may be propted to choose between *Jupyter* (Notebooks) or *JupyterLab*. Both are browser-based interfaces to a `python` interpreter (referred to as a *kernel*). JupyterLab is more featureful and more similar to an IDE (*integrated development environment*), but is also heavier and has a less polished interface (although this is subjective). It does not matter what you use, at this moment.

**Pro-tip / desktop IDE**: if you want a more advanced working environment, you may install an IDE of your choice. Microsoft [VS Code](https://code.visualstudio.com/) is nowadays very popular and can be set up to run Jupyter notebooks. While very useful when working with pure source code (`.py` files), for notebooks an IDE does not add much to the experience and can actually make things unnecessarily complicated, so beware.