from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
   return 'hello world - /hello'

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route("/template")
def template_test():
    return render_template('template.html', my_name="senthil", my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


def hello_jesus_world():
   return 'Hello Jesus World'

if __name__ == '__main__':
   app.add_url_rule('/jesus', 'jesus', hello_jesus_world)
   app.run()