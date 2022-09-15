pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'docker_django_adminSystem', url: 'https://github.com/it21918/django_adminSystem.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source myvenv/bin/activate
                    pip install -r requirements.txt
                    cd adminSystem
                    cp adminSystem/.env.example adminSystem/.env
                    chmod +x manage.py
                    ./manage.py test'''
            }
        }
        stage('install ansible prerequisites') {
            steps {
                sh '''
                    ansible-galaxy install geerlingguy.docker
                    ansible-galaxy install geerlingguy.pip
                    ansible-galaxy install geerlingguy.postgresql
                '''

                sh '''
                    mkdir -p ~/workspace/ansible-django/files/certs
                    cd ~/workspace/ansible-django/files/certs
                    openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 --nodes -subj '/C=GR/O=myorganization/OU=it/CN=myorg.com'
                '''
            }
        }   
        
        stage('Prepare Docker') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        pwd
                        echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l database ~/workspace/ansible-django/playbooks/docker-install.yml
                        '''
            }
            }
        }
        
        stage('deploy docker adminSystem image to vm 1') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        pwd
                        echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l database ~/workspace/ansible-django/playbooks/django-adminSystem-docker.yml
                        '''
            }
            }
        }
    

    }
}
