stage('Build ImG From Docker file'){
    sh 'docker build -t demo/demorp name .'
}
stage('Push Docker Images to Nexus Registry'){
    sh 'docker push '
}
stage('Docker Nexus Auth'){
    sh 'docker login -u admin -p admin http://44.201.118.101:9001/'
}