<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Consultation";

$nom=$_POST['nom'];
$prenom=$_POST['prenom'];
$age=$_POST['age'];
$sex=$_POST['sex'];
$date=$_POST['date'];
// connection au serveur
$conn = mysqli_connect($servername, $username, $password, $dbname);
// verification de la connection
if (!$conn) {
    die("erreur de connection: " . mysqli_connect_error());
}
//creation de la table
$sql = "INSERT INTO Consultation(NOM, PRENOM, AGE,SEX,date_enregitrment)
VALUES ('$nom','$prenom','$age','$sex','$date')";

if ($conn->query($sql) === TRUE) {
    echo "<h1>Vos information on ete enregistrer</h1>";
} else {
    echo "Erreur: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>