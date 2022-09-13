pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "http://44.202.141.94:8085/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/VishalTx/dockerflaskdemo.git']]])
      }
    }
     stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imageName
        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
         script {
             docker.withRegistry( 'http://44.202.141.94:8085' ) {
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}