def call(String imageName, String dockerUser, String credentialsId) {
    withCredentials([usernamePassword(credentialsId: credentialsId, passwordVariable: "dockerPass", usernameVariable: "dockerUserVar")]) {
        sh "echo \$dockerPass | docker login -u \$dockerUserVar --password-stdin"
        sh "docker tag ${imageName} \$dockerUserVar/${imageName}"
        sh "docker push \$dockerUserVar/${imageName}"
    }
}