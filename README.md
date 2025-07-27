# 🚀 Deploy a Dockerized Web App using Ansible on Kubernetes (MicroK8s)

This project demonstrates deploying a Flask-based Dockerized Web App using Ansible onto a manually configured MicroK8s cluster inside WSL Ubuntu.

## 🧰 Stack

- Docker (manual build)
- MicroK8s (lightweight Kubernetes)
- Ansible (automation tool)
- Python Flask (sample app)

## 📦 Folder Structure

```
dockerized-app-ansible-k8s/
├── app/                  # Flask app + Dockerfile
├── ansible/              # Ansible playbooks and roles
├── README.md             # This file
```

## ✅ How to Run

1. Clone the repo:
    ```bash
    git clone <your-repo>
    cd dockerized-app-ansible-k8s
    ```

2. Install dependencies:
    ```bash
    sudo apt install docker.io ansible
    sudo snap install microk8s --classic
    microk8s enable dns storage
    ```

3. Build and deploy:
    ```bash
    cd ansible
    ansible-playbook -i inventory.ini playbook.yml
    ```

4. Access the app:
    - URL: `http://localhost:30080`
