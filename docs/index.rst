.. Iriskit documentation master file, created by
   sphinx-quickstart on Sun Sep  2 11:53:26 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Iriskit's documentation!
===================================

Client (and possibly server framework) implementing the Internet Registry
Information Service (IRIS) protocol.

The initial revision will support enough of `RFC 3981`_ (IRIS), `RFC 3982`_
(the IRIS 'dreg' type), and `RFC 4993`_ (the IRIS-LWZ transport protocol) to
support `RFC 5144`_ (DCHK), at least for writing a dchk client library.

It is not as yet intended that any support be added for `S-NAPTR`_-based
service discovery initially. That will come later.

.. _RFC 3981: http://tools.ietf.org/html/rfc3981
.. _RFC 3982: http://tools.ietf.org/html/rfc3982
.. _RFC 4993: http://tools.ietf.org/html/rfc4993
.. _RFC 5144: http://tools.ietf.org/html/rfc5144
.. _S-NAPTR: http://tools.ietf.org/html/rfc3958

.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

