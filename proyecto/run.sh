#!/bin/bash

python3 app.py &

#Para iniciar Apache en primer plano
apache2ctl -D FOREGROUND
