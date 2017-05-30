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
    <link rel="stylesheet" href="css/style.css">
  </head>
<body>

<a href="/">Главная</a><br>
<a href="/">Помошь</a><br>
<a href="/">Доставка</a><br>
<a href="/">Способы оплаты</a><br>
<hr>
<a href="/">Все песни</a><br>
<a href="/">Исполнители</a><br>
<a href="/directions.php">Жанры</a><br>
<a href="/articles.php">Статьи</a><br>
<a href="/">Альбомы</a><br>
<a href="/">Популярное</a><br>
<a href="/">Рекомендации</a><br>
<hr>
<a href="/">Искать</a><br>
<hr>
<a href="/">Корзина</a><br>
<hr>
<?php
    $directions = R::findAll('directions');
    echo "Все жанры:<br>";
    foreach ($directions as $direction) {
        echo '№'.$direction->id.'<a href="/songs.php?direction_id='.$direction->id.'">'.$direction->name.'</a><br>';
    }
?>