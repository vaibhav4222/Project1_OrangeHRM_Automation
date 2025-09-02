pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/vaibhav4222/Project1_OrangeHRM_Automation.git', branch: 'master'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
