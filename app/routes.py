from app import app, db
from app.models import Hosts
from flask import request, render_template


@app.route('/')
def home():
    return 'Hello world!!!'


@app.route('/inventory/api', methods=['POST'])
# @auth.login_required
def inventory_api():
    # {'hostname': 'debian-11', 'hostid': '27518fa5e15440aaa3cb6510c78680e6', 'kernel': '5.10.0-21-amd64', 'distro': 'Debian', 'release': 'Debian GNU/Linux 11 (bullseye)', 'version': '11.6', 'host_ip': '192.168.1.63'}
    payload = request.get_json()
    hostname = payload['hostname']
    hostid = payload['hostid']
    kernel = payload['kernel']
    distro = payload['distro']
    release = payload['release']
    version = payload['version']
    host_ip = payload['host_ip']

    qhostname = Hosts.query.filter_by(host_name=hostname).first()
    qhostid = Hosts.query.filter_by(host_name=hostid).first()

    app.logger.debug(payload)

    if qhostname is None and qhostid is None:
        msg = f'Host {hostname} cadastrado'
        app.logger.debug('Host não cadastrado')
        host = Hosts(
            host_name=hostname,
            host_id=hostid,
            host_kernel=kernel,
            host_distro=distro,
            host_release=release,
            host_version=version,
            host_ip=host_ip
        )
        db.session.add(host)
        db.session.commit()
    elif qhostid is not None:
        msg = f'Host {hostname} atualizado'
        app.logger.debug('Host mudou de nome')
        qhostid.host_name = hostname
        db.session.add(qhostid)
        db.session.commit()
    else:
        msg = f'Host {hostname} existe'
        app.logger.debug('Host existe')
    return f'{msg}\n'


@app.route('/hosts', methods=['GET'])
def list_hosts():
    hosts = Hosts.query.all()
    return render_template('hosts.html', hosts=hosts)

