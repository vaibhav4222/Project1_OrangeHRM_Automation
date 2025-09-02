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

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }
    }
}
