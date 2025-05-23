## 📊 CloudFinSecure – Employee Transaction Fraud Detection System

**CloudFinSecure** is an AWS-powered real-time fraud detection solution designed to help small and medium-sized organizations identify suspicious employee transactions. It leverages serverless architecture and intelligent risk scoring to detect high-risk financial activities and alert stakeholders instantly.

---

### ✨ Project Highlights

* 🔍 **Detects anomalous or high-risk transactions**
* 📬 **Sends real-time alerts via Amazon SNS**
* 📃 **Stores structured transactions in DynamoDB**
* 📈 **Visualizes transactions through an interactive Streamlit dashboard**
* ☁️ **Deployed entirely on AWS with no servers to manage**

---

### 📇 Architecture Overview

```plaintext
S3 (CSV Upload)
     ⬇ Trigger
AWS Lambda (ETL + Risk Engine)
     ⬇
DynamoDB (Storage)
     ⬇
Streamlit Dashboard (Visualization)
     ⬇
SNS (Real-time Alerts)
```

---

### 🛠 Technologies Used

* **AWS Lambda** – Serverless compute for processing
* **Amazon S3** – Upload transaction CSVs
* **Amazon DynamoDB** – NoSQL transaction storage
* **Amazon SNS** – Send fraud alerts via email
* **Streamlit** – Frontend dashboard
* **Python** – Language for logic and dashboard
* **Boto3** – AWS SDK for Python

---

### 📂 Folder Structure

```
cloudfinsecuredashboard/
│
├— cloudfinsecure.py           # Streamlit dashboard app
├— requirements.txt            # Dependencies for deployment
├— lambda_function.py          # AWS Lambda fraud detection logic
├— sample_transactions.csv     # Example transaction file
└— README.md                   # Project documentation
```

---

### 🛆 Features

✅ Real-time transaction risk scoring
✅ Email alerts for high-risk anomalies
✅ Fully serverless AWS backend
✅ Interactive filtering by risk level & location
✅ Secure and scalable

---

### 🧠 How It Works

1. **Upload CSV to S3**

   * A file like `transactions.csv` is uploaded to a secure S3 bucket.

2. **Lambda Is Triggered**

   * The Lambda function parses the CSV, computes fraud risk scores using:

     * High amount detection
     * Outlier locations
     * Weekend/late-night activity
     * Suspicious descriptions (e.g., "gift", "gaming")

3. **DynamoDB Stores Results**

   * Structured transaction data, along with risk scores, is stored in DynamoDB.

4. **SNS Sends Alerts**

   * For any transaction flagged as **HIGH** risk or amount > ₹10,000, an email alert is sent via Amazon SNS.

5. **Streamlit Dashboard Shows Everything**

   * Visualize all transactions, filter by risk level or location, and download results.

---

### 🖥 Demo – Streamlit Dashboard

> ✅ [Click here to view the live dashboard](https://cloudfinsecure-mi8hfv8dtelmep49qu3sqe.streamlit.app)
> ---

### 🔐 Setup Instructions (Locally)

1. Clone this repository

   ```bash
   git clone https://github.com/sourav24r/cloudfinsecure.git
   cd cloudfinsecure
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials

   ```bash
   aws configure
   ```

4. Run the dashboard

   ```bash
   streamlit run cloudfinsecure.py
   ```

---

### 🔐 Streamlit Cloud Deployment

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) → “New app”
3. Select the repo and file `cloudfinsecure.py`
4. Add the following **secrets**:

```toml
AWS_ACCESS_KEY_ID     = "your-key"
AWS_SECRET_ACCESS_KEY = "your-secret"
AWS_DEFAULT_REGION    = "ap-south-1"
DYNAMO_TABLE          = "transactions_cloudfinsecure"
```

---

### 🧪 Sample Transaction Format (CSV)

| transaction\_id | employee\_id | amount | location | description | timestamp            |
| --------------- | ------------ | ------ | -------- | ----------- | -------------------- |
| TXN001          | EMP001       | 12000  | delhi    | gift card   | 2025-05-20T23:30:00Z |
| TXN002          | EMP002       | 5000   | london   | lunch       | 2025-05-21T14:10:00Z |

---

### 🏑 Final Thoughts

CloudFinSecure offers a production-ready blueprint for financial anomaly detection, tailored for SMEs. It's serverless, scalable, secure, and simple to deploy.

> ⭐ Star this repo if you found it helpful!
> 🛠 Feel free to fork and extend the logic, alerts, or dashboards.
