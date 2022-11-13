==========
How to use
==========


Installation
============

.. code-block:: python

   pip install zipfile-inflate64


Usage
=====

Anywhere in a Python codebase:

.. code-block:: python

   import zipfile_inflate64  # This has the side effect of patching the zipfile module to support Enhanced Deflate


Alternatively, ``zipfile_inflate64`` re-exports the ``zipfile`` API, as a convenience:

.. code-block:: python

   import zipfile_inflate64 as zipfile

   zipfile.ZipFile(...)



Dependency
==========

Zipfile-inflate64 depends ``inflate64`` python library.
