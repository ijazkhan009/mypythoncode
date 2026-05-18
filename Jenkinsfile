@Library('shared') _
pipeline {
    agent { label 'localVm-agent' }

    environment {
        IMAGE_NAME = "notes-app:latest"
        DOCKER_USER = "ejazkhan1995"
    }

    stages {

        stage("Checkout Code") {
            steps {
                script {
                    clone("https://github.com/ijazkhan009/mypythoncode.git", "master")
                }
            }
        }

        
        stage("Hadolint Scan") {
            steps {
                sh """
                echo "Running Hadolint Scan..."

                docker run --rm -i \
                  hadolint/hadolint < Dockerfile > hadolint_report.txt || true

                cat hadolint_report.txt

                echo "Checking for errors..."

                # ✅ FAIL ONLY ON ERRORS
                if grep -i "error" hadolint_report.txt; then
                    echo " Hadolint Errors Found → Failing Build"
                    exit 1
                else
                    echo " No critical errors"
                fi
                """
            }
        }


        stage("Build Image") {
            steps {
                script {
                    buildDocker(IMAGE_NAME)
                }
            }
        }

        stage("Test") {
            steps {
                echo "Running tests...."
            }
        }

        stage("Push Image") {
            steps {
                script {
                    pushDocker(IMAGE_NAME, DOCKER_USER, "dockerhub-creds")
                }
            }
        }

        stage("Deploy") {
            steps {
                script {
                    deployApp(IMAGE_NAME)
                }
            }
        }
    }
}