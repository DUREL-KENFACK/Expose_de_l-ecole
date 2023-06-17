<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Consultation";

// connection au serveur
$conn = mysqli_connect($servername, $username, $password, $dbname);
// verificaton de la connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// creation de la table
$sql = "CREATE TABLE Consultation(
id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
NOM VARCHAR(30) NOT NULL,
PRENOM VARCHAR(30) NOT NULL,
AGE VARCHAR(50) NOT NULL,
SEX VARCHAR(30) NOT NULL,
date_enregitrment VARCHAR(30) NOT NULL
)";

if (mysqli_query($conn, $sql)) {
    echo "<h1>La table a ete cree</h1>";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);
?>