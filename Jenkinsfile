pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/vaibhav4222/Project1_OrangeHRM_Automation.git', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
