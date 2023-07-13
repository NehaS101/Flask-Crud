from flask import Blueprint, render_template, request
from controllers.crud_controller import (
    create,
    read,
    update,
    delete,
    hello,
    greet,
    farewell
)

# Create a Blueprint for the CRUD routes
crud_router = Blueprint('crud', __name__)


crud_router.route('/')(hello)

crud_router.route('/greet/<username>')(greet)

crud_router.route('/farewell/<username>')(farewell)

crud_router.route('/read')(read)

crud_router.route('/create', methods=['POST'])(create)

crud_router.route('/update/<int:id>', methods=['PATCH'])(update)

crud_router.route('/delete/<int:id>', methods=['DELETE'])(delete)
