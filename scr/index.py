from flask import Flask, render_template
from database.connectDB import get_connection
from models.model_Voucher import get_Vouchers
from models.model_bank import  model_bank

app =Flask(__name__)

@app.route('/')
def principal():
   name=[]
   for i in range(0,5):
       name.append(i)

   #get_Vouchers()
   #get_connection()
   banks= model_bank.get_bank()
   for bank in banks:
       print(bank)
   return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

