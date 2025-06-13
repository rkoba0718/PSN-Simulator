pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        bat 'cmake -B build -DCMAKE_BUILD_TYPE=Release'
        bat 'cmake --build build --config Release'
      }
    }
    stage('Archive Artifact') {
      steps {
        archiveArtifacts artifacts: 'build/src/Release/psn_cli.exe', fingerprint: true
      }
    }
  }

  post {
    always {
      slackSend(
        tokenCredentialId: 'psn-simulator-token',
        channel: '#daily-jenkins-build-alert',
        color: currentBuild.result == 'SUCCESS' ? 'good' : 'danger',
        teamDomain: 'psnsimulator',
        message: "Jenkins Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' ${currentBuild.result}. <${env.BUILD_URL}|Show detail>"
      )
    }
  }
}
