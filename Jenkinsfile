pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 --version
                pip3 install --break-system-packages -r UserService/requirements.txt
                pip3 install --break-system-packages -r ProductService/requirements.txt
                pip3 install --break-system-packages -r OrderService/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                cd UserService && python3 -m pytest
                '''
            }
        }
        stage('Lint UserService') {
    steps {
        sh '''
        cd UserService
        python3 -m flake8 .
        '''
    }
}

stage('Lint ProductService') {
    steps {
        sh '''
        cd ProductService
        python3 -m flake8 .
        '''
    }
}

stage('Lint OrderService') {
    steps {
        sh '''
        cd OrderService
        python3 -m flake8 .
        '''
    }
}
stage('Build UserService Image') {
    steps {
        sh '''
        docker build -t userservice:${BUILD_NUMBER} UserService
        '''
    }
}
stage('Build ProductService Image') {
    steps {
        sh '''
        docker build -t productservice:${BUILD_NUMBER} ProductService
        '''
    }
}
stage('Build OrderService Image') {
    steps {
        sh '''
        docker build -t orderservice:${BUILD_NUMBER} OrderService
        '''
    }
}
stage('Scan UserService Image') {
    steps {
        sh '''
        trivy image userservice:${BUILD_NUMBER}
        '''
    }
}
stage('Scan ProductService Image') {
    steps {
        sh '''
        trivy image productservice:${BUILD_NUMBER}
        '''
    }
}
stage('Scan OrderService Image') {
    steps {
        sh '''
        trivy image orderservice:${BUILD_NUMBER}
        '''
    }
}
stage('Docker Login') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            sh '''
            echo "$DOCKER_PASS" | docker login \
            -u "$DOCKER_USER" \
            --password-stdin
            '''
        }
    }
}

stage('Push Docker Images') {
    steps {
        sh '''
        docker tag userservice:${BUILD_NUMBER} srihaasad/userservice:${BUILD_NUMBER}
        docker tag productservice:${BUILD_NUMBER} srihaasad/productservice:${BUILD_NUMBER}
        docker tag orderservice:${BUILD_NUMBER} srihaasad/orderservice:${BUILD_NUMBER}

        docker push srihaasad/userservice:${BUILD_NUMBER}
        docker push srihaasad/productservice:${BUILD_NUMBER}
        docker push srihaasad/orderservice:${BUILD_NUMBER}
        '''
    }
}
        
    }
}

