<<<<<<< HEAD

# 🚀 Deploy a Dockerized Web App Using Ansible on a Kubernetes Cluster (MicroK8s on WSL)

This project demonstrates how to **build and deploy a Flask-based Docker web application** using **Ansible** on a **manually configured Kubernetes cluster (MicroK8s)** inside **WSL Ubuntu**. All Docker and Kubernetes configurations are done manually — no prebuilt images or services.



## 📦 Project Structure

```

=======
# 🚀 Deploy Dockerized Web App on MicroK8s using Ansible

This project automates the deployment of a Flask-based Docker web app onto a manually configured MicroK8s Kubernetes cluster using Ansible.

---

## 📁 Project Structure

```
>>>>>>> 7ecc758 (updated)
docker-ansible-k8s/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   ├── templates/
│   │   └── deployment.yaml.j2
│   └── roles/
│       └── webapp/
│           └── tasks/
│               └── main.yml
├── webapp/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
<<<<<<< HEAD

````

---

## ⚙️ Technologies Used

- **Python** & **Flask**
- **Docker** (Manual image build)
- **MicroK8s** (Kubernetes on WSL)
- **Ansible** (For automation)
- **WSL Ubuntu 22.04+**

---

## ✅ Prerequisites

1. Docker installed in WSL Ubuntu
2. MicroK8s installed and running:
   ```bash
   sudo snap install microk8s --classic
   sudo usermod -a -G microk8s $USER
   microk8s status --wait-ready
````

3. Ansible installed:

   ```bash
   sudo apt update && sudo apt install -y ansible python3-venv
   ```
4. Python Virtual Environment for Ansible dependencies:

   ```bash
   python3 -m venv ~/ansible-venv
   source ~/ansible-venv/bin/activate
   pip install -r ansible/requirements.txt
   ```

---

## 🚀 Step-by-Step Setup

### 1. 🧱 Clone the Repo

```bash
git clone https://github.com/your-username/docker-ansible-k8s.git
cd docker-ansible-k8s
```

### 2. 🐳 Build and Save Docker Image with Ansible

```bash
cd ansible
ansible-playbook -i inventory.ini playbook.yml
```

> 🔹 This will:
>
> * Build a Docker image from `webapp/`
> * Save it as a `.tar`
> * Import it into MicroK8s containerd
> * Deploy it to Kubernetes using templated YAML

### 3. 🔎 Verify Kubernetes Resources

```bash
microk8s kubectl get all
```

You should see the pod, deployment, and service up and running.

---

## 🌐 Access the Web App

1. Get the `NodePort` exposed:

   ```bash
   microk8s kubectl get svc flask-service
   ```

2. Access it using:

   ```
   http://localhost:<nodeport>
   ```

---

## 📜 Example Ansible Tasks

```yaml
- name: Build Docker image
  shell: docker build -t flask-webapp:latest {{ playbook_dir }}/../webapp

- name: Save Docker image to tar
  shell: docker save flask-webapp -o /tmp/flask-webapp.tar

- name: Import image into MicroK8s
  shell: microk8s ctr image import /tmp/flask-webapp.tar

- name: Deploy to Kubernetes
  kubernetes.core.k8s:
    state: present
    definition: "{{ lookup('template', 'templates/deployment.yaml.j2') }}"
=======
```

---

## ⚙️ Manual Setup (WSL + MicroK8s)

```bash
# On WSL Ubuntu
sudo apt update && sudo apt install -y docker.io python3-pip python3-venv

# Install and enable MicroK8s
sudo snap install microk8s --classic
sudo usermod -a -G microk8s $USER
newgrp microk8s
microk8s status --wait-ready
microk8s enable dns storage

# Create and activate virtual environment
python3 -m venv ansible-venv
source ansible-venv/bin/activate
pip install --upgrade pip
pip install ansible docker kubernetes
```

---

## 🚀 Deployment using Ansible

```bash
cd docker-ansible-k8s/ansible
ansible-playbook -i inventory.ini playbook.yml
```

---

## 🌐 Access Web App

```bash
microk8s kubectl get svc flask-service
# Visit http://localhost:<NodePort> on your browser
>>>>>>> 7ecc758 (updated)
```

---

<<<<<<< HEAD
## 🧪 Test the Web App

Once deployed, you can test:

```bash
curl http://localhost:<nodeport>
```

You should receive a message like: `Hello from Flask inside Kubernetes!`

---

## 📌 Author

**Vaibhavi Sugandhi**
[GitHub](https://github.com/VaibhaviSugandhi1733) • [LinkedIn](https://www.linkedin.com/in/vaibhavi-sugandhi/)

---

## 🏁 Final Notes

* This setup avoids prebuilt images and registries.
* Great for DevOps hands-on learning: Docker, Kubernetes, Ansible, and MicroK8s all in one.
* Easily extendable for CI/CD pipelines (Jenkins + GitHub Actions next!).

---

---

=======
## 🧹 To Redeploy

```bash
microk8s kubectl delete deployment flask-deployment
microk8s kubectl delete svc flask-service
ansible-playbook -i inventory.ini playbook.yml
```
>>>>>>> 7ecc758 (updated)
