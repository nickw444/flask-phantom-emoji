from flask import Flask, render_template_string
from flask_phantom_emoji import PhantomEmoji


app = Flask(__name__)
PhantomEmoji(app)


@app.route('/')
def index():
  return render_template_string("""
{{ s | phantom }}
{{ s | phantom(50) }}
{{ s | phantom(25) }}
{{ t | phantom }}
""", s=":smile:", t="""
  :drunk:
  :electric_light_bulb: :fearful_face:
  :heart: :snail: :family:
""")

app.run(debug=True)
