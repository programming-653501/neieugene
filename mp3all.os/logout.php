<?php
	require("db.php");
	unset($_SESSION['logged_user']);
	session_destroy();
	header('Location: /')
?>