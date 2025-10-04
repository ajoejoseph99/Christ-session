# Christ-session

# Cloud Storage

This repository demonstrates basic operations with **Google Cloud Storage (GCS)**, including copying files from a bucket to your local machine and accessing the bucket via the console.

---

## Copy File from Cloud Storage

You can copy a file from a GCS bucket to your local machine using the following `gcloud` command:

```bash
gcloud storage cp gs://christ-bucket/google-cloud-logo-png_seeklogo-336116.png ./google-cloud-logo.png
```

You can access the shared bucket using the link (change the bucket name):
```bash
https://console.cloud.google.com/storage/browser/christ-bucket
```

You can delete an object from a bucket using the command 
```bash
gcloud storage rm gs://christ-bucket/google-cloud-logo.png
```
---

## Configure VM

Name: hello-cloud-vm (or any unique name)

Region & Zone: Choose a nearby region (e.g., asia-south1-a)

Machine Type: e2-micro (fits in free-tier)

Boot Disk:

Click Change

Choose Ubuntu 22.04 LTS or Debian 11

Size: default 10GB is fine

Firewall: Check both:

Allow HTTP traffic

Allow HTTPS traffic

✅ Click Create

## Inside the Virtual Machine

You can run the following commands inside the virtual machine 

```bash
sudo apt update
```

Install apache server

```bash
sudo apt install apache2 -y
sudo systemctl start apache2
sudo systemctl enable apache2
```

Create a Simple Web Page

```bash
sudo bash -c 'echo "<h1>Hello Cloud!</h1><p>My first VM is running!</p>" > /var/www/html/index.html'
```

Set correct permissions

```bash
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R 755 /var/www/html
```

Restart Web Server

```bash
sudo systemctl restart apache2
```

Go to VM’s external IP in a browser:

```bash
http://EXTERNAL_IP/
```

---

## Cloud SQL (MySQL)
Demo: Create an instance

Go to GCP Console → SQL → Create Instance

Choose MySQL

Set:

Instance ID: student-sql-demo

Password: your choice (note for Cloud Shell login) (GcP-1234)

Click Create (wait ~5 min for instance to be ready)


Connect via Cloud Shell

```bash
gcloud sql connect student-sql-demo --user=root
```

If it asks you to enable APIs, continue to do so.

Run simple SQL queries
```bash
CREATE DATABASE students;
USE students;

CREATE TABLE student_names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO student_names (name) VALUES ('Ajoe');
SELECT * FROM student_names;
```

Inserts your own name into the table
```bash
INSERT INTO student_names (name) VALUES ('<Your Name>');
SELECT * FROM student_names;
```

#Task 1: 
Query all names sorted alphabetically - put your SQL skills to use

---

## BigQuery
Demo: Load a public dataset

Go to BigQuery → Public Datasets → covid19_open_data (or Wikipedia dataset)

Click Explore → Create Table (if using local CSV)

Or query directly using SQL Editor:
```bash
SELECT country_name, SUM(new_confirmed) as total_cases
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
GROUP BY country_name
ORDER BY total_cases DESC
LIMIT 5;
```

#Task 2:
Hands-On Activity

Give 3 simple queries for:

-> Top 5 countries by total confirmed cases

-> Total deaths in a specific country

-> Find dates with the highest daily cases in a country

---

## Cloud Functions
Demo: Deploy a simple function

Go to Cloud Functions → Write a Function

Settings:

Name: hello-name

Trigger: HTTP

Runtime: Python 3.11 / Node.js 18

Code example (Python):
```bash
def hello_world(request):
    return "Hello Ajoe!"
```

Deploy → copy the trigger URL → visit in browser

#Task 3:
Create a function that returns current time

---

## Cloud Run
Copy contents of files 'app.py' and 'requirements.txt' into Cloud Editor

Set your project id in the gcloud terminal
```bash
gcloud config set project <<YOUR_GCP_PROJECT_ID>>
```

Enable the required APIs
```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

Deploy to Cloud Run
```bash
gcloud run deploy <<YOUR_APP_NAME>> --source . \
--region us-central1 \
--allow-unauthenticated \
--labels dev-tutorial=cvs11 \
--set-env-vars GOOGLE_CLOUD_PROJECT=<<YOUR_PROJECT_ID>>
```

---

##PubSub

Create a topic:
```bash
gcloud pubsub topics create demo-topic
```

Create a subscription:
```bash
gcloud pubsub subscriptions create demo-sub --topic=demo-topic
```

Publish message:
```bash
gcloud pubsub topics publish demo-topic --message "Hello students"
```

Pull message:
```bash
gcloud pubsub subscriptions pull demo-sub --auto-ack
```


