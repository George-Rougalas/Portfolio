
<?php
$servername = "localhost";
$username = "mpa"; //ή όποιον χρήστη έχετε
$password = "geiasou"; // αλλάξτε το
$dbname = "persona";
// Δημιουργία σύνδεσης 
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Έλεγχος σύνδεσης
if (!$conn) {
die("Connection failed: " . mysqli_connect_error());}
//ορισμός charset της σύνδεσης ώστε να παρουσιάζονται τα ελληνικά σωστά
mysqli_set_charset($conn, "utf8");
//Δημιουργία ερωτήματος
$sql = "INSERT INTO `f5`(`name`, `sex`, `album`, `comments`, `dislike`, `lyrics`, `review`) VALUES ('".$_POST['name']."','".$_POST['sex']."',',".$_POST['album']."','".$_POST['comments']."','".$_POST['dislike']."','".$_POST['lyrics']."','".$_POST['review']."') ;";
//εκτέλεση ερωτήματος στη βάση
$result = mysqli_query($conn, $sql);
//έλεγχος αποτελεσμάτων
if ($result) {
//Εμφάνιση αποτελεσμάτων σε μορφή πίνακα
echo "<br>αποθηκευση οκ<br>";
}else{
echo "no";}
//κλείσιμο σύνδεσης
mysqli_close($conn);
?>  