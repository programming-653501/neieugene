<?php 
	include("db.php");
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?php echo $SESSION['site_name']; ?></title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="./slick/slick.css">
    <link rel="stylesheet" type="text/css" href="./slick/slick-theme.css">
    <link rel="stylesheet" href="css/style.css">
  </head>


<body>
	<div class="wrapper">
		<header class="header">
			<div class="container">
				<div class="row">
					<div class="h-panel clearfix">
						<nav class="h-nav h-nav-tabs">
							<a href="/">Главная</a>
							<a href="/">Помошь</a>
							<a href="/">Доставка</a>
							<a href="/">Способы оплаты</a>
						</nav>
						<nav class="h-nav pull-right">
							<?php if (isset($_SESSION['logged_user'])) : ?>
								Авторизован!
								Привет, <?php echo $_SESSION['logged_user']->login; ?>
								<a href="logout.php">Выйти</a>
							<?php else : ?>
								<a href="login.php">Войти</a>
								<a href="signup.php">Регистрация</a>
							<?php endif; ?>
						</nav>
					</div>
				</div>
			</div>
			<div class="header-bottom">
				<div class="container">
				<div class="row">
					<div class="col-lg-3">
						<div class="logo">
							<a href="/"><img src="img/logo.png" height="59" alt=""><a href=""></a>
						</div>
					</div>
					<div class="col-lg-6">
						<form action="#" class="h-search">
							<input type="text" placeholder="Поиск среди десятков песен">
							<input type="submit" value="искать">
						</form>
					</div>
					<div class="pull-right">
						<div class="dropdown">
							<form action="basket.php">
								<button class="btn btn-lg btn-info">Корзина</button>
							</form>
						</div>
					</div>
				</div>
				</div>
			</div>
		</header>

		<div class="panel">
			<div class="container">
				<div class="row buttons">
					<div class="btn-group btn-group-justified">
						<div class="btn-group"><a href="/"><button class="br0 btn btn-default" role="button">Все песни</button></a></div>
						<div class="btn-group"><a href="/"><button class="btn btn-default" role="button">Исполнители</button></a></div>
						<div class="btn-group"><a href="/"><button class="btn btn-default" role="button">Жанры</button></a></div>
						<div class="btn-group"><a href="/"><button class="btn btn-default" role="button">Статьи</button></a></div>
						<div class="btn-group"><a href="/"><button class="btn btn-default" role="button">Альбомы</button></a></div>
						<div class="btn-group"><a href="/"><button class="btn btn-default" role="button">Популярное</button></a></div>
						<div class="btn-group"><a href="/"><button class="br0 btn btn-default" role="button">Рекомендации</button></a></div>
					</div>
				</div>
			</div>
		</div>
	<div class="container">
		<div class="row">
			<section class="slider">
    			<div class="slide"><img src="img/albums/GoltOnTheCelig.jpg"></div>
    			<div class="slide"><img src="img/albums/Enjoykin.jpg"></div>
    			<div class="slide"><img src="img/albums/Kapital.jpg"></div>
    			<div class="slide"><img src="img/albums/Love.jpg"></div>
    			<div class="slide"><img src="img/albums/Matreshka.jpg"></div>
    			<div class="slide"><img src="img/albums/nirvana.jpg"></div>
    			<div class="slide"><img src="img/albums/Rise.jpg"></div>
    			<div class="slide"><img src="img/albums/TheEssential.jpg"></div>
    			<div class="slide"><img src="img/albums/ACDC.jpg"></div>
    			<div class="slide"><img src="img/albums/Covers.jpg"></div>
    			<div class="slide"><img src="img/albums/SayAnything.jpg"></div>
    			<div class="slide"><img src="img/albums/ThisIsIt.jpg"></div>
    		</section>
		</div>
	</div>

<?php
	$song_id = $_GET['song_id'];

	if ($_SESSION['confirmation'] and isset($_SESSION['songsinbasket'][$song_id])){ # нажата кнопка убать из карзины
		unset($_SESSION['songsinbasket'][$song_id]);
		$_SESSION['confirmation'] = false;
	}
	else if ($_SESSION['confirmation'] and !isset($_SESSION['songsinbasket'][$song_id])){ # нажата кнопка добавить  карзину
		$_SESSION['songsinbasket'][$song_id] = 1;
		$_SESSION['confirmation'] = false;
	}

	$_SESSION['confirmation'] = false;
	$songs = R::findAll('songs');
	$directions = R::findAll('directions');
	$executors = R::findAll('executors');
	foreach ($songs as $song) {
		if ($song->id == $song_id){
			echo $song->name.'<br>Жанр: '.$directions[$song->direction_id]->name.'<br>Исполнитель: '.$executors[$song->executor_id]->name.'<br>Песня из альбома: '.$song->album.'<br>Стоимость: '.$song->value.'$';
			if (!isset($_SESSION['songsinbasket'][$song_id])){
				echo "<form action=\"confirmation.php\" method=\"POST\"><button  class=\"btn btn-lg btn-info\" name=\"but\">Добавить в корзину</button></form>";
			}
			else if (isset($_SESSION['songsinbasket'][$song_id])){
				echo "<form action=\"confirmation.php\" method=\"POST\"><button  class=\"btn btn-lg btn-info\" name=\"but\">Убрать из корзины</button></form>";				
			}
			echo '<hr>'.$song->text;
		}
	}
?>

	<audio src="songs/Michael Jackson - They Don’t Care About Us (Brazil Version) (Official Video).mp3" preload="auto" controls>
	</audio>

	<script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>
	<script type="text/javascript" src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
	<script type="text/javascript" src="slick/slick.min.js"></script>
    <script src="js/slider.js"></script>

</body>
</html>