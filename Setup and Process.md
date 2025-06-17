## ⚙️ Setup & Deployment

This section outlines how to deploy the complete Azure-based RAG (Retrieval-Augmented Generation) pipeline.

---

### ✅ Prerequisites

Make sure you have access to:

- An **Azure Subscription**
- **Azure OpenAI access** (approved from Azure portal)
- A **Resource Group**
- **Azure Blob Storage** with uploaded documents
- **Azure AI Search** instance
- Access to **AI Foundry** via Azure AI Studio

---

### 🧱 1. Resource Creation & Configuration

#### 📦 A. Azure Blob Storage

1. Go to **Azure Portal > Storage Accounts**
2. Create or open an existing storage account
3. Inside the storage account:
   - Navigate to **Containers**
   - Create a container (e.g., `enterprise-docs`)
   - Upload your files: `.pdf`, `.docx`, `.txt`, etc.

#### 🔎 B. Azure AI Search

1. Navigate to **Azure Portal > Azure AI Search**
2. Create a new Search service
   - Choose a pricing tier (Basic for small, Standard for scale)
3. In the Azure AI Search Studio:
   - **Create a Data Source**:
     - Source type: **Azure Blob Storage**
     - Provide a connection string or managed identity
   - **Create an Indexer**:
     - Use built-in skills (for OCR, metadata extraction)
     - Map fields: content, metadata, file name, etc.
   - **Create an Index**:
     - Make sure to include a `content` field (searchable)
     - Enable **vector search** if using semantic RAG

#### 🤖 C. Azure OpenAI

1. Go to **Azure AI Studio > Azure OpenAI**
2. Deploy a model (e.g., `gpt-35-turbo`, `gpt-4`)
3. Note down:
   - **API Endpoint**
   - **Deployment name**
   - **API key**

#### 🛠️ D. AI Foundry (Azure AI Studio)

1. Go to **Azure AI Studio > AI Foundry**
2. Create a new **Project** (RAG or Custom)
3. Add a **Data Source**:
   - Select your **AI Search index**
   - Choose which fields to extract (e.g., `content`, `filename`)
4. Add a **Skill Chain**:
   - Choose **Retrieve & Answer**
   - Select your deployed Azure OpenAI model
   - Connect it with the AI Search data source
5. Save & deploy

---

### 🔄 How It Works

```mermaid
flowchart TD
    A[User Input] --> B[AI Foundry Skill Chain]
    B --> C[Azure AI Search]
    C --> D[Retrieve Relevant Chunks]
    D --> E[Azure OpenAI Completion]
    E --> F[Generated Answer]
