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
                // Cloning the GitHub repository
                git([url: 'git@github.com:SabahNawab/class-activity-5.git', branch: 'main'])
            }
        }

        stage('Building Image') {
            steps {
                script {
                    // Building Docker image
                    dockerImage = docker.build("${imagename}:latest")
                }
            }
        }

        stage('Stop and Remove Container (if exists)') {
            steps {
                script {
                    // Stop and remove any existing container before starting a new one
                    sh """
                        if [ \$(docker ps -aq -f name=${containerName}) ]; then
                            docker stop ${containerName}
                            docker rm ${containerName}
                        fi
                    """
                }
            }
        }

        stage('Running Image') {
            steps {
                script {
                    // Running the newly built Docker image
                    sh "docker run -d --name ${containerName} ${imagename}:latest"
                }
            }
        }

        stage('Pushing Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: dockerHubCredentials, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Logging in to Docker Hub
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        // Pushing the Docker image to Docker Hub
                        sh "docker push ${imagename}:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Ensuring the container is stopped and removed after the pipeline execution
                sh """
                    if [ \$(docker ps -aq -f name=${containerName}) ]; then
                        docker stop ${containerName}
                        docker rm ${containerName}
                    fi
                """
            }
        }

        cleanup {
            // Clean up dangling images
            script {
                sh "docker image prune -f"
            }
        }
    }
}
