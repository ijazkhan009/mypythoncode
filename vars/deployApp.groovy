def call(String imageName) {
    echo "Deploying container..."
    sh "docker run -d -p 9001:9001 ${imageName}"
}