
# 🚀 Dockerized Web App Deployment using Ansible on Kubernetes (MicroK8s + WSL Ubuntu)

This project demonstrates how to **automate the deployment of a Dockerized Flask web application** using an **Ansible Playbook** on a **custom Kubernetes cluster** running on **MicroK8s in WSL Ubuntu**.

---

## 📌 Key Highlights

- 🐳 Docker image built manually
- ⚙️ Ansible automates Docker build, image import, and Kubernetes deployment
- ☸️ Kubernetes setup using MicroK8s (not Minikube)
- 🖥️ Fully runnable in **WSL2 Ubuntu**
- ❌ No DockerHub or pre-built images used

---

## 🗂️ Project Structure

```

dockerized-app-ansible-k8s/
├── app/
│   ├── app.py              # Simple Flask Web App
│   └── requirements.txt    # Python dependencies
├── Dockerfile              # Dockerfile to containerize the Flask app
├── ansible/
│   ├── inventory.ini       # Ansible inventory file (localhost)
│   ├── playbook.yml        # Main Ansible Playbook
│   └── roles/
│       ├── build-image/    # Docker image build role
│       └── deploy-k8s/     # Kubernetes deployment role

````

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- WSL2 with Ubuntu
- [MicroK8s installed](https://microk8s.io/docs/install-alternatives)
- Docker installed in WSL
- Python & Ansible installed in a virtual environment

```bash
sudo apt update
sudo apt install docker.io python3 python3-pip -y
pip3 install virtualenv
virtualenv ansible-venv
source ansible-venv/bin/activate
pip install ansible
````

---

## 🚀 Step-by-Step Execution

### 1. ✅ Start MicroK8s and enable DNS + storage:

```bash
sudo microk8s start
sudo microk8s enable dns storage
```

### 2. ✅ Clone the repo:

```bash
git clone https://github.com/yourusername/dockerized-app-ansible-k8s.git
cd dockerized-app-ansible-k8s/ansible
```

### 3. ✅ Run the Ansible Playbook:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

## 🔧 How It Works

### ✅ Role: `build-image`

* Builds Docker image from the `app/` folder
* Tags it as `flaskapp:latest`
* Saves and imports the image into MicroK8s' containerd

### ✅ Role: `deploy-k8s`

* Deploys the Flask app on Kubernetes using `microk8s kubectl`
* Creates a `Deployment` and `Service` (NodePort 30080)
* Uses `imagePullPolicy: Never` to force local image usage

---

## 🔍 Validate Deployment

```bash
microk8s kubectl get pods
microk8s kubectl get svc
```

Visit your app in the browser:

```
http://localhost:30080
```

---

## 📸 Sample Output

![MicroK8s Deployment](https://user-images.githubusercontent.com/youruser/flask-k8s-deployment.png)

---

## 🤝 Credits

Project developed by **Vaibhavi**, DevOps Engineer
Inspired by real-world Kubernetes and Ansible automation use cases.

---

## 📣 Let's Connect

If you liked the project, connect with me on [LinkedIn](https://www.linkedin.com/in/yourprofile)!




