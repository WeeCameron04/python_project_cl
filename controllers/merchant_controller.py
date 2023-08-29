from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repo as merchant_repo

merchant_blueprint = Blueprint("merchants", __name__)

@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repo.select_all() # NEW
    return render_template("merchnats/index.html", merchants = merchants)

@merchant_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repo.select(id)
    return render_template("merchants/show.html", merchant=merchant)