Red Text Explainer
==================

This is a generator for an updated version of Ezeith's BL2 mod "Red text
explainer."  Ezeith will be uploading it on their account in a bit, but
I wanted to store the code that I'd used for it in here.

It's a little bit clunkier than the TPS Red Text Explainer mod that I
put together, but is largely the same.

The actual mod itself is not stored here -- check Ezeith's areas (github
and Nexus) for the compiled, downloadable mod.

Mod Construction / Implementation Details
=========================================

*(This section is only relevant for someone looking to edit the mod in the
same way I do, or just someone curious about my mod construction techniques.
If you're just looking to run the mod, see the "Usage" section above.  The
mod can, of course, be edited directly in BLCMM as well, once it's
been imported.)*

This mod is generated using a Python script named `generate-mod.py`,
which makes use of some data classes from my [FT/BLCMM Explorer](https://github.com/apocalyptech/ft-explorer)
project.  You'll need to copy (or symlink, if you're on Linux or OSX) that
project's `resources` and `ftexplorer` dirs into this one, to run the
generation script.  The script also makes use of `modprocessor.py` from my
main BL2 mods directory, so copy (or symlink) that as well.

License
=======

The `generate-mod.py` script is licensed under the
[3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).
