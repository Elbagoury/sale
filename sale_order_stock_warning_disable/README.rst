.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================================
Disabled Stock Level Warning for Sale Orders
============================================

* Removes the "You plan to sell X but you only have Y available!" warning when choosing an out-of-stock product on a Sale Order Line

Installation
============
* Just install this module

Configuration
=============
* No configuration needed

Usage
=====
\- 

Known issues / Roadmap
======================
* Note that in 8.0 the stock warning generation is bundled inside SO line's product onchange. This module suppresses warnings from that onchange and therefore could suppress warnings provided by other custom modules.

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.