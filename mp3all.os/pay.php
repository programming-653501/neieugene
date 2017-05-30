<?php 
	header("Location: {$_SERVER['HTTP_REFERER']}");
	include("db.php");
	if ($_SESSION['total'] <= $_SESSION['mybalance']){
		foreach ($_SESSION['goodsongs'] as $song) {
			$_SESSION['paysongs'] = $_SESSION['goodsongs'];
		}
		foreach (array_keys($_SESSION['songsinbasket']) as $song_id){
            $_SESSION['songsinbasket'][$song_id] = 2;
        }
		$user = R::findOne('users', 'login = ?', array($_SESSION['savelogin']));
		$user->money -= $_SESSION['total'];
		$user->songsinbasket = serialize($_SESSION['songsinbasket']);
		R::store($user);
		$_SESSION['logged_user'] = $user;


		$stats = R::dispense( 'statistics' );
    	$stats->name = $_SESSION['savelogin'];
    	$stats->datetime = date("Y-m-d H:i:s");
    	$stats->value = $_SESSION['total'];
    	R::store( $stats );
	}
?>