<?php
// Koneksi ke database
$servername = "localhost";
$username = "root"; // default XAMPP
$password = ""; // kosongkan jika belum diatur
$dbname = "kampus"; // nama database yang kamu buat

// Membuat koneksi
$conn = new mysqli($servername, $username, $password, $dbname);

// Memeriksa koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}

// SQL untuk membuat tabel
$sql = "CREATE TABLE Mahasiswa (
    NPM VARCHAR(9) PRIMARY KEY,
    Nama VARCHAR(25),
    tglLhr DATE,
    Prodi VARCHAR(20)
)";

// Eksekusi query
if ($conn->query($sql) === TRUE) {
    echo "Tabel Mahasiswa berhasil dibuat!";
} else {
    echo "Error saat membuat tabel: " . $conn->error;
}

$conn->close();
?>
