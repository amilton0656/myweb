#!/bin/bash

# Caminho base
PROJECT_PATH="/var/www/myweb"
PROJECT_NAME="core"
DOMAIN_NAME="amilton.com.br"

# Atualiza sistema e instala pacotes
sudo apt update
sudo apt install -y python3-venv python3-dev apache2 libapache2-mod-wsgi-py3 apache2-dev build-essential

# Cria venv (caso não exista)
cd $PROJECT_PATH
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Ativa e instala dependências
source venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
else
  pip install django
fi

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Permissões
sudo chown -R www-data:www-data $PROJECT_PATH
sudo chmod -R 755 $PROJECT_PATH

# Gera config do mod_wsgi se necessário
WSGI_CONFIG=$(mod_wsgi-express module-config)
if ! grep -q "mod_wsgi" /etc/apache2/apache2.conf; then
  echo "Adicionando mod_wsgi no apache2.conf..."
  echo "$WSGI_CONFIG" | sudo tee -a /etc/apache2/apache2.conf > /dev/null
fi

# Cria arquivo core.conf
CONF_FILE="/etc/apache2/sites-available/core.conf"
sudo tee $CONF_FILE > /dev/null <<EOF
<VirtualHost *:80>
    ServerName $DOMAIN_NAME
    ServerAdmin webmaster@localhost

    DocumentRoot $PROJECT_PATH

    Alias /static $PROJECT_PATH/static
    <Directory $PROJECT_PATH/static>
        Require all granted
    </Directory>

    <Directory $PROJECT_PATH/$PROJECT_NAME>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess $PROJECT_NAME python-home=$PROJECT_PATH/venv python-path=$PROJECT_PATH
    WSGIProcessGroup $PROJECT_NAME
    WSGIScriptAlias / $PROJECT_PATH/$PROJECT_NAME/wsgi.py

    ErrorLog \${APACHE_LOG_DIR}/core_error.log
    CustomLog \${APACHE_LOG_DIR}/core_access.log combined
</VirtualHost>
EOF

# Ativa o site e reinicia o Apache
sudo a2ensite core.conf
sudo a2enmod wsgi
sudo systemctl restart apache2

echo "✅ Deploy finalizado. Acesse: http://$DOMAIN_NAME ou via IP público."
