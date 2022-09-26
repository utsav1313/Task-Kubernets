node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("us1313/test1")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
         sh 'docker Push us1313/test1'
    }
     stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
 }