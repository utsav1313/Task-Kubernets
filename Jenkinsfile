stage('Build ImG From Docker file'){
    sh 'docker build -t docker12/proj12 .'
}
stage('Push Docker Images to Nexus Registry'){
    sh 'docker push '
}
stage('Docker Nexus Auth'){
    sh 'docker login -u admin -p 123 http://44.201.118.101:9001/'
}