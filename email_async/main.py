from website import create_app
import yagmail
#from website import celery
#from website.celery import make_celery

from datetime import datetime, timedelta
now = datetime.now()

import yagmail

yag = yagmail.SMTP('testingcelery2021', 'Pyth0nC0d3r.2791')

app,celery = create_app()

#celery = make_celery(app)

@celery.task
def send_with_attachment(to, subject, content, attachment):
    yag.send(
        to=to,
        subject=subject,
        contents=content,
        attachments=attachment,
    )


@celery.task
def send_without_attachment(to, subject, content):
    yag.send(
        to=to,
        subject=subject,
        contents=content
    )

@app.route('/mailer', methods=['GET', 'POST'])
def mailer():
    email_to='testingcelery2021@gmail.com'

    send_without_attachment(
    email_to,
    'Celery Testing',
    'Esto es una envio desde flask con Celery'
    )
    
    return (f'Email has been Sent to: {email_to}')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
    
