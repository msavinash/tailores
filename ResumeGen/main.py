from flask import Flask, Response
from io import BytesIO
from pdfGen import generate_print_pdf

app = Flask(__name__)

contact = {
        'name': 'Nicholas Depinet',
        'website': 'http://github.com/nickdepinet/',
        'email': 'depinetnick@gmail.com',
        'address': '3092 Nathaniel Rochester Hall, Rochester, NY 14623',
        'phone': '(614)365-1089'
    }
    
data = {
        'objective': ' '.join(['Seeking co-operative employment',
                    'in the field of software development,',
                    'preferably working in python and web backend infrastructure or distributed computing, ',
                    'to start June 2016.']),
        'summary': ' '.join(['I love to use programming to solve interesting problems.',
                    'I love working in Python (which is why I generated this resume in Python using ReportLab), but I am comfortable working in a variety of languages.',
                    'I am currently exploring the exciting world of distributed and cloud computing, and love to discuss the unique opportunities this type of computing presents.']),
        'education': '<br/>'.join(['<b>Rochester Insitute of Technology</b>',
                    '<b>B.S.</b>  Computer Science',
                    '<b>Expected Graduation</b>  2017']),
        'skills': '<br/>'.join(['<b>Languages</b>  Python, Java, C#, C, MIPS Assembly, Bash, jQuery, HTML, CSS',
                    '<b>Tools</b>  Git/Mercurial, Vim, Django, Tornado, Twisted, Autobahn, ReportLab',
                    '<b>Platforms</b>  Linux (Debian, RHEL), OSX, Windows',
                    '<b>Services</b>  Microsoft Application Insights, MySQL, PostgreSQL, MongoDB, Apache/Nginx, HAProxy, Gunicorn']),
        'experience': [''.join(['<b>Microsoft</b> - Redmond, WA<br/>',
                    '<alignment=TA_RIGHT>Software Engineer Intern: May - August 2015</alignment><br/>',
                    'Designed and developed a distributed testing framework to allow for the execution of ',
                    'the principals of testing in production of Windows 10 Universal Apps across many devices.',
                    'Development done in C#, using Microsoft Application Insights as a data backend.<br/>']),
                    ''.join(['<b>Nebula</b> - Seattle, WA<br/>',
                    '<alignment=TA_RIGHT>Software Development Intern, Control Plane: June - August 2014</alignment><br/>',
                    'Developed improvements to the initial installation Out-of-box experience (OOBE) of the Nebula One product. ',
                    'Development done in python.<br/>']),
                    ''.join(['<b>SpkrBar</b> - Columbus, OH<br/>',
                    '<alignment=TA_RIGHT>Software Developer: September - December 2013</alignment><br/>',
                    'Developed and maintained the front and backend of a startup website using Python and the Django framework. ',
                    'The website allows technical conferences, speakers, and attendees to connect and keep up to date. ']),
                    ''.join(['<b>Olah Healthcare</b> - Columbus, OH<br/>',
                    '<alignment=TA_RIGHT>Software Engineering Intern: May - August 2013</alignment><br/>',
                    'Developed a web application using Python and the Django framework ',
                    'to allow hospitals to easily store, search, and retrieve archived medical records. ',
                    'Primary Responsibility was the design and implementation of the metadata storage backend, and search functionality.']),
                    ''.join(['<b>Computer Science House</b> - Rochester, NY<br/>',
                    'Drink Administrator: February 2013 - Present<br/>',]),
                    ''.join(['<b>STI-Healthcare</b> - Columbus, OH<br/>',
                    'Network & Server Administration Intern: May - August 2012<br/>',])],
        'projects': [
                    ''.join(['<b>Hangman</b> - http://github.com/nickdepinet/hangman<br/>',
                    'Implemented a command line hangman game engine and an artifical intelligence player in python.',
                    'The AI uses letter frequencies from the english dictionary and additionally word frequencies from the ',
                    'Google corpus make intelligent guesses as to the next letter.']),
                    ''.join(['<b>g()(\'al\')</b> - http://github.com/eatnumber1/goal<br/>',
                    'Completed the first python solution to the g()(\'al\') programming challenge. ',
                    'The "goal" of the g()(\'al\') challenge is to enable the calling of g()(\'al\') in the source of the ',
                    'language of choice with n ()\'s, and to be returned the string "goal" with the appropriate number of "o"s.']),
                    ''.join(['<b>DrinkPi</b> - http://github.com/jeid64/drinkpi/<br/>',
                    'Worked with a partner to replace a failing component in the Computer Science House drink machines. ',
                    'The software controlling the machines was previously written in java and running on Dallas TINI microcomputers. ',
                    'These TINI\'s were failing and were no longer produced, so we re-wrote the software in python to run on a ',
                    'Raspberry Pi. The software talks to the drink server over sockets using the SUNDAY protocol, and to the drink ',
                    'machine hardware using the 1-Wire protocol and a usb 1-Wire bus master.']),
                    ''.join(['<b>TempMon</b> - http://github.com/nickdepinet/tempmon/<br/>',
                    'Implemented a temperature monitoring system for a server room using a Raspberry Pi. ',
                    'The system monitors temperature using a series of DSB1820 temperature sensors. ',
                    'When the temperature exceeds a set limit, an email notification is sent. ',
                    'The software, including temperature reading, threading, and email notification is written in python.']),
                    ''.join(['<b>Nexus Q Development</b> - http://github.com/nickdepinet/android_device_google_steelhead<br/>'])]}



@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    
    # Create an in-memory PDF
    pdf_buffer = BytesIO()
    generate_print_pdf(pdf_buffer, data, contact)

    # Serve the generated PDF as a response
    pdf_buffer.seek(0)
    response = Response(pdf_buffer.read(), content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
    return response



if __name__ == "__main__":
    app.run()