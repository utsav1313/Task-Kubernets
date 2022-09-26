pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build imagename .' 
                  sh 'docker tag imagename us1313/test1'
                
               
          }
        }
     
  stage('Push image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "dockerHub", url: "" ]) {
          sh  'docker push us1313/test1:latest'
          
        }
                  
          }
        }
     
      stage('Run Docker container on Jenkins Agent') {
             
            steps {
                sh "docker run -it  -p 9090:9090 us1313/test1"
 
            }
        }
 
    }
}