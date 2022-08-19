pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/it21918/django_adminSystem.git'

                
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
        
        stage('Setup DB') {
            steps {
                ssshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l deploymentservers ~/workspace/ansible-django/playbooks/postgres.yml
                    '''
                }
            }
        }
        
    
        stage('deploym to vm 1') {
            steps{
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l deploymentservers ~/workspace/ansible-django/playbooks/django-project-install-adminSystem.yml
                    '''
                }

            }

        }
    }
}
