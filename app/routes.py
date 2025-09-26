import os
from flask import Blueprint, jsonify, render_template

from app.controllers.plan import create_plan, get_day_plans, get_month_plans
from app.controllers.user import login, register

main_bp = Blueprint("main", __name__)
@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/register", methods=["POST"])
def register_user():
    return jsonify(register())

@main_bp.route("/login", methods=["POST"])
def login_user():
    return jsonify(login())

@main_bp.route("/plans", methods=["POST"])
def add_plan():
    return jsonify(create_plan())

@main_bp.route("/month_plans", methods=["GET"])
def month_plan():
    return jsonify(get_month_plans())

@main_bp.route("/today_plans", methods=["GET"])
def today_plan():
    return jsonify(get_day_plans())