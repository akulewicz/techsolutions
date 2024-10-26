from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import ContactForm
from flask_mail import Mail, Message

mail = Mail(app)


def prepare_email(form):
    subject = "Zapytanie o usługę"
    sender = "dev@kula.usermd.net"
    recipients = ["a.kulewicz@gmail.com"]
    
    html = f"""<html><strong>Nadawca:</strong> {form.firstname.data} {form.lastname.data} <br>
            <strong>E-mail:</strong> {form.email.data} <br>
            <strong>Firma:</strong> { form.company.data } <br>
            <strong>Treść:<br></strong> {form.details.data }</html>"""

    msg = Message(subject=subject, sender=sender, recipients=recipients, html=html)
    return msg


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        msg = prepare_email(form)
        mail.send(msg)
        flash("Wiadomość została wysłana. Dziękujemy za za kontakt", "success")
        return redirect(url_for("home"))
    return render_template("home.html", form=form)


@app.route("/onas")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404