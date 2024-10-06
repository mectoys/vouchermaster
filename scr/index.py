from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def principal():
   name=[]
   for i in range(0,5):
       name.append(i)
   return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

