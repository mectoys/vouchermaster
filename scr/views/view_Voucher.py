from flask import render_template, Blueprint
from scr.models.model_Voucher import model_Voucher


main = Blueprint('voucher_bp',__name__)

@main.route('/list_voucher')
def get_Vouchers():
    vouchers=model_Voucher.get_Vouchers()

    return render_template('/voucher/voucher_list.html',vouchers=vouchers, use_datatables=True)