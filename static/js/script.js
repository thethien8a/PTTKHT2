document.getElementById('fileInput').addEventListener('change', handleFile);

function handleFile(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();

    reader.onload = function (e) {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });

        // Giả sử dữ liệu nằm trong sheet đầu tiên
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];

        // Chuyển sheet thành JSON
        const jsonData = XLSX.utils.sheet_to_json(worksheet);

        // Cập nhật bảng
        populateTable(jsonData);
    };

    reader.readAsArrayBuffer(file);
}

function populateTable(data) {
    const tableBody = document.getElementById('productTableBody');
    tableBody.innerHTML = ''; // Xóa dữ liệu cũ

    data.forEach(row => {
        const tr = document.createElement('tr');

        tr.innerHTML = `
            <td><input type="checkbox"></td>
            <td>${row['Mã hàng'] || ''}</td>
            <td>${row['Tên hàng'] || ''}</td>
            <td>${row['Giá bán'] || ''}</td>
            <td>${row['Tồn kho'] || ''}</td>
            <td>${row['Số lượng'] || ''}</td>
            <td>${row['Trạng thái'] || ''}</td>
        `;

        tableBody.appendChild(tr);
    });
}
