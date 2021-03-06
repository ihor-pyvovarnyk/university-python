from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required, current_identity

from lab6 import db_utils
from lab6.middlewares import (
    db_lifecycle,
    only_admin_access,
    only_target_authorized_user_access_or_admin,
)
from lab6.models import Users, Wallets, Transactions
from lab6.schemas import (
    UserData,
    ListUsersRequest,
    UserToCreate,
    UserToUpdate,
    StatusResponse,
    WalletData,
    WalletToCreate,
    WalletToUpdate, TransactionData, FundsToSend,
)

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/user", methods=["GET"])
@jwt_required()
@only_admin_access
@db_lifecycle
def list_users():
    args = ListUsersRequest().load(request.args)
    users = db_utils.list_users(
        args.get("email"), args.get("first_name"), args.get("last_name")
    )
    return jsonify(UserData(many=True).dump(users))


@api_blueprint.route("/user", methods=["POST"])
@jwt_required()
@only_admin_access
@db_lifecycle
def create_user():
    user_data = UserToCreate().load(request.json)
    user = db_utils.create_entry(Users, **user_data)
    return jsonify(UserData().dump(user))


@api_blueprint.route("/user/<int:user_id>", methods=["GET"])
@jwt_required()
@only_target_authorized_user_access_or_admin
@db_lifecycle
def get_user_by_id(user_id):
    user = db_utils.get_entry_by_uid(Users, user_id)
    return jsonify(UserData().dump(user))


@api_blueprint.route("/user/<int:user_id>", methods=["PUT"])
@jwt_required()
@only_target_authorized_user_access_or_admin
@db_lifecycle
def update_user(user_id):
    user_data = UserToUpdate().load(request.json)
    user = db_utils.get_entry_by_uid(Users, user_id)
    db_utils.update_entry(user, **user_data)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/user/<int:user_id>", methods=["DELETE"])
@jwt_required()
@only_target_authorized_user_access_or_admin
@db_lifecycle
def delete_user(user_id):
    db_utils.delete_entry(Users, user_id)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/wallet", methods=["GET"])
@jwt_required()
@db_lifecycle
def list_wallets():
    if current_identity.is_admin:
        wallets = db_utils.list_wallets()
    else:
        wallets = db_utils.list_wallets(Wallets.owner_uid == current_identity.id)
    return jsonify(WalletData(many=True).dump(wallets))


@api_blueprint.route("/wallet", methods=["POST"])
@jwt_required()
@db_lifecycle
def create_wallet():
    wallet_data = WalletToCreate().load(request.json)
    wallet = db_utils.create_entry(
        Wallets, **wallet_data, owner_uid=current_identity.id, funds=0
    )
    return jsonify(WalletData().dump(wallet))


@api_blueprint.route("/wallet/<int:wallet_id>", methods=["GET"])
@jwt_required()
@db_lifecycle
def get_wallet_by_id(wallet_id):
    wallet = db_utils.get_entry_by_uid(
        Wallets, wallet_id, owner_uid=current_identity.id
    )
    return jsonify(WalletData().dump(wallet))


@api_blueprint.route("/wallet/<int:wallet_id>", methods=["PUT"])
@jwt_required()
@db_lifecycle
def update_wallet(wallet_id):
    wallet_data = WalletToUpdate().load(request.json)
    wallet = db_utils.get_entry_by_uid(Wallets, wallet_id, owner_uid=current_identity.id)
    db_utils.update_entry(wallet, **wallet_data)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/wallet/<int:wallet_id>", methods=["DELETE"])
@jwt_required()
@db_lifecycle
def delete_wallet(wallet_id):
    wallet = db_utils.get_entry_by_uid(
        Wallets, wallet_id, owner_uid=current_identity.id
    )
    db_utils.delete_entry(Wallets, wallet.uid)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/wallet/<int:wallet_id>/send-funds", methods=["POST"])
@jwt_required()
@db_lifecycle
def send_funds(wallet_id):
    transaction_data = FundsToSend().load(request.json)

    if wallet_id != 0 and not current_identity.is_admin:
        from_wallet = db_utils.get_entry_by_uid(
            Wallets, wallet_id, owner_uid=current_identity.id
        )
        assert from_wallet.funds > transaction_data["amount"], "Not enough funds"
        db_utils.update_entry(
            from_wallet,
            funds=Wallets.funds - transaction_data["amount"],
            commit=False,
        )

    to_wallet = db_utils.get_entry_by_uid(Wallets, transaction_data["to_wallet"])
    db_utils.update_entry(
        to_wallet,
        funds=Wallets.funds + transaction_data["amount"],
        commit=False,
    )

    transaction = db_utils.create_entry(
        Transactions,
        from_wallet_uid=wallet_id or None,
        to_wallet_uid=transaction_data["to_wallet"],
        amount=transaction_data["amount"],
    )
    return jsonify(TransactionData().dump(transaction))


@api_blueprint.route("/wallet/<int:wallet_id>/transactions", methods=["GET"])
@jwt_required()
@db_lifecycle
def list_wallet_transactions(wallet_id):
    transactions = db_utils.list_transactions_for_wallet(
        current_identity.id, wallet_id
    )
    return jsonify(TransactionData(many=True).dump(transactions))
