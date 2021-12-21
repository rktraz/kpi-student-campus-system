from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func
from datetime import datetime
from . import db
import json
from .models import Dormitory, Resident, Faculty, Payment

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    dormitories_all = Dormitory.query.with_entities(
        Dormitory.number,
        Dormitory.address) \
        .order_by(Dormitory.number) \
        .all()
    residents_per_dormitory = db.session.query(
        Resident.dormitory_id,
        func.count(Resident.id)) \
        .group_by(Resident.dormitory_id) \
        .order_by(Resident.dormitory_id) \
        .all()
    popular_faculty = db.session.query(
        Resident.dormitory_id,
        func.mode().within_group(
            Resident.faculty_id)) \
        .group_by(Resident.dormitory_id) \
        .all()
    faculties_dict = dict(
        db.session.query(Faculty.id, Faculty.name) \
            .order_by(Faculty.id) \
            .all()
    )

    return render_template("home.html",
                           user=current_user,
                           dormitories_residents_faculties_zip=zip(
                               dormitories_all,
                               residents_per_dormitory,
                               popular_faculty),
                           faculties_dict=faculties_dict
                           )


@views.route('/dormitory_info', methods=['GET', 'POST'])
@login_required
def dormitory_info():
    popular_faculty = db.session.query(
        Resident.dormitory_id,
        func.mode().within_group(
            Resident.faculty_id)) \
        .group_by(Resident.dormitory_id) \
        .all()

    with db.engine.connect() as con:
        residents_all = con.execute(
            'SELECT * FROM residents WHERE residents.dormitory_id = {}'.format(current_user.id))
        number_of_residents = con.execute(
            'SELECT COUNT(*) FROM residents WHERE residents.dormitory_id = {}'.format(current_user.id))
        max_floor = con.execute(
            'SELECT MAX(room) FROM residents WHERE residents.dormitory_id = {}'.format(current_user.id))
        paid_status_query = list(con.execute(
            """SELECT residents.id, payments.month_payed
               FROM residents
               INNER JOIN payments ON residents.id=payments.resident_id           
               WHERE residents.dormitory_id = {}""".format(current_user.id))
        )

    paid_status = list()
    for record in paid_status_query:
        record = list(record)
        paid_status.append(record[1] in (12, 1, 2, 3))
    faculties_dict = dict(
        db.session.query(Faculty.id, Faculty.name) \
            .order_by(Faculty.id) \
            .all()
    )

    residents_paid_status_zipped = zip(residents_all, paid_status)
    number_of_residents = (list(number_of_residents)[0][0])
    max_floor = str(list(max_floor)[0][0])[0]
    number_of_debtors = len(paid_status) - sum(paid_status)
    return render_template("dormitory_info.html",
                           user=current_user,
                           residents_paid_status_zipped=residents_paid_status_zipped,
                           number_of_debtors=number_of_debtors,
                           number_of_residents=number_of_residents,
                           faculties_dict=faculties_dict,
                           popular_faculty=popular_faculty,
                           max_floor=max_floor
                           )


@views.route('/payments', methods=['GET', 'POST'])
@login_required
def payments():
    dates = list()
    months = list()
    payer_emails = list()

    with db.engine.connect() as con:
        residents_dict = dict(list(con.execute(
            'SELECT id, email FROM residents WHERE residents.dormitory_id = {}'.format(current_user.id))
        ))

        payments_time_month_payer_id = list(con.execute(
            """SELECT payments.time, payments.month_payed, payments.resident_id
               FROM payments 
               INNER JOIN residents ON payments.resident_id=residents.id
               WHERE residents.dormitory_id = {}
               ORDER BY payments.time DESC""".format(current_user.id))
        )

    months_dict = {1: 'January',
                   2: 'February',
                   3: 'March',
                   4: 'April',
                   5: 'May',
                   6: 'June',
                   7: 'July',
                   8: 'August',
                   9: 'September',
                   10: 'October',
                   11: 'November',
                   12: 'December'}

    for record in payments_time_month_payer_id:
        record = list(record)
        dates.append(record[0].strftime("%d.%m.%Y, %H:%M:%S"))
        months.append(months_dict[record[1]])
        payer_emails.append(residents_dict[record[2]])

    return render_template("payments.html",
                           user=current_user,
                           dates=dates,
                           months=months,
                           payer_emails=payer_emails,
                           length=len(dates)
                           )
