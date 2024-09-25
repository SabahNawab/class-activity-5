pipeline {
    environment {
        imagename = "sabahnawabkhan/activity5"
        dockerImage = ''
        containerName = 'class-activity-container'
        dockerHubCredentials = 'clasactivityid' // Replace with your actual credentials ID
    }
  
    agent any

    stages {
        stage('Cloning Git') {
            steps {
                git([url: 'git@github.com:SabahNawab/class-activity-5.git', branch: 'main'])
            }
        }
 
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build "${imagename}:latest"
                }
            }
        }
 
        stage('Stop and Remove Container (if exists)') {
            steps {
                script {
                    bat """
                        IF EXIST ${containerName} (
                            docker stop ${containerName} || exit 0
                            docker rm ${containerName} || exit 0
                        )
                    """
                }
            }
        }

        stage('Deploy Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: dockerHubCredentials, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Using bat for Windows
                        bat """
                            docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                            docker build -t my_app_container .
                            docker tag my_app_container your_dockerhub_username/my_app_container
                            docker push your_dockerhub_username/my_app_container
                        """
                    }
                }
            }
        }
    }
}
