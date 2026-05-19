def call(String imageName) {
    echo "Building Docker image..."
    sh "docker build -t ${imageName} ."
}