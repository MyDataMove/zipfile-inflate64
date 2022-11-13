=================
zipfile-inflate64
=================

.. image:: https://dev.azure.com/miurahr/CodeBerg/_apis/build/status/CodeBerg-zipfile-inflate64-CI?branchName=releases
    :target: https://dev.azure.com/miurahr/CodeBerg
    :alt: Test Status

.. image:: https://readthedocs.org/projects/zipfile-inflate64/badge/?version=latest
    :target: https://zipfile-inflate64.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Extract Enhanced Deflate ZIP archives with Python's ``zipfile`` API.

Installation
============

.. code-block:: python

   pip install zipfile-inflate64


Usage
=====

Anywhere in a Python codebase:

.. code-block:: python

   import zipfile_inflate64  # This has the side effect of patching the zipfile module to support Enhanced Deflate


Alternatively, `zipfile_inflate64` re-exports the `zipfile` API, as a convenience:

.. code-block:: python

   import zipfile_inflate64 as zipfile

   zipfile.ZipFile(...)


Design Rationale
================

The Problem
-----------

Recent versions of Microsoft Windows Explorer
[use Deflate64 compression when creating ZIP files larger than 2GB](https://github.com/dotnet/runtime/issues/17802#issuecomment-231808916).
With the ubiquity of Windows and the ease of using "Sent to compressed folder", a majority of newly-created large
ZIP files use Deflate64 compression.

Solution
--------

Python package [inflate64](https://pypi.org/project/inflate64/) provide compression(deflate) and decompression(inflate)
by Enhanced Deflate, aka Deflate64, procedure.

To manage ZIP archive extraction operations, the Python standard library
[zipfile](https://docs.python.org/3/library/zipfile.html) module provides the essential features and is already
ubiquitous in availability and usage. However, zipfile is difficult to extend, as it hardcodes many conditionals for
compression formats and does not provide capabilities for easily augmenting or replacing parts of it. Monkey-patching
can overcome some of these problems, and the promise of a drop-in, API-compatible patch to a standard library module
outweighed the engineering benefits of basing a solution off a more naturally extensible third-party ZIP manipulation
package.

History
-------

Zipfile-deflate64 realize extraction of zipfile compressed with DEFLATE64(tm) algorithm by binding with infback9
extension in zlib.

zipfile-inflate64 is a fork that use inflate64 python package to realize compress and decompress of archives.

Copyright & License
===================

zipfile-inflate64 is distributed under GNU General Public License Version 3.0 or (in your choice) later.

zipfile-deflate64 is distributed under Apache-2.0 license.
which authored by Kitware, Inc.
