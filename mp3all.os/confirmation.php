<?php 
	header("Location: {$_SERVER['HTTP_REFERER']}");
	include("db.php");
	$_SESSION['confirmation'] = true;
?>