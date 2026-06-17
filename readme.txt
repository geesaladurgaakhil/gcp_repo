   30  gcloud iam workload-identity-pools create github-pool1 --location=global
   31  gcloud iam workload-identity-pools providers create-oidc github-provider --location="global" --workload-identity-pool="github-pool1"   --issuer-uri="https://token.actions.githubusercontent.com"   --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.ref=assertion.ref"   --attribute-condition="attribute.repository=='geesaladurgaakhil/gcp_repo' && attribute.ref=='refs/heads/main'"
   32  gcloud iam workload-identity-pools providers describe github-provider --location=global --workload-identity-pool=github-pool
   33  gcloud projects describe project-125a5906-9774-4549-bad --format="value(projectNumber)"
   35  gcloud iam service-accounts add-iam-policy-binding githubactions-sa@project-125a5906-9774-4549-bad.iam.gserviceaccount.com --role="roles/iam.workloadIdentityUser" --member="principalSet://iam.googleapis.com/projects/717948519217/locations/global/workloadIdentityPools/github-pool1/attribute.repository/geesaladurgaakhil/gcp_repo"

sonarqube:
---------



kubectl create namespace sonarqube
   48  helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
   49  helm repo update
   50  helm search repo sonarqube
   51  vi values.yml
   52  helm install sonarqube sonarqube/sonarqube -n sonarqube -f values.yaml
   53  helm install sonarqube sonarqube/sonarqube -n sonarqube -f values.yml
   54  helm install sonarqube sonarqube/sonarqube -n sonarqube -f values.yml --set monitoringPasscode=SonarMonitoring123
   55  helm install sonarqube sonarqube/sonarqube -n sonarqube -f values.yml --set monitoringPasscode=SonarMonitoring123 --set edition=developer
   56  kubectl get pods
   57  kubectl get pods -n sonarqube
   58  kubectl get svc -n sonarqube
