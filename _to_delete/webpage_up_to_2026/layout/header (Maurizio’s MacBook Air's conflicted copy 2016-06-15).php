<?
$pages = 'pages/';

$menu['index'] = 'Home';
$menu['research'] = 'Research';
$menu['biography'] = 'Biography';
$menu['publications'] = 'Publications';
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
  <title>Dr Maurizio Filippone - <? echo $title; ?></title>

  <link rel="stylesheet" type="text/css" href="<?echo $root;?>layout/style.css">

  <meta name="Keywords" content="maurizio filippone">
  <meta name="Author" content="Maurizio Filippone">

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-29625288-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

<meta HTTP-EQUIV="Pragma" content="no-cache">
<meta HTTP-EQUIV="Expires" content="-1">

</head>


<body>

<div id="titlecontainer">

<div id="title_img">
  <a href="http://www.eurecom.fr/en/" target="_blank">
  <img id="imglogo" src="<?echo $root;?>/layout/logoEURECOM.jpeg" alt="Logo EURECOM">
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
    <a href="<?echo $root;?>index.html"><?echo $menu['index'];?></a>
  </div>
  <div class="divider"></div>

  <div class="menu_section"><?echo $menu['research'];?></div>
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>biography.html"><?echo $menu['biography'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>publications.html"><?echo $menu['publications'];?></a>
  </div>

<!--
   <div class="menu_page">
     <a href="<?echo $root.$pages;?>phd_projects.html"><?echo $menu['phdprojects'];?></a>
   </div> 
-->

  <div class="menu_page">
    <a href="<?echo $root.$pages;?>cv/short_cv.pdf" target="_blank"><?echo $menu['shortcv'];?></a>
  </div>
<!--
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>cv/cv_en.pdf" target="_blank"><?echo $menu['curriculumen'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>cv/cv_it.pdf" target="_blank"><?echo $menu['curriculumit'];?></a>
  </div>
  <div class="divider"></div>
  <div class="menu_section"><?echo $menu['music'];?></div>
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>gears.html"><?echo $menu['gears'];?></a>
  </div>
  <div class="menu_page">
    <a href="<?echo $root.$pages;?>media.html"><?echo $menu['media'];?></a>
  </div>
-->

<!--
  <div class="divider"></div>
  <div class="menu_section"><?echo $menu['others'];?></div>

  <div class="menu_page">
    <a href="<?echo $root.$pages;?>sport.html"><?echo $menu['sport'];?></a>
  </div>

  <div class="menu_page">
    <a href="<?echo $root.$pages;?>links.html"><?echo $menu['links'];?></a>
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

  <div class="lastupdate"><b>Last updated</b>: <br><em>27 May 2016</em></div>

  <div class="divider"></div>

</div>

<div id = "menu_end"></div>

</div>

<div id="content">
