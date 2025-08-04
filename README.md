# fastpeek
This is a tool for quickly peeking at a git repository.

sometimes just seeing the changes in a file is more convenient than the CLI and I often found myself running those commands manually and removing files after, this is why I made this tool :

## How to get it running:

```bash
git clone https://github.com/Davis-3450/fastpeek
cd fastpeek
```

I highly recommend using uv to install the tool.

```bash
uv tool install -e . # install as a tool with uv
```
but you can also use pip.

```bash
pip install -e .
```


## How to use

Simply run the tool in the root of the repository you want to peek at!

This will automatically make the following files:

* diff.diff (to be implemented)
* log.txt
* status.txt
