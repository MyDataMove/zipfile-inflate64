# zipfile-inflate64

Extract Enhanced Deflate ZIP archives with Python's `zipfile` API.

## Installation
```bash
pip install zipfile-inflate64
```

## Usage
Anywhere in a Python codebase:
```python
import zipfile_inflate64  # This has the side effect of patching the zipfile module to support Enhanced Deflate
```

Alternatively, `zipfile_inflate64` re-exports the `zipfile` API, as a convenience:
```python
import zipfile_inflate64 as zipfile

zipfile.ZipFile(...)
...
```

## Design Rationale

### The Problem
Recent versions of Microsoft Windows Explorer
[use Deflate64 compression when creating ZIP files larger than 2GB](https://github.com/dotnet/runtime/issues/17802#issuecomment-231808916).
With the ubiquity of Windows and the ease of using "Sent to compressed folder", a majority of newly-created large
ZIP files use Deflate64 compression.

### Solution
Python package [inflate64](https://pypi.org/project/inflate64/) provide compression(deflate) and decompression(inflate)
by Enhanced Deflate, aka Deflate64, procedure.

To manage ZIP archive extraction operations, the Python standard library
[zipfile](https://docs.python.org/3/library/zipfile.html) module provides the essential features and is already
ubiquitous in availability and usage. However, zipfile is difficult to extend, as it hardcodes many conditionals for
compression formats and does not provide capabilities for easily augmenting or replacing parts of it. Monkey-patching
can overcome some of these problems, and the promise of a drop-in, API-compatible patch to a standard library module
outweighed the engineering benefits of basing a solution off a more naturally extensible third-party ZIP manipulation
package.

### History

Zipfile-deflate64 realize extraction of zipfile compressed with DEFLATE64(tm) algorithm by binding with infback9
extension in zlib.

zipfile-inflate64 is a fork that use inflate64 python package to realize compress and decompress of archives.

## Copyright

zipfile-deflate64 is authored by Kitware, Inc.
zipfile-inflate64 is authored by Hiroshi Miura.
