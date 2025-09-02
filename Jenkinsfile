pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vaibhav4222/Project1_OrangeHRM_Automation.git'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
