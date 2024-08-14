<?php 
$pages = 'pages/';

$menu['index'] = 'Home';
$menu['research'] = 'Research';
$menu['biography'] = 'Biography';
$menu['publications'] = 'Publications';
$menu['axachair'] = 'AXA Chair';
$menu['shortcv'] = 'Short CV';
$menu['curriculumen'] = 'Full CV - En';
$menu['curriculumit'] = 'Full CV - It';
$menu['phdprojects'] = 'PhD projects';
$menu['others'] = 'Others';
$menu['music'] = 'Music';
$menu['gears'] = 'Gears';
$menu['media'] = 'Media';
$menu['sport'] = 'Sport';
$menu['links'] = 'Links';
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html>

<head>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
  <title>Dr Maurizio Filippone - <?php  echo $title; ?></title>

  <link rel="stylesheet" type="text/css" href="<?php echo $root;?>layout/style.css">

  <meta name="Keywords" content="maurizio filippone">
  <meta name="Author" content="Maurizio Filippone">


<meta HTTP-EQUIV="Pragma" content="no-cache">
<meta HTTP-EQUIV="Expires" content="-1">

</head>


<body>

<div id="titlecontainer">

<div id="title_img">
  <a href="https://www.kaust.edu.sa/en/" target="_blank">
  <img id="imglogo" src="<?php echo $root;?>/layout/logoKAUST.png" alt="Logo KAUST">
  </a>
</div>

<div id="title">
  DR MAURIZIO FILIPPONE
</div>

<div style="clear:both;"></div>

</div>

<div id = "menucontainer">
<div id = "menu">

  <div id="menu_label">
    MENU
  </div>
  <div class="divider"></div>

  <div class="menu_page">
    <a href="<?php echo $root;?>index.html"><?php echo $menu['index'];?></a>
  </div>
  <div class="divider"></div>

  <div class="menu_section"><?php echo $menu['research'];?></div>
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>biography.html"><?php echo $menu['biography'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>publications.html"><?php echo $menu['publications'];?></a>
  </div>
<!--
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>axachair.html"><?php echo $menu['axachair'];?></a>
  </div>
-->

<!--
   <div class="menu_page">
     <a href="<?php echo $root.$pages;?>phd_projects.html"><?php echo $menu['phdprojects'];?></a>
   </div> 
-->

<!--
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>cv/short_cv.pdf" target="_blank"><?php echo $menu['shortcv'];?></a>
  </div>
-->
<!--
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>cv/cv_en.pdf" target="_blank"><?php echo $menu['curriculumen'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>cv/cv_it.pdf" target="_blank"><?php echo $menu['curriculumit'];?></a>
  </div>
  <div class="divider"></div>
  <div class="menu_section"><?php echo $menu['music'];?></div>
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>gears.html"><?php echo $menu['gears'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>media.html"><?php echo $menu['media'];?></a>
  </div>
-->

<!--
  <div class="divider"></div>
  <div class="menu_section"><?php echo $menu['others'];?></div>

  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>sport.html"><?php echo $menu['sport'];?></a>
  </div>

  <div class="menu_page">
    <a href="<?php echo $root.$pages;?>links.html"><?php echo $menu['links'];?></a>
  </div>

  <div class="divider"></div>

  <div class="menu_img">
   <a href="http://jigsaw.w3.org/css-validator/" target="_blank"><img style="border:0;width:88px;height:31px"
    src="http://jigsaw.w3.org/css-validator/images/vcss" alt="Valid CSS!"></a>
  </div>
  <div class="menu_img">
  <a href="http://validator.w3.org/check?uri=referer" target="_blank"><img style="border:0" src="http://www.w3.org/Icons/valid-html401"
    alt="Valid HTML 4.01 Transitional" height="31" width="88"></a>
  </div>

-->

  <div class="divider"></div>

  <div class="lastupdate"><b>Last updated</b>: <br><em>14 Aug 2024</em></div>

  <div class="divider"></div>

</div>

<div id = "menu_end"></div>

</div>

<div id="content">
