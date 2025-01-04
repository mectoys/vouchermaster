from flask import Flask, render_template
from database.connectDB import get_connection

from models.model_bank import  model_bank
from models.model_fpago import  model_fpago

app =Flask(__name__)

@app.route('/')
def principal():
   name=[]
   for i in range(0,5):
       name.append(i)


   #get_connection()

   fpagos= model_fpago.get_fpago()
   for fpago in fpagos:
       print(fpago)

   return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

