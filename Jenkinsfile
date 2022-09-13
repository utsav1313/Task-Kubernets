pipeline{
  agent any
  environment {
        imagename = "docker-image"
        registryCredentials = "nexus"
        registry = "54.89.106.223:9050"
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
          
          sh 'docker build -t localhost:9050/imagename:latest .'

        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
        script {
            
          sh 'docker push localhost:9050/imagename'
          }
        }
      }
    }
}