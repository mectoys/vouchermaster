from flask import Flask, render_template
from database.connectDB import get_connection
from models.model_bank import  model_bank
from models.model_fpago import  model_fpago
from models.modelo_beneficiario import model_Beneficiario
from models.model_Voucher import model_Voucher
from scr.views import view_Voucher

app =Flask(__name__)

@app.route('/')
def principal():
   name=[]
   for i in range(0,5):
       name.append(i)

   vals= model_Voucher.get_Vouchers()
   print(vals)
   for val in vals:
       print('')
   #get_connection()
   return render_template('index.html')


if __name__ == '__main__':
    app.register_blueprint(view_Voucher.main,url_prefix='/')
    app.run(debug=True)



