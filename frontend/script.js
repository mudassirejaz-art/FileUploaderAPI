const form = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const fileList = document.getElementById("fileList");

async function fetchFiles() {
  const res = await fetch("/api/files/");
  const files = await res.json();
  fileList.innerHTML = "";
  files.forEach(f => {
    const li = document.createElement("li");
    li.textContent = f.filename + " ";
    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = async () => {
      await fetch(`/api/files/${f.id}`, { method: "DELETE" });
      fetchFiles();
    };
    li.appendChild(delBtn);
    fileList.appendChild(li);
  });
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = fileInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  await fetch("/api/files/upload", {
    method: "POST",
    body: formData
  });

  fileInput.value = "";
  fetchFiles();
});

fetchFiles();
