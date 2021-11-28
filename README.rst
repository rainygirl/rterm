=====
Rterm
=====

Rterm is Twitter / RSS reader client for CLI(Command Line Interface).
Rterm requires Python version 3.5 and above.


----------
Screenshot
----------

.. image:: https://raw.githubusercontent.com/rainygirl/rterm/master/screenshot.gif

---------------
Getting Started
---------------


Try it with::

    pip3 install rterm
    rterm

You can clone the git repo::

    git clone https://github.com/rainygirl/rterm
    cd rterm
    python3 setup.py install
    rterm

You may need to get your own Twitter consumer key (API key) and consumer secret key. Go to `https://dev.twitter.com/apps/new <https://dev.twitter.com/apps/new>`_ and copy to terminal.

---------
RSS feeds
---------

You can add/modify RSS feeds on src/config.py


-------------
Shortcut keys
-------------

* [H], [?] : Help
* [Up], [Down], [W], [S], [J], [K] : Select from list
* [Shift]+[Up], [Shift]+[Down], [PgUp], [PgDn] : Quickly select from list
* [Space] : Open attached image or URL
* [O] : Open canonical link
* [:] : Select by typing a number from list
* [Tab], [Shift]+[Tab] : Change the category tab
* [Q], [Ctrl]+[C] : Quit


------------
Contributing
------------

Feel free to fork & contribute!


-------
License
-------

Rterm is released under the MIT license.


-------
Credits
-------

* `Lee JunHaeng aka rainygirl <https://rainygirl.com/>`_.


