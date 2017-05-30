<?php 
	require "db.php";
	$data = $_POST;
	$_SESSION['savelogin'] = $data['login'];
	$_SESSION['savepassword'] = $data['password'];

	if (isset($data['do_login'])){
		$user = R::findOne('users', 'login = ?', array($data['login']));
		if ($user){
			if (password_verify($data['password'], $user->password)){
				$_SESSION['logged_user'] = $user;
				echo '<div style="color: green;">Вы авторизованы, можете перейти на <a href="/"> главную </a> страницу!</div><hr>';
				$_SESSION['songsinbasket'] = unserialize($user->songsinbasket);
			}
			else{
				$errors[] = 'Неверный пароль!';
			}
		}
		else{
			$errors[] = 'Пользователя с таким логином не существует!';
		}

		if (empty($errors)){

		}
		else{
			echo '<div style="color: red;">'.array_shift($errors).'</div><hr>';		
		}
	}
?>

<form action="login.php" method="POST">
	<p>
		<p><strong>Логин:</strong></p>
		<input type="text" name="login" value="<?php echo @$data['login']; ?>">
	</p>

	<p>
		<p><strong>Пароль:</strong></p>
		<input type="password" name="password" value="<?php echo @$data['password']; ?>">
	</p>

	<p>
		<button type="submit" name="do_login" >Войти</button>
	</p>
</form>