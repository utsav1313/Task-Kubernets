pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "54.89.106.223:9001/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/utsav1313/Task-Kubernets.git']]])
      }
    }
     stage('Building image') {
      steps{
        script {
          
          sh 'docker build -t imageName .'

        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
         script {
             docker.withRegistry( 'http://54.89.106.223:9001' ) {
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}