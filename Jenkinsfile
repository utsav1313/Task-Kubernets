pipeline{
  agent any
  environment {
        imageName = "docker-imgutsav"
        registryCredentials = "nexus"
        registry = "54.236.40.60:9091/"
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
<<<<<<< HEAD
          
          sh 'docker build -t 54.236.40.60:9091/imagename:latest .'
=======
            dockerImage = docker.build imageName
            
>>>>>>> 43ace5a1d3588c5a17996d9fffbe58f33ed8e14b

        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
        script {
            
           docker.withRegistry( 'http://'+registry, registryCredentials ) {
           dockerImage.push('latest')
          }
        }
      }
    }
  }
}
