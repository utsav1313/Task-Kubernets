pipeline{
  agent any
  environment {
        imagename = "docker-image"
        registryCredentials = "nexus"
        registry = "localhost:9091"
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
          
          sh 'docker build -t localhost:9091/imagename:latest .'

        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
        script {
            
           sh 'docker push localhost:9091/imagename:latest'
          }
        }
      }
    }
}