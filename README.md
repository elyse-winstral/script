# Welcome

The idea behind this repo is to combine Markdown and Marimo to create a script with accessible (and editable) code snippets.

## Contents

- `Conditional_Probability.md` and `Conditional_Expectation.md`: Markdown versions of selected parts of the lecture notes. The vision is to have all of the lecture notes compiled into such Markdown files.
- `docs/*.py` and `docs/*.html`: Marimo notebooks with interactive visualizations, both as source files and HTML exports.


## Intended Use

- **Students** open the [repository](https://github.com/elyse-winstral/script) on GitHub, view markdown files, and chat about them with GitHub Copilot. They can also interact with Marimo notebooks, alas not directly on GitHub. Instead, they must open the notebooks on [GitHub pages](https://elyse-winstral.github.io/script/), which renders the contents of the `docs` folder.
- **Teachers** clone the repository and edit the Markdown files and Marimo notebooks. The Marimo notebooks can also be run locally (see setup below).


## Setup

Setup:
```bash
git clone https://github.com/elyse-winstral/script.git
cd script
uv sync
```
Working with Marimo notebooks:
```bash
uv run marimo edit docs/notebook.py
```
Exporting Marimo Notebooks to HTML:
```bash
uv run marimo export html docs/notebook.py --self-contained -o docs/notebook.html
```
