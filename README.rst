============
flask-phantom-emoji
============
Use Phantom Open Emoji in your Flask Apps!

------------
Installation
------------
::

    pip install flask-phantom-emoji

-----
Usage
-----
::

    from flask import Flask
    from flask_phantom_emoji import PhantomEmoji
    
    app = Flask(__name__)
    PhantomEmoji(app)


::

    <html>
    <body>
        {{ content | phantom }}
    </body>
    </html>
