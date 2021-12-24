from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
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


# this route is for inserting data to mysql database via html forms
@views.route('/add_new_resident', methods=['GET', 'POST'])
@login_required
def add_new_resident():
    print(request.form)
    print(request.form.values())
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    room = request.form['room']
    course = request.form['course']
    group = request.form['group']
    faculty_id = request.form['faculty_id']
    dormitory_id = current_user.id

    faculties_dict = {
        "IAT": 1,
        "IEE": 2,
        "IMZ": 3,
        "IASA": 4,
        "ISZZI": 5,
        "ITS": 6,
        "FBMI": 7,
        "FBT": 8,
        "FEA": 9,
        "FEL": 10,
        "FIOT": 11,
        "FL": 12,
        "FMM": 13,
        "FPM": 14,
        "FSP": 15
    }

    if type(faculty_id) == str:
        faculty_id = faculties_dict[faculty_id]
    new_resident = Resident(
                            first_name=first_name, last_name=last_name,
                            email=email, room=room, course=course,
                            group=group, faculty_id=faculty_id,
                            dormitory_id=dormitory_id
                            )
    db.session.add(new_resident)
    db.session.commit()
    db.session.add(Payment(
        month_payed=datetime.now().month,
        resident_id=Resident.query.filter(Resident.email == new_resident.email).first().id
    ))
    db.session.commit()

    print(Resident.query.filter(Resident.email == new_resident.email).first(), new_resident.email)

    flash("Resident was inserted successfully!")

    return redirect(url_for('views.dormitory_info'))


# this is our update route where we are going to update our employee
@views.route('/update_info_about_resident', methods=['GET', 'POST'])
@login_required
def update_info_about_resident():
    print(request.form)
    resident_to_update = Resident.query.get(request.form.get('resident_id'))

    resident_to_update.first_name = request.form['first_name']
    resident_to_update.last_name = request.form['last_name']
    resident_to_update.email = request.form['email']
    resident_to_update.room = request.form['room']
    resident_to_update.course = request.form['course']
    resident_to_update.group = request.form['group']
    resident_to_update.faculty_id = request.form['faculty_id']

    db.session.commit()
    flash("Resident was updated successfully.")

    return redirect(url_for('views.dormitory_info'))


# This route is for deleting our employee
@views.route('/delete/<resident_id>/', methods=['GET', 'POST'])
@login_required
def delete(resident_id):
    payment_to_delete = Payment.query.filter(Payment.resident_id == resident_id).first()
    db.session.delete(payment_to_delete)
    resident_to_delete = Resident.query.get(resident_id)
    db.session.delete(resident_to_delete)
    db.session.commit()
    flash("Resident was deleted successfully.")

    return redirect(url_for('views.dormitory_info'))
