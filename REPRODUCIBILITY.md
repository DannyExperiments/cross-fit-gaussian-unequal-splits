# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay verifies 150 fold log-likelihood identities and 400 balanced exponent factorizations by exact rational arithmetic. It checks both finite expectation certificates, compares the limiting slopes at 61 sample sizes, and brackets the unequal-split intercept using a rational series for log 2. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/cross-fit-balls-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font parameters. [Build the paper](paper/BUILD.md).
