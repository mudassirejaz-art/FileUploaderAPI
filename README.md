# 🐍 Snake File Uploader API + UI

A **production-ready file uploader** built with FastAPI (backend) and React + Tailwind (frontend). Users can upload, view, download, and delete files (images, videos, PDFs, etc.) directly from the browser or via API.

---

## ✨ Features

* Upload any file type (image, video, PDF, docs, etc.)
* Auto-generate unique stored filenames with hash
* File metadata stored in SQLite (size, type, hash, uploaded\_at)
* Public file view & download endpoints
* Delete files by ID
* Modern frontend UI for drag-and-drop or manual upload
* API tested with Postman (ready collection)

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Uvicorn, SQLite
* **Frontend:** React, TailwindCSS
* **Storage:** Local `/uploads` folder
* **Tools:** Postman (for API testing)

---

## 🚀 Setup Instructions

### Backend (FastAPI)

```bash
# Clone repo
git clone https://github.com/mudassirejaz-art/FileUploaderAPI
cd snake-file-uploader-api

# Create venv & install deps
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

👉 API will run at: `http://127.0.0.1:8000`

### Frontend (React + Tailwind)

```bash
cd frontend
npm install
npm run dev
```

👉 UI will run at: `http://localhost:5173`

---

## 📡 API Endpoints

| Method | Endpoint                         | Description    |
| ------ | -------------------------------- | -------------- |
| GET    | `/`                              | Health check   |
| POST   | `/api/upload`                    | Upload file    |
| GET    | `/api/files`                     | List all files |
| GET    | `/api/files/{id}`                | Get file by ID |
| GET    | `/api/files/download/{filename}` | Download file  |
| DELETE | `/api/files/{id}`                | Delete file    |

---

## 🧪 Testing with Postman

1. Import provided Postman collection
2. Test all endpoints: upload → list → view → download → delete
3. Confirm uploaded files open in browser via `url_view`
---

## 📌 Roadmap

* [ ] Add JWT authentication for file access
* [ ] Support cloud storage (AWS S3, GCP, etc.)
* [ ] Multi-user accounts with quotas

---

## 👨‍💻 Author

**Mudassir Ejaz**
GitHub: [mudassirejaz-art](https://github.com/mudassirejaz-art)

---

## 📜 License

MIT License
