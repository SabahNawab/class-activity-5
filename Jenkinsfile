pipeline {
    
    environment {
        imagename = "sabahnawabkhan/activity5"
        dockerImage = ''
        containerName = 'class-activity-container'
        dockerHubCredentials = 'clasactivityid'
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
                    dockerImage = docker.build("${imagename}:latest")
                }
            }
        }
 
        stage('Running image') {
            steps {
                script {
                    
                    bat "docker run -d --name ${containerName} ${imagename}:latest"
                }
            }
        }
 
        stage('Stop and Remove Container) {
            steps {
                script {
                    // Using 'bat' for Windows shell commands
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
                        // Use 'bat' for Windows shell commands
                        bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
                        bat "docker push ${imagename}:latest"
                    }
                }
            }
        }
    }
}
