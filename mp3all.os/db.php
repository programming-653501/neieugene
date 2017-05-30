<?php
    require("libs/rb.php");
    R::setup( 'mysql:host=localhost;dbname=mp3all',
        'root', '' );
    $link = mysqli_connect("localhost", "root", "", "mp3all");
    session_start();
?>