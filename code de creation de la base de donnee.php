<?php
$servername = "localhost";
$username = "root";
$password = "";

// connection au seveur
$conn = mysqli_connect($servername, $username, $password);
// verification de la connection
if (!$conn) {
    die("erreur de la connection: " . mysqli_connect_error());
}
else
{
    echo "connection reusie";
}

// creation de base de donnee
$sql = "CREATE DATABASE Consultation";
// verificatiin de la creation
if (mysqli_query($conn, $sql)) {
    echo "<h1>La base a bien ete cree</h1>";
} else {
    echo "<h1>erreur</h1> " . mysqli_error($conn);
}

mysqli_close($conn);
?>