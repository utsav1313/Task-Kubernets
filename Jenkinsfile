pipeline{
  agent any
  environment {
        imagename = "docker-image"
        registryCredentials = "nexus"
        registry = "54.89.106.223:9001"
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
          
          sh 'docker build -t 54.89.106.223:9001/imagename:latest .'

        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
         script {
            
            sh 'docker push 54.89.106.223:9001/imagename'
          }
        }
      }
    }
}