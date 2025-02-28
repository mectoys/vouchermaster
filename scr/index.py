from flask import Flask, render_template
from database.connectDB import get_connection

from models.model_bank import  model_bank
from models.model_fpago import  model_fpago
from models.modelo_beneficiario import model_Beneficiario
app =Flask(__name__)

@app.route('/')
def principal():
   name=[]
   for i in range(0,5):
       name.append(i)

   benef= model_Beneficiario.get_beneficiario("Proveedores")
   for ben in benef:
       print(ben['Nombres'])
   #get_connection()



   return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

