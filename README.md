# Amazon Category Explorer (ACE)
This repo contains the source code for my final project in CS744 (Visualization) at UW-Madison in Fall 2020: Amazon Category Explorer (ACE)

Some details:
- `all-nodes.csv` is the product category data given for the project. It's a bit old, from 2014 I believe.
- `data-to-json.py` is a python script which converts the `all-nodes.csv` to a JSON tree structure which is used by the app.
- Run `python3 data-to-json.py > tree.json` to (re)generate the JSON data for the app.
- `index.html` is the main app page.
- `about.html` has some background information about the project.

The app is [available online](https://tomreitz.github.io/amazon-category-explorer/).
