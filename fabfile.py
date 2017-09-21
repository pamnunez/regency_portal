from fabric.api import lcd, local

def prepare_deployment(branch_name):
    local('python manage.py test regency_portal')
    local('git add -p && git commit')

def deploy():
    with lcd('/c/Users/Home/django/regency_portal'):
    	local('git pull /c/Users/Home/dev/regency_portal')

