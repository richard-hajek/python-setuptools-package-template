# Project name

You may use this template to create Python packages quickly.

## Running the code

You have several options of running any source code you write. In any case, always source the venv before `source venv/bin/activate`

### Run as `__main__`

```bash
python main.py [args]
```

> This will work **if** you never import from any other directory than from the same one.
If you ever import a module from a different folder **this will not work**. 

### Run as module

```bash
python -m project_name.main [args]
```

> This method will correctly construct the Python library tree, so you can import from any directory you like

### Run as entrypoint

See [Full Installation](#Full-installation).

## Setup

### Minimal installation

- [ ] Clone this repo `https://github.com/richard-hajek/python-setuptools-package-template.git`
- [ ] Remove `.git` folder
- [ ] Run `make prepare`

### Full installation

- [ ] In your setup.cfg
  - [ ] Change install_requirements in `[options]` to fit your needs
  - [ ] Change console_scripts in `[options.entry_points]` to fit your needs ( or delete it )
- [ ] In your setup.cfg change `name`, `version`, `author`, `author_email`, `description`, `version`
- [ ] Add README
- [ ] Add LICENSE