import os
import pkg_resources

from flask import Blueprint, url_for, Markup

def PhantomEmoji(app, **kwargs):
  """Phantom Emoji Factory"""
  return _PhantomEmoji.init_app(app, **kwargs)

class _PhantomEmoji(object):

  @classmethod
  def init_app(self, app, url_prefx='/phantom', emoji_class='phantom-icon'):
    # Config

    # Get phantom names
    phantom_images_path = pkg_resources.resource_filename(
      __package__,
      'PhantomOpenEmoji/emoji/',
    )
    names = list(map(lambda s: os.path.splitext(s)[0],
                filter(lambda s: s.endswith('.svg'),
                       os.listdir(phantom_images_path))))

    phantom = Blueprint(
      'phantom',
      __name__,
      static_folder='PhantomOpenEmoji/emoji',
      static_url_path='',
    )
    app.register_blueprint(phantom, url_prefix=url_prefx)

    # Jinja filter
    @app.template_filter('phantom')
    def phantom_filter(s, height='auto'):
      splits = s.split(':')
      splits_len = len(splits)
      out = ''
      for i, w in enumerate(splits):
        if w in names:
          out = out[:-1]
          out += '<img src="%s" alt="%s" class="%s" height="%s">' % (
            url_for('phantom.static',
                    filename='%s.svg' % w),
            w,
            emoji_class,
            height,
          )
        elif i + 1 < splits_len:
          out += w + ':'
        else:
          out += w

      return Markup(out)
