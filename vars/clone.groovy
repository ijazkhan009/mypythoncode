def call(String repo, String branch) {
    echo "Cloning repo..."
    git url: repo, branch: branch
}