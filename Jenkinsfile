pipeline {
    agent any
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
                    dockerImage = docker.build "${imagename}:latest"
                }
            }
        }
 
        stage('Running image') {
            steps {
                script {
                    sh "docker run -d --name ${containerName} ${imagename}:latest"
                }
            }
        }
 
        stage('Stop and Remove Container') {
            steps {
                script {
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"
                }
            }
        }
 
        stage('Deploy Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: dockerHubCredentials, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"

                        sh "docker push ${imagename}:latest"
                    }
                }
            }
        }
    }
}