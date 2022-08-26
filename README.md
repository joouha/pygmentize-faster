# Pygmentize Faster

This package uses [pygments-cache](https://github.com/xonsh/pygments-cache) to run `pygmentize` just a little bit faster.

It overrides the `pygmentize` script provided by `pygments`.

## Benkmarks

`pygmentize-faster` runs about twice as fast as `pygmentize`:

```bash

$ time fd -d1 -j1 '.py$' -x python -m pygmentize {} > /dev/null ';' /usr/lib/python3.10
user=65.25s system=7.81s cpu=98% total=1:14.45

$ time fd -d1 -j1 '.py$' -x python -m pygmentize_faster {} > /dev/null ';' /usr/lib/python3.10
user=33.61s system=4.96s cpu=99% total=38.663

```
