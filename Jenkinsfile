stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/utsav1313/Task-Kubernets.git']]])
      }
    }
     stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imageName
        }
      }
    }
    stage('Uploading to Docker hub') {
     steps{  
         script {
             sh 'docker tag imagename us1313/test1 '
             sh 'docker push us1313/test1'
          }
        }
      }
    }
    stage('Pre Prod..') {
     steps{  
         script {
             sh ' docker run -it -d -p 9090:9090 --name demo localhost:9091/docker-image'
        }
      }
    }
  
