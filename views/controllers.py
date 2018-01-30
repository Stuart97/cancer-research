"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 12 January, 2018 @ 4:25 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from views import app, back


@app.route('/')
@back.anchor
def index():
    return render_template('index.html')


@app.route('/about/')
@back.anchor
def about():
    return render_template('about.html')


@app.route('/classification/')
@back.anchor
def classification():
    return render_template('classification.html')


@app.route('/contact/')
@back.anchor
def contact():
    return render_template('contact.html')
