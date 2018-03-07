=======
Progeny
=======

Simple (but powerful) management for complex class hierarchies

Examples
--------

Basic Usage
===========

.. code:: python

    from progeny import ProgenyBase


    class NotificationHandler(ProgenyBase):
        def send_message(self, *args, **kwargs):
            raise RuntimeError


    class CustomerOneNotificationHandler(NotificationHandler):
        def send_message(self, *args, **kwargs):
            # .. business logic ...


    class CustomerTwoNotificationHandler(NotificationHandler):
        def send_message(self, *args, **kwargs):
            # .. business logic ...

Now we can iterate over all of the subclasses of ``NotificationHandler``:

.. code:: python

    def send_newsletter():
        for handler in NotificationHandler.tracked_descendants():
            handler.send_message('Your attention, please!')

Omitting descendant classes
===========================

In some cases, it may be useful to prevent descendant classes from being visible to Progeny.

.. code:: python

    from progeny import ProgenyBase


    class NotificationHandler(ProgenyBase):
        def send_message(self, *args, **kwargs):
            raise RuntimeError


    class EmailNotificationHandler(NotificationHandler):
        __progeny_tracked__ = False

        def send_message(self, *args, **kwargs):
            # .. business logic ..


    class SmsNotificationHandler(NotificationHandler):
        __progeny_tracked__ = False

        def send_message(self, *args, **kwargs):
            # .. business logic ..


    class CustomerOneNotificationHandler(EmailNotificationHandler):
        pass


    class CustomerTwoNotificationHandler(SmsNotificationHandler):
        pass

Any classes with ``__progeny_tracked__`` set to a falsy value during class
construction will be ignored by Progeny. It's descendant classes are unaffected:

.. code:: python

    NotificationHandler.tracked_descendants()
    # {CustomerOneNotificationHandler, CustomerTwoNotificationHandler}

This can be especially handy to conditionally track subclasses based on config
context:

.. code:: python

    class CustomerFooNotificationHandler(EmailNotificationHandler):
        __progeny_tracked__ = config.get('CUSTOMER_FOO_ACTIVE')

Using the descendants registry
==============================

Progeny makes it easy to choose between descendant classes at runtime:

.. code:: python

    from progeny import ProgenyBase
    from my_app.users import UserLevel


    class UploadParser(ProgenyBase):
        pass


    class FreeUserUploadParser(UploadParser):
        __progeny_key__ = UserLevel.FREE

        def parse_upload(self, *args, **kwargs):
            # .. logic to parse the upload slowly, using shared resources


    class PremiumUserUploadParser(UploadParser):
        __progeny_key__ = UserLevel.PAID

        def parse_upload(self, *args, **kwargs):
            # .. logic to parse the upload immediately with dedicated resources

.. code:: python

    def parse_upload(data):
        UploadParser.get_progeny(session.user.level).parse_upload(data)
