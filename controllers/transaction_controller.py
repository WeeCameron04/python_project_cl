from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transactions import Transactions
import repositories.transactions_repo as transaction_repo
import repositories.tag_repo as tag_repo
import repositories.merchant_repo as merchant_repo

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repo.select_all() # NEW
    return render_template("transaction/index.html", transactions = transactions)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_task():
    tags = transaction_repo.select_all()
    merchants = transaction_repo.select_all()
    return render_template("transactions/new.html", tags = tags, merchants = merchants)

@transactions_blueprint.route("/visits",  methods=['POST'])
def create_task():
    tag_id = request.form['tag_id']
    merchant_id = request.form['merchant_id']
    review = request.form['review']
    tag = tag_repo.select(tag_id)
    location = merchant_repo.select(merchant_id)
    transactions = Transactions(tag, location, review)
    transaction_repo.save(transactions)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_task(id):
    transaction_repo.delete(id)
    return redirect('/transactions')